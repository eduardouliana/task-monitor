import importlib.util

class TaskFactory():

    def execute(self, kind, configuration):
        spec = importlib.util.spec_from_file_location(f"kinds.{kind}", f"kinds/{kind}.py")
        spec_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(spec_module)
        spec_module.Task(configuration).execute()