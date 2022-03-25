from datetime import datetime
from croniter import croniter


class Cron:
    def __init__(self, json_schedule):
        if not croniter.is_valid(json_schedule["cron"]):
            raise Exception("Invalid cron")

        self._iter = croniter(json_schedule["cron"], datetime.now())
        self._next_execution = self._iter.get_next(datetime)

    def is_time_to_run(self):
        _is_time = self._next_execution <= datetime.now()

        if _is_time:
            self._next_execution = self._iter.get_next(datetime)

        return _is_time
