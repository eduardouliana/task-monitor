from task.factory import TaskFactory
from notification.factory import NotificationFactory

class Runner():

    def __init__(self, tasks):
        self.__tasks = tasks

    def __is_time_to_run(self, schedule):
        return True

    def __get_task_message(self, kind, configuration):
        task = TaskFactory(kind).get_instance(configuration)
        message = task.execute()
        del task

        return message

    def __send_notification(self, kind, data, message):
        notification = NotificationFactory(kind).get_instance(data)
        notification.send(message)
        del notification

    def perform(self):
        for task in self.__tasks:
            if not self.__is_time_to_run(task['schedule']):
                continue

            message = self.__get_task_message(task['kind'], task['configuration'])

            if not message:
                continue

            for notification in task['notifications']:
                self.__send_notification(notification['kind'], notification['data'], message)
