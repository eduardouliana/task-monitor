class Schedule:
    def __init__(self, json_schedule):
        self.kind = json_schedule["kind"]
        self.time = json_schedule["time"]
        self.start = json_schedule["start"]
        self.end = json_schedule["end"]
