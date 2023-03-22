import unittest
from console import HBNBCommand
from models import storage


class TestDoCreate(unittest.TestCase):
    def test_no_args(self):
        """
        If no args are provided to the 'do_create'
        function in the CMD, HBNBCommand should print
        "** class name missing **" and not change anything
        in the 'storage.all()' dictionary.
        """
        previous = storage.all().copy()
        console = HBNBCommand()
        console.do_create()
        current = storage.all().copy()
        self.assertEqual(previous, current)
