#!/usr/bin/python3
"""
Tests for module of Review class
"""
import os
import unittest
import datetime
import models
import models.review
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Testing the class.
    """
    def test_instance_no_arg(self):
        msj = "Bad id for Review without args"
        my_model1 = Review()
        self.assertIsNotNone(my_model1.id, msj)

    def test_instance_arg(self):
        msj = "Bad id for Review with args"
        my_model_json = {'id': 'd2f054ed-7125-4417-8416-aea973791d04',
                         'my_number': 89, 'name': 'AlxHolberton',
                         'created_at': datetime.datetime(2020, 2, 19, 19,
                                                         14, 55, 659675),
                         'updated_at': datetime.datetime(2020, 2, 19, 19,
                                                         14, 55, 659675)}
        my_model1 = Review(**my_model_json)
        self.assertIsNotNone(my_model1.id, msj)

    def test_no_arg_random(self):
        msj = "Id Review no random for created Review"
        my_model1 = Review()
        my_model2 = Review()
        self.assertNotEqual(my_model1.id, my_model2.id, msj)

    def test_no_arg_timestamp(self):
        msj = "Date Review bad timestamp"
        my_model1 = Review()
        self.assertEqual(my_model1.created_at, my_model1.updated_at, msj)

    def test_id_public(self):
        msj = "Id isn't public"
        my_model1 = Review()
        my_model1.id = "HELLO"
        self.assertEqual(my_model1.id, "HELLO")

    def test_name_public(self):
        msj = "Name isn't public"
        my_model1 = Review()
        my_model1.name = "AlxHolberton"
        self.assertEqual(my_model1.name, "AlxHolberton")

    def test_place_id__public(self):
        msj = "Place_id isn't public"
        my_model1 = Review()
        my_model1.place_id = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        self.assertEqual(my_model1.place_id,
                         "b6a6e15c-c67d-4312-9a75-9d084935e579")

    def test_user_id__public(self):
        msj = "User_id isn't public"
        my_model1 = Review()
        my_model1.user_id = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        self.assertEqual(my_model1.user_id,
                         "b6a6e15c-c67d-4312-9a75-9d084935e579")

    def test_text_public(self):
        msj = "Text isn't public"
        my_model1 = Review()
        my_model1.text = "Define your future"
        self.assertEqual(my_model1.text, "Define your future")

    def test_id(self):
        '''test if the id of two instances are different'''
        my_model = Review()
        my_model1 = Review()
        self.assertNotEqual(my_model.id, my_model1.id)

    def test_executable_file(self):
        '''test if file has permissions u+x to execute'''
        # Check for read access
        is_read_true = os.access('models/review.py', os.R_OK)
        self.assertTrue(is_read_true)
        # Check for write access
        is_write_true = os.access('models/review.py', os.W_OK)
        self.assertTrue(is_write_true)
        # Check for execution access
        is_exec_true = os.access('models/review.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_is_an_instance(self):
        '''check if my_model is an instance of Review'''
        my_model = Review()
        self.assertIsInstance(my_model, Review)

    def test_str(self):
        '''check if the output of str is in the specified format'''
        my_model4 = Review()
        _dict = my_model4.__dict__
        string1 = "[Review] ({}) {}".format(my_model4.id, _dict)
        string2 = str(my_model4)
        self.assertEqual(string1, string2)

    def test_save(self):
        '''check if the attribute updated_at (date) is updated for
        the same object with the current date'''
        my_model2 = Review()
        first_updated = my_model2.updated_at
        my_model2.save()
        second_updated = my_model2.updated_at
        self.assertNotEqual(first_updated, second_updated)

    def test_to_dict(self):
        '''check if to_dict returns a dictionary, if add a class
        key with class name of the object and if updated_at and
        created_at are converted to string object in ISO format.'''
        my_model3 = Review()
        my_dict_model3 = my_model3.to_dict()
        self.assertIsInstance(my_dict_model3, dict)
        for key, value in my_dict_model3.items():
            flag = 0
            if my_dict_model3['__class__'] == 'Review':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict_model3.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)


class TestBase_Model_documentation(unittest.TestCase):
    """
    Testing the documentation
    """
    def test_module_docstring(self):
        """
        Test if modules have docstring
        """
        obj = models.review.__doc__
        msj = "Module does not has docstring"
        self.assertIsNotNone(obj, msj)  # Classes

    def test_class_docstring(self):
        """
        Test if class have docstring
        """
        obj = models.review.Review.__doc__
        msj = "Class does not has docstring"
        self.assertIsNotNone(obj, msj)  # Classes

    def test_init_docstring(self):
        """
        Test if method has docstring
        """
        obj = models.review.Review.__init__.__doc__
        msj = "Method __init__ does not has docstring"
        self.assertIsNotNone(obj, msj)  # Classes

    def test_str_docstring(self):
        """
        Test if method has docstring
        """
        obj = models.review.Review.__str__.__doc__
        msj = "Method __str__ does not has docstring"
        self.assertIsNotNone(obj, msj)  # Classes

    def test_save_docstring(self):
        """
        Test if method has docstring
        """
        obj = models.review.Review.save.__doc__
        msj = "Method save does not has docstring"
        self.assertIsNotNone(obj, msj)  # Classes

    def test_to_dict_docstring(self):
        """
        Test if method has docstring
        """
        obj = models.review.Review.to_dict.__doc__
        msj = "Method to_dict does not has docstring"
        self.assertIsNotNone(obj, msj)  # Classes

if __name__ == "__main__":
    unittest.main()
