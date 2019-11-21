"""
    VcScheduleFetcher. Fetch calendar information from webuntis for Virtual Classroom Project

Usage:
    vcschedulefetch <vc_username> <vc_password> <webuntis_user> <webuntis_pwd> [-h] [-v...] [options]

Options:
    -h, --help                          Print this help text
    -v                                  Set the loglevel

Operations:
    -u --update-schedule                Updates the schedule of recording-enabled rooms
    -c --update-courses                 Bulk updates all courses in the API
    -a <room>, --add-room <room>        Adds the specified room to the list of recording-enabled rooms
    -p <limit>, --print-rooms <limit>   Print <limit> amount of recording-enabled-rooms. [<limit> | all]

Config:
    --schedule-start <start_date>       Set the start date of the scheduled fetched by update-schedule.
                                        The date must be in the format DD-MM-YYYY
    --schedule-end <end_date>           Set the end date of the scheduled fetched by update-schedule
    --api-url <url>                     Url of the api to use [default: https://vc-api.amavin.dk]
    --no-verify-certs                   Disables certificate validation of the https api endpoint 
"""


from docopt import docopt
from webuntis_fetcher import WebuntisFetcher
import openapi_client
import logging
import datetime


class VcScheduleFetcher:
    def __init__(self):
        self.api_conf = None
        self.api_client = None
        self.schedule_api = None
        self.auth_api = None
        self.course_api = None
        self.untis = None
        self.log = logging.getLogger(__name__)

    def _get_jwt_token(self, username, password):
        try:
            login_rsp = self.auth_api.api_authentication_post(
                login_model=openapi_client.LoginModel(user_name=username, password=password))
            return login_rsp.token
        except openapi_client.ApiException as e:
            self.log.exception("Exception when calling AuthenticationApi->api_authentication_post: %s\n" % e)

    def _fetch_schedules(self, start, end):
        start, end = self._sanitize_dates(start, end)
        if start and end:
            rooms = self.schedule_api.api_schedule_get_rooms_get()
            self.log.info("Updating schedule for %d rooms.." % len(rooms))
            for room in rooms:
                room_schedule = self.untis.get_schedule_for_room(room, start, end)
                self.schedule_api.api_schedule_post(scheduled_session=room_schedule)
            self.log.info("Completed updating schedule.")
        else:
            self.log.error("Unable to fetch schedules. No dates provided")

    def _post_courses(self):
        courses = self.untis.get_courses()
        courses_updated = self.course_api.api_courses_add_range_post(course=courses)
        self.log.info("Updated %d courses" % courses_updated)

    def _sanitize_dates(self, start, end):
        today = datetime.date.today()
        start = self._parse_date(start)
        end = self._parse_date(end)
        if isinstance(start, bool) or isinstance(end, bool):
            return None  # Unable to parse dates

        if not start and not end:
            start = today - datetime.timedelta(days=today.weekday())
            end = start + datetime.timedelta(days=7)
        elif not end:
            end = start + datetime.timedelta(days=7)
        elif not start:
            start = end - datetime.timedelta(days=7)

        self.log.info("Using start date of %s" % start.strftime("%d-%m-%Y"))
        self.log.info("Using end date of %s" % end.strftime("%d-%m-%Y"))
        return start, end

    def _add_room(self, room):
        room_obj = self.untis.get_room(room)
        if room_obj:
            try:
                self.schedule_api.api_schedule_add_room_post(room=room_obj)
                self.log.info("Room \"%s\" has been enabled for recording." % room)
            except openapi_client.ApiException as e:
                if e.reason == "Conflict":
                    self.log.warning("Room \"%s\" is already enabled for recording." % room)
                else:
                    raise
        else:
            self.log.error("Room \"%s\" was not found." % room)

    def _print_room_list(self, limit):
        if limit == 'all':
            limit = 0
        room_list = self.schedule_api.api_schedule_get_rooms_get(limit=limit)
        for room in room_list:
            print("Room: %s" % room.name)

    def _parse_date(self, date):
        if date:
            try:
                return datetime.datetime.strptime(date, "%d-%m-%Y")
            except ValueError:
                self.log.error("Unable to parse date string %s" % date)
                return False

    def main(self):
        arguments = docopt(__doc__)
        logging.basicConfig(level=-10 * arguments["-v"] + 30)

        if not (arguments["--update-schedule"] or arguments["--update-courses"]
                or arguments["--add-room"] or arguments["--print-rooms"]):
            self.log.error("Please provide an operation option")
            exit(1)
            
        self.api_conf = openapi_client.Configuration(host=arguments["--api-url"])
        self.api_conf.verify_ssl = False if arguments["--no-verify-certs"] else True
        self.api_client = openapi_client.ApiClient(configuration=self.api_conf)
        self.auth_api = openapi_client.AuthenticationApi(self.api_client)
        self.schedule_api = openapi_client.ScheduleApi(self.api_client)
        self.course_api = openapi_client.CoursesApi(self.api_client)
        self.untis = WebuntisFetcher(arguments["<webuntis_user>"], arguments["<webuntis_pwd>"])

        auth_token = self._get_jwt_token(arguments["<vc_username>"], arguments["<vc_password>"])
        if auth_token:
            self.api_conf.access_token = auth_token
            self.log.debug("Authorized as %s with JWT token %s" % (arguments["<vc_username>"], auth_token))
        else:
            self.log.error("Unable to authenticate as %s. Exiting.." % arguments["<vc_username>"])
            exit(1)

        if arguments["--print-rooms"]:
            self._print_room_list(arguments["--print-rooms"])
        else:
            self.untis.login()
            if arguments["--add-room"]:
                self._add_room(arguments["--add-room"])
            if arguments["--update-courses"]:
                self._post_courses()
            if arguments["--update-schedule"]:
                self._fetch_schedules(arguments["--schedule-start"], arguments["--schedule-end"])


# When run as console script through setup.py entry_point:
def main():
    VcScheduleFetcher().main()

# When run as script with python -m:
VcScheduleFetcher().main() 
