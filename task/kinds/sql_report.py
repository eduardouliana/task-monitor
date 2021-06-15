from database.postgresql import Postgresql

class Task():

    def __init__(self, configuration):
        self.__sql_command = configuration['sql-command']
        self.__message_format = configuration['message-format']
        database = configuration['database']
        self.__postgresql = Postgresql(
            database['host'],
            database['database'],
            database['username'],
            database['password'],
        )

    def __del__(self):
        del self.__postgresql

    def execute(self):
        query = self.__postgresql.get_query(self.__sql_command)
        records = query.fetchall()

        messages = []
        for record in records:
            message = self.__message_format.format(*record)
            messages.append(message)

        query.close()

        return '\n\n'.join(messages)
