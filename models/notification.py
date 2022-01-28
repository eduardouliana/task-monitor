from models.notification_data import NotificationData


class Notification:
    def __init__(self, json_notification):
        self.kind = json_notification["kind"]
        self.data = NotificationData(json_notification["data"])
