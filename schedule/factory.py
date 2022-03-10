from schedule.kinds.cron import Cron
from schedule.kinds.interval import Interval


class KindFactory:
    def __init__(self, json_schedule):
        self._kind_list = {"interval": Interval, "cron": Cron}
        self._kind = json_schedule["kind"]

        if not self._kind in self._kind_list:
            raise Exception("Invalid schedule kind")

        self._json_schedule = json_schedule

    def new(self):
        return self._kind_list[self._kind](self._json_schedule)
