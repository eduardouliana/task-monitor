from database.realtime_db import RealTimeDB
import json

class Tasks():

    def get_from_firebase(self, db_name, data_path):
        firebase = RealTimeDB(db_name)
        return firebase.get(data_path)


    def get_from_json_file(self, file_path):
        with open(file_path) as json_file:
            return json.load(json_file)
