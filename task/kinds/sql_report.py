from utils.postgresql import Postgresql
from utils.postgresql import Postgresql

class Task():
    def __init__(self, configuration):
        self.__sql_command = configuration['sql-command']
        self.__message_format = configuration['message-format']
        self.__postgresql = Postgresql(
            configuration['host'],
            configuration['database'],
            configuration['username'],
            configuration['password'],
        )

    def execute(self):
        query = self.__postgresql.get_query(self.__sql_command)
        records = query.fetchall()

        messages = []
        for record in records:
            message = self.__message_format.format(*record)
            messages.add(message)

        return '\\n'.join(messages)
