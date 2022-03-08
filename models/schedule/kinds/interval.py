from datetime import datetime


class Interval:
    def __init__(self, time, start, end):
        self.time = time
        self.start = start
        self.end = end
        self.next_execution = datetime.min

    def is_time_to_run(self):
        current_date_time = datetime.now()

        if (self.next_execution <= current_date_time) and (
            self.start <= current_date_time.time() <= self.end
        ):
            self.next_execution = current_date_time + self.time
            return True

        return False