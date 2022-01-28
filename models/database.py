class Database:
    def __init__(self, json_database):
        self.user = json_database["username"]
        self.password = json_database["password"]
        self.host = json_database["host"]
        self.database = json_database["database"]
