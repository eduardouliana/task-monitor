import importlib.util

class BaseFactory():

    __MODULE_NAME_FORMAT = "base.{}"
    __FILE_PATH_FORMAT = "base/{}.py"

    def __init__(self, kind):
        module_name = self.__MODULE_NAME_FORMAT.format(kind)
        file_path = self.__FILE_PATH_FORMAT.format(kind)
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        self.__spec_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.__spec_module)
