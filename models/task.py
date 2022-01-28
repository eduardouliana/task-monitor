from models.configuration import Configuration
from models.notification import Notification
from models.schedule import Schedule


class Task:
    def __init__(self, json_task):
        self.name = json_task["name"]
        self.kind = json_task["kind"]
        self.schedule = Schedule(json_task["schedule"])
        self.configuration = Configuration(json_task["configuration"])
        self.notifications = [
            Notification(element) for element in json_task["notifications"]
        ]
