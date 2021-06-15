import unittest
from core.factory import BaseFactory

class MyFactory(BaseFactory):

    __MODULE_NAME_FORMAT = "tests.resources.factory_test.{}"
    __FILE_PATH_FORMAT = "tests/resources/factory_test/{}.py"

    def execute(self):
        return "ok"

class TestStringMethods(unittest.TestCase):

    def test_execute_factory(self):
        s = MyFactory('text_output').execute()
        self.assertEqual(s, 'ok')

if __name__ == '__main__':
    unittest.main()

