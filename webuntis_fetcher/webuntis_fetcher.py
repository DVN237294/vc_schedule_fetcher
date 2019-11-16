import webuntis
import logging
from openapi_client import ScheduledSession, Course, Room


class WebuntisFetcher:
    def __init__(self, username, password):
        self.session = webuntis.Session(
            username=username,
            password=password,
            server='skema.via.dk',
            school='viauc',
            useragent='Virtual Classroom BachelorProject. 237294(at)via.dk',
            cachelen=100
        )
        self.log = logging.getLogger(__name__)

    def login(self):
        self.session.login()

    def get_schedule_for_room(self, room, start, end):
        tt = self.session.timetable(room=room.webuntis_id, start=start, end=end)
        return [ScheduledSession(webuntis_id=ses.id, webuntis_course_id=p.id, room_id=room.id,
                                 start_time=ses.start, end_time=ses.end,
                                 webuntis_teacher_ids=list(map(lambda x: x['id'], ses._data['te']))
                                 if len(ses._data['te']) > 0 else [])
                for ses in tt for p in ses.subjects]

    def get_courses(self):
        subjects = self.session.subjects()
        return [Course(webuntis_course_id=subject.id, name=subject.name) for subject in subjects]

    def get_room(self, name):
        room_list = self.session.rooms().filter(name=name)
        if len(room_list) > 0:
            room_obj = room_list[0]
            return Room(webuntis_id=room_obj.id, name=room_obj.name)
        return None


