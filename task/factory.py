from core.factory import BaseFactory

class TaskFactory(BaseFactory):

    __MODULE_NAME_FORMAT = "task.kinds.{}"
    __FILE_PATH_FORMAT = "task/kinds/{}.py"

    def get_instance(self, configuration):
        return self.__spec_module.Task(configuration)
