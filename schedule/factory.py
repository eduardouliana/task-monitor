from schedule.kinds.cron import Cron
from schedule.kinds.interval import Interval


class ScheduleFactory:
    __KINDS = {"interval": Interval, "cron": Cron}
    
    def __init__(self, json_schedule):
        schedule_kind = json_schedule["kind"]

        if not schedule_kind in self.__KINDS:
            raise Exception("Invalid schedule kind")

        self._kind = self.__KINDS[schedule_kind]
        self._json_schedule = json_schedule

    def new(self):
        return self._kind(self._json_schedule)
