import importlib.util

class NotificationFactory():

    def execute(self, kind, data, message):
        spec = importlib.util.spec_from_file_location(f"notification.kinds.{kind}", f"notification/kinds/{kind}.py")
        spec_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(spec_module)
        spec_module.Notification(data).execute(message)        