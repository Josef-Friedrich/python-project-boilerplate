import unittest

import python_project_boilerplate


class PythonProjectBoilerplateTest(unittest.TestCase):
    def test_version(self):
        self.assertEqual(python_project_boilerplate.__version__, "0.1.0")

    def test_print(self):
        print("use nose2 --output-buffer to capture the printed test")
