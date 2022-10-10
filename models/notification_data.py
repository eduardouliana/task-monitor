import os
from dotenv import load_dotenv

from models.date_configuration import DateConfiguration


class NotificationData:
    def __init__(self, json_notification_data):
        load_dotenv()

        self.url = os.getenv(json_notification_data["url"])
        self.user_name = json_notification_data["user-name"]
        self.avatar_url = json_notification_data["avatar-url"]
        self.color = json_notification_data["color"]
        self.title = json_notification_data["title"]
        self.date_configuration = DateConfiguration(json_notification_data.get("date-configuration", dict()))
