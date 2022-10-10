class DateConfiguration:
    def __init__(self, json_notification_data) -> None:
        self.date_on_title = json_notification_data.get("date-on-title", False)
        self.days_offset = json_notification_data.get("days-offset", 0)
        self.date_format = json_notification_data.get("date-format", "%d-%m-%Y")