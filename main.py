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

def __get_task_message(kind, configuration):
    task = TaskFactory(kind).get_instance(configuration)
    message = task.execute()
    del task

    return message

def __send_notification(kind, data, message):
    notification = NotificationFactory(kind).get_instance(data)
    notification.send(message)
    del notification

def __execute(tasks):
    for task in tasks:
        if not __is_time_to_run(task['schedule']):
            continue

        message = __get_task_message(task['kind'], task['configuration'])

        if not message:
            continue

        for notification in task['notifications']:
            __send_notification(notification['kind'], notification['data'], message)

def main():
    tasks = __load_tasks()

    while True:
        __execute(tasks)
        timer.sleep(5 * 60)

if __name__ == '__main__':
    main()
