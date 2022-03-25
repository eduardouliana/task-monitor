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
        current_date_time = datetime.now()

        if (current_date_time <= self._next_execution):
            return False

        is_time = self._start <= current_date_time.time() <= self._end
    
        if is_time:
            self._next_execution = current_date_time + self._time

        return is_time
