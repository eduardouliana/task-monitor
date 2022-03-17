from models.configuration import Configuration
from models.notification import Notification
from schedule.factory import ScheduleFactory


class Task:
    def __init__(self, json_task):
        self.name = json_task["name"]
        self.kind = json_task["kind"]
        self.schedules = [
            ScheduleFactory(schedule_item).new() for schedule_item in json_task["schedule"]
        ]
        self.configuration = Configuration(json_task["configuration"])
        self.notifications = [
            Notification(element) for element in json_task["notifications"]
        ]

    def can_run(self):
        for schedule in self.schedules:
            if schedule.is_time_to_run():
                return True

        return False