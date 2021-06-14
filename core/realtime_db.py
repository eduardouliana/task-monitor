import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class RealTimeDB():

    def __init__(self, account_key_path, realtime_db_name):
        cred = credentials.Certificate(account_key_path)
        url = f'https://{realtime_db_name}.firebaseio.com/'
        firebase_admin.initialize_app(cred, {'databaseURL': url})

    def get(self):
        ref = db.reference('/tasks/')
        return ref.get()
