import unittest
from console import HBNBCommand
from models import storage


class TestDoCreate(unittest.TestCase):
    console = HBNBCommand()

    def test_no_args(self):
        """
        If no args are provided to the 'do_create'
        function in the CMD, HBNBCommand should print
        "** class name missing **" and
        NOT CHANGE ANYTHING AT ALL
        in the 'storage.all()' dictionary.
        """
        previous = storage.all().copy()
        self.console.do_create("")
        current = storage.all().copy()
        self.assertEqual(previous, current)

    def test_invalid_class(self):
        """
        If the class specified in the name doesn't exist,
        HBNBCommand should print "** class doesn't exist **"
        and NOT CHANGE ANYTHING AT ALL in the
        'storage.all()' dictionary.
        """
        previous = storage.all().copy()
        self.console.do_create("HotDogs")
        current = storage.all().copy()
        self.assertEqual(previous, current)

    def test_correct_classes(self):
        """
        If the classes are correct, but the attrs
        are wrong, the class itself should print
        "Invalid attribute key:value pair for '{type(self)}': {k}:{v}"
        and NOT CHANGE ANYTHING AT ALL in the
        'storage.all()' dictionary.
        """
        previous = storage.all().copy()
        self.console.do_create("BaseModel god_loves_you=\"true\"")
        current = storage.all().copy()
        self.assertEqual(previous, current)

        previous = storage.all().copy()
        self.console.do_create("Amenity never=\"gonna\"")
        current = storage.all().copy()
        self.assertEqual(previous, current)

        previous = storage.all().copy()
        self.console.do_create("Place give=\"you\"")
        current = storage.all().copy()
        self.assertEqual(previous, current)

        previous = storage.all().copy()
        self.console.do_create("Review up=0")
        current = storage.all().copy()
        self.assertEqual(previous, current)
    
    def test_correct_class_and_params(self):
        """
        If the class and arg names are correct,
        but the arg values are wrong,
        they should be skipped.
        """
        pass
