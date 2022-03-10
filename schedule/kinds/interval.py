from datetime import datetime, timedelta


class Interval:
    def __init__(self, json_schedule):
        self._time = timedelta(minutes=json_schedule["time"])
        self._start = self._parse_time(json_schedule["start"])
        self._end = self._parse_time(json_schedule["end"])
        self._next_execution = datetime.min

    def _parse_time(self, time):
        return datetime.strptime(time, "%H:%M").time()

    def is_time_to_run(self):
        _current_date_time = datetime.now()
        _is_time = (self._next_execution <= _current_date_time) and (
            self._start <= _current_date_time.time() <= self._end
        )

        if _is_time:
            self._next_execution = _current_date_time + self._time

        return _is_time
