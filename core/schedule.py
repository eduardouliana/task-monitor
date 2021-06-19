from datetime import datetime, time

class Schedule():

    def __init__(self, start, end, ):
        self.__start = time.fromisoformat(start)
        self.__end = time.fromisoformat(end)

    def is_in_period(self, start, end):
        now = datetime.now().time()

        return (now > start_time) and (now < end_time)
