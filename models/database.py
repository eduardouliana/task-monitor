import os
from dotenv import load_dotenv


class Database:
    def __init__(self, json_database):
        load_dotenv()

        self.user = os.getenv(json_database["username"])
        self.password = os.getenv(json_database["password"])
        self.host = os.getenv(json_database["host"])
        self.database = os.getenv(json_database["database"])
