# from jobs.redmine import Redmine
from datetime import datetime
from models.schedule import Schedule
from models.task import Task
from task.factory import TaskFactory
from notification.factory import NotificationFactory
import time as timer
import json


def __load_tasks():
    with open("tasks.json") as json_file:
        data = [Task(element) for element in json.load(json_file)]

    return data


def __is_time_to_run(schedule: Schedule):
    current_date_time = datetime.now()

    if schedule.next_execution <= current_date_time:
        schedule.next_execution = current_date_time + schedule.time
        return True

    return False


def main():
    tasks = __load_tasks()

    while True:
        for task in tasks:
            if __is_time_to_run(task.schedule):
                message = TaskFactory().execute(task.kind, task.configuration)

                if not message:
                    continue

                for notification in task.notifications:
                    NotificationFactory().execute(
                        notification.kind, notification.data, message
                    )

        timer.sleep(60)


if __name__ == "__main__":
    main()
