import os
from dotenv import load_dotenv


class NotificationData:
    def __init__(self, json_notification_data):
        load_dotenv()

        self.url = os.getenv(json_notification_data["url"])
        self.user_name = json_notification_data["user-name"]
        self.avatar_url = json_notification_data["avatar-url"]
        self.color = json_notification_data["color"]
        self.title = json_notification_data["title"]
        self.current_date_on_title = json_notification_data["current_date_on_title"]
