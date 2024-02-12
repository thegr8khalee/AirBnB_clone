import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, expected_output, mock_stdout, function_to_test, *args):
        function_to_test(*args)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_create(self):
        hbnb_cmd = HBNBCommand()
        with patch('sys.stdin', return_value='BaseModel'):
            self.assert_stdout("Usage: BaseModel.create()\n", hbnb_cmd.do_create, '')
        with patch('sys.stdin', return_value='MyModel'):
            self.assert_stdout("** class doesn't exist **\n", hbnb_cmd.do_create, '')
        with patch('sys.stdin', return_value='BaseModel'):
            self.assert_stdout("** instance id missing **\n", hbnb_cmd.do_create, '')
        with patch('sys.stdin', return_value='BaseModel'):
            with patch('models.storage.save') as mock_save:
                self.assert_stdout("0001-1234-5678\n", hbnb_cmd.do_create, '')
                mock_save.assert_called_once()

    def test_show(self):
        hbnb_cmd = HBNBCommand()
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            hbnb_cmd.do_show('')
            self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            hbnb_cmd.do_show('MyModel')
            self.assertEqual(mock_stdout.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            hbnb_cmd.do_show('BaseModel')
            self.assertEqual(mock_stdout.getvalue(), "** instance name missing **\n")
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            hbnb_cmd.do_show('BaseModel 1234')
            self.assertEqual(mock_stdout.getvalue(), "** no instance found **\n")

    # Add tests for other methods similarly

if __name__ == '__main__':
    unittest.main()
