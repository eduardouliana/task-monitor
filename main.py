from models.task import Task
from task.factory import TaskFactory
from notification.factory import NotificationFactory
import time as timer
import json


def __load_tasks():
    with open("tasks.json") as json_file:
        data = [Task(element) for element in json.load(json_file)]

    return data


def main():
    tasks = __load_tasks()

    while True:
        for task in tasks:
            if task.can_run():
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
