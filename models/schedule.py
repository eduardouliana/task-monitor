from datetime import datetime, time, timedelta


class Schedule:
    def __init__(self, json_schedule):
        self.kind = json_schedule["kind"]
        self.time = timedelta(minutes=json_schedule["time"])
        self.start = datetime.strptime(json_schedule["start"], "%H:%M").time()
        self.end = datetime.strptime(json_schedule["end"], "%H:%M").time()
        self.next_execution = datetime.min
