from utils.postgresql import Postgresql

class Task():
    def __init__(self, configuration):
        self.__sql_command = configuration['sql-command']
        self.__message_format = configuration['message-format']
        __database = configuration['database']
        self.__postgresql = Postgresql(
            __database['host'],
            __database['database'],
            __database['username'],
            __database['password'],
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

        return '\n\n'.join(messages)
