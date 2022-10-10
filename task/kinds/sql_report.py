import re

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
        translate_map = str.maketrans("\n\t\r", "   ")
        for record in records:
            new_record = list(record)
            for i, r in enumerate(new_record):
                if isinstance(r, str):
                    new_record[i] = re.sub(r' +', ' ', r.translate(translate_map).strip())

            message = self.__message_format.format(*new_record)

            if message.find("--url") >= 0:
                original_match = re.search(
                    r"--url\(((http:\/\/|https:\/\/).*)\)", 
                    repr(message),
                    flags=re.MULTILINE
                ).group()
                original_url, _ = re.search(
                    r"--url\(((http:\/\/|https:\/\/).*)\)", 
                    repr(message),
                    flags=re.MULTILINE
                ).groups()

                parsed_url = bytes(original_url, encoding= 'windows-1252').decode('unicode_escape').replace(" ", "+")

                message = message.replace(bytes(original_match, encoding= 'windows-1252').decode('unicode_escape'), parsed_url)

            messages.append(message)

        query.close()
        del self.__postgresql

        return "\n\n".join(messages)
