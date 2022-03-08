from datetime import datetime
from croniter import croniter

class Cron:
    def __init__(self, cron):
        if not croniter.is_valid(cron):
            raise Exception("Invalid cron")

        self.iter = croniter(cron, datetime.now())
        self.next_execution = self.iter.get_next(datetime)
        

    def is_time_to_run(self):
        current_date_time = datetime.now()

        if (self.next_execution <= current_date_time):
            self.next_execution = self.iter.get_next(datetime)
            return True

        current_date_time = datetime.now()

        return False