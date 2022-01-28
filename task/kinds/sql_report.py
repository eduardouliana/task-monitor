from models.configuration import Configuration
from utils.postgresql import Postgresql


class Task:
    def __init__(self, configuration: Configuration):
        self.__sql_command = configuration.sql_command
        self.__message_format = configuration.message_format
        __database = configuration.database
        self.__postgresql = Postgresql(
            __database.host,
            __database.database,
            __database.user,
            __database.password,
        )

    def execute(self):
        query = self.__postgresql.get_query(self.__sql_command)
        records = query.fetchall()

        messages = []
        for record in records:
            message = self.__message_format.format(*record)
            messages.append(message)

        query.close()
        del self.__postgresql

        return "\n\n".join(messages)
