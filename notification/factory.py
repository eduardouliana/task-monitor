from core.factory import BaseFactory

class NotificationFactory(BaseFactory):

    __MODULE_NAME_FORMAT = "notification.kinds.{}"
    __FILE_PATH_FORMAT = "notification/kinds/{}.py"

    def get_instance(self, data):
        return self.__spec_module.Notification(data)
