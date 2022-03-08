from datetime import datetime, timedelta
from models.schedule.kinds.cron import Cron
from models.schedule.kinds.interval import Interval


class Factory:
    def __init__(self, json_schedule):
        if json_schedule["kind"] == "interval":
            self.kind = Interval(
                timedelta(minutes=json_schedule["time"]),
                datetime.strptime(json_schedule["start"], "%H:%M").time(),
                datetime.strptime(json_schedule["end"], "%H:%M").time(),
            )
        elif json_schedule["kind"] == "cron":
            self.kind = Cron(json_schedule["cron"])


    def is_time_to_run(self):
        self.kind.is_time_to_run()