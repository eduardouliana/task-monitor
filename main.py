#from jobs.redmine import Redmine
from datetime import datetime, time
from task.factory import TaskFactory
from notification.factory import NotificationFactory
import time as timer
import json

def __load_tasks():
    with open('tasks.json') as json_file:
        data = json.load(json_file)

    return data        

def __is_time_to_run(schedule):
    return True

def main():
    tasks = __load_tasks()

    while True:
        for task in tasks:
            if __is_time_to_run(task['schedule']):
                message = TaskFactory().execute(task['kind'], task['configuration'])
                for notification in task['notifications']:
                    NotificationFactory().execute(notification['kind'], notification['data'], message)
            timer.sleep(5 * 60)    

if __name__ == '__main__':
    main()