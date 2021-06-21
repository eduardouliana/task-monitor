from datetime import datetime, time, timedelta

class Schedule():

    def __init__(self, schedule):
        self.__schedule = schedule
        self.__set_interval

    def __set_interval(self):
        self.__interval = timedelta(minutes = self.__times)

        if self.__schedule['kind'] == 'times':
            self.__interval = timedelta((60 * 24) / self.__times)

    def __set_next(self, value):
        self.__schedule['next'] = value

    def __kind(self):
        return self.__schedule['kind']

    def __time(self):
        return self.__schedule['time']

    def __next(self):
        return self.__schedule['next']

    def __start(self):
        time = self.__schedule['period']['start']
        return time.fromisoformat(time)

    def __stop(self):
        time = self.__schedule['period']['stop']
        return time.fromisoformat(time)

    def __is_in_period(self, value):
        return (value > self.__start) and (value < self.__end)

    def is_time_to_run(self):
        now = datetime.now().time()

        if not self.__is_in_period(now):
            return False

        if now >= self.__next:
            self.__set_next(now + self.__interval)
            return True

        return False
