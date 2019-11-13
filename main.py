"""
    VcScheduleFetcher. Fetch calendar information from webuntis for Virtual Classroom Project

Usage:
    vcschedulefetch <vc_username> <vc_password> <room>
"""


from docopt import docopt
import openapi_client


class Program:
    def __init__(self):
        self.api_conf = None
        self.api_client = None
        self.schedule_api = None
        self.auth_api = None

    def get_jwt_token(self, username, password):
        try:
            login_rsp = self.auth_api.api_authentication_post(
                login_model=openapi_client.LoginModel(user_name=username, password=password))
            return login_rsp.token
        except openapi_client.ApiException as e:
            print("Exception when calling AuthenticationApi->api_authentication_post: %s\n" % e)

    def main(self):
        arguments = docopt(__doc__)

        self.api_conf = openapi_client.Configuration(host="https://localhost:44388")
        self.api_conf.verify_ssl = False
        self.api_client = openapi_client.ApiClient(configuration=self.api_conf)
        self.auth_api = openapi_client.AuthenticationApi(self.api_client)
        self.schedule_api = openapi_client.ScheduleApi(self.api_client)

        auth_token = self.get_jwt_token(arguments["<vc_username>"], arguments["<vc_password>"])
        if auth_token:
            self.api_conf.access_token = auth_token
        else:
            print("Unable to get authenticate as %s. Exiting..", arguments["<vc_username>"])
            quit()

        result = self.schedule_api.api_schedule_add_room_room_name_post(room_name="MyRoom")
        print(result)


if __name__ == '__main__':
    Program().main()
