from models.database import Database


class Configuration:
    def __init__(self, json_configuration):
        self.database = Database(json_configuration["database"])
        self.sql_command = json_configuration["sql-command"]
        self.message_format = json_configuration["message-format"]
