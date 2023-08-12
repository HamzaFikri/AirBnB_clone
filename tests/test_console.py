#!/usr/bin/python3
"""
Tests for module of BaseModel class
"""
import os
import sys
import unittest
import datetime
import console
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """
    Testing the class.
    """
    def test_instance_no_arg(self):
        msj = "Bad id for BaseModel without args"
        my_model1 = HBNBCommand()
        self.assertIsNotNone(my_model1.prompt, msj)

class TestHBNBCommand_documentation(unittest.TestCase):
    """
    Testing the documentation
    """
    def test_module_docstring(self):
        """
        Test if modules have docstring
        """
        obj = console.__doc__
        msj = "Module does not has docstring"
        self.assertIsNotNone(obj, msj)  # Classes

    def test_class_docstring(self):
        """
        Test if class have docstring
        """
        obj = console.HBNBCommand.__doc__
        msj = "Class does not has docstring"
        self.assertIsNotNone(obj, msj)  # Classes

    def test_do_EOF_docstring(self):
        """
        Test if method has docstring
        """
        obj = console.HBNBCommand.do_EOF.__doc__
        msj = "Method do_EOF does not has docstring"
        self.assertIsNotNone(obj, msj)  # Classes

    def test_do_quit_docstring(self):
        """
        Test if method has docstring
        """
        obj = console.HBNBCommand.do_quit.__doc__
        msj = "Method do_quit does not has docstring"
        self.assertIsNotNone(obj, msj)  # Classes

    def test_do_create_docstring(self):
        """
        Test if method has docstring
        """
        obj = console.HBNBCommand.do_quit.__doc__
        msj = "Method do_create does not has docstring"
        self.assertIsNotNone(obj, msj)  # Classes

    def test_do_show_docstring(self):
        """
        Test if method has docstring
        """
        obj = console.HBNBCommand.do_show.__doc__
        msj = "Method do_show does not has docstring"
        self.assertIsNotNone(obj, msj)  # Classes

    def test_do_show_docstring(self):
        """
        Test if method has docstring
        """
        obj = console.HBNBCommand.do_show.__doc__
        msj = "Method do_show does not has docstring"
        self.assertIsNotNone(obj, msj)  # Classes

if __name__ == "__main__":
    unittest.main()
