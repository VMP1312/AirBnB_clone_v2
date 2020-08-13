#!/usr/bin/pytho3
from unittest.mock import patch
import unittest
import pep8
import sys
import os


class TestConsole(unittest.TestCase):
    """ Testcases for the console """

    @classmethod
    def setUpClass(cls):
        """setup"""
        cls.console = HBNBCommand()

    @classmethod
    def teardown(cls):
        """TearDown"""
        del cls.console
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8(self):
        """ Tests pep8 """
        style = pep8.StyleGuide(quiet=True)
        files = ["console.py", "test/test_console.py"]
        result = style.check_files(files)
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")

    def test_documentation(self):
        """checking the documentation"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.count.__doc__)
        self.assertIsNotNone(HBNBCommand.strip_clean.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

        def test_emptyline(self):
            """Test empty line"""
            with patch("sys.stdout", new=StringIO()) as f:
                self.consol.onecmd("\n")
                self.assertEqual("", f.getvalue())

    def test_quit(self):
        """test quit command"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("quit")
            self.assertEqual("", f.getvalue())


if __name__ == "__main__":
    unittest.main()
