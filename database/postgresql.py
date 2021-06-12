import psycopg2

class Postgresql:
    def __init__(self, host, database, user, password, timeout=120):
        self.__connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            connect_timeout=timeout,
        )

    def __del__(self):
        self.__connection.close()

    def get_query(self, command):
        try:
            query = self.__connection.cursor()
            query.execute(command)

            return query
        except Exception as error:
            return f"Erro: {error}"
