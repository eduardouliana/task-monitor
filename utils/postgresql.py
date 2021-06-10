import psycopg2

class Postgresql:
    def getExecuteQuery(self, host, database, user, password, command, timeout=120):
        try:
            connection = psycopg2.connect(
                host=host,
                database=database,
                user=user,
                password=password,
                connect_timeout=timeout,
            )
            query = connection.cursor()
            query.execute(command)
            result = query.fetchall()
            query.close()
            connection.close()

            return result

        except Exception as error:
            return f"Erro: {error}"
