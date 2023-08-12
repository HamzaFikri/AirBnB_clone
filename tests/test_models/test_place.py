#!/usr/bin/python3
"""
Tests for module of Place class
"""
import os
import unittest
import datetime
import models
import models.place
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Testing the class.
    """
    def test_instance_no_arg(self):
        msj = "Bad id for Place without args"
        my_model1 = Place()
        self.assertIsNotNone(my_model1.id, msj)

    def test_instance_arg(self):
        msj = "Bad id for Place with args"
        my_model_json = {'id': 'd2f054ed-7125-4417-8416-aea973791d04',
                         'my_number': 89, 'name': 'AlxHolberton',
                         'created_at': datetime.datetime(2020, 2, 19, 19,
                                                         14, 55, 659675),
                         'updated_at': datetime.datetime(2020, 2, 19, 19,
                                                         14, 55, 659675)}
        my_model1 = Place(**my_model_json)
        self.assertIsNotNone(my_model1.id, msj)

    def test_no_arg_random(self):
        msj = "Id Place no random for created Place"
        my_model1 = Place()
        my_model2 = Place()
        self.assertNotEqual(my_model1.id, my_model2.id, msj)

    def test_no_arg_timestamp(self):
        msj = "Date Place bad timestamp"
        my_model1 = Place()
        self.assertEqual(my_model1.created_at, my_model1.updated_at, msj)

    def test_id_public(self):
        msj = "Id isn't public"
        my_model1 = Place()
        my_model1.id = "HELLO"
        self.assertEqual(my_model1.id, "HELLO")

    def test_user_id_public(self):
        msj = "User_id isn't public"
        my_model1 = Place()
        my_model1.user_id = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        self.assertEqual(my_model1.user_id, "b6a6e15c-c67d-4312-9a75-9d084935e579")

    def test_city_id_public(self):
        msj = "City_id isn't public"
        my_model1 = Place()
        my_model1.city_id = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        self.assertEqual(my_model1.city_id, "b6a6e15c-c67d-4312-9a75-9d084935e579")

    def test_name_public(self):
        msj = "Name isn't public"
        my_model1 = Place()
        my_model1.name = "AlxHolberton"
        self.assertEqual(my_model1.name, "AlxHolberton")

    def test_description_public(self):
        msj = "Description isn't public"
        my_model1 = Place()
        my_model1.description = "AlxHolberton Campus"
        self.assertEqual(my_model1.description, "AlxHolberton Campus")

    def test_number_rooms_public(self):
        msj = "Number of rooms isn't public"
        my_model1 = Place()
        my_model1.number_rooms = 33
        self.assertEqual(my_model1.number_rooms, 33)

    def test_number_bathrooms_public(self):
        msj = "Number of bathrooms isn't public"
        my_model1 = Place()
        my_model1.number_bathrooms = 2
        self.assertEqual(my_model1.number_bathrooms, 2)

    def test_max_guest_public(self):
        msj = "Max of guests isn't public"
        my_model1 = Place()
        my_model1.max_guest = 1
        self.assertEqual(my_model1.max_guest, 1)

    def test_price_by_night_public(self):
        msj = "Price by night isn't public"
        my_model1 = Place()
        my_model1.price_by_night = 50
        self.assertEqual(my_model1.price_by_night, 50)

    def test_latitude_public(self):
        msj = "Latitude isn't public"
        my_model1 = Place()
        my_model1.latitude = 10
        self.assertEqual(my_model1.latitude, 10)

    def test_longitude_public(self):
        msj = "Longitude isn't public"
        my_model1 = Place()
        my_model1.longitude = -76
        self.assertEqual(my_model1.longitude, -76)

    def test_amenity_ids_public(self):
        msj = "Longitude isn't public"
        my_model1 = Place()
        my_model1.amenity_ids = [ "b6a6e15c-c67d-4312-9a75-9d084935e579" ]
        self.assertEqual(my_model1.amenity_ids, [ "b6a6e15c-c67d-4312-9a75-9d084935e579" ])

    def test_id(self):
        '''test if the id of two instances are different'''
        my_model = Place()
        my_model1 = Place()
        self.assertNotEqual(my_model.id, my_model1.id)

    def test_executable_file(self):
        '''test if file has permissions u+x to execute'''
        # Check for read access
        is_read_true = os.access('models/place.py', os.R_OK)
        self.assertTrue(is_read_true)
        # Check for write access
        is_write_true = os.access('models/place.py', os.W_OK)
        self.assertTrue(is_write_true)
        # Check for execution access
        is_exec_true = os.access('models/place.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_is_an_instance(self):
        '''check if my_model is an instance of Place'''
        my_model = Place()
        self.assertIsInstance(my_model, Place)

    def test_str(self):
        '''check if the output of str is in the specified format'''
        my_model4 = Place()
        _dict = my_model4.__dict__
        string1 = "[Place] ({}) {}".format(my_model4.id, _dict)
        string2 = str(my_model4)
        self.assertEqual(string1, string2)

    def test_save(self):
        '''check if the attribute updated_at (date) is updated for
        the same object with the current date'''
        my_model2 = Place()
        first_updated = my_model2.updated_at
        my_model2.save()
        second_updated = my_model2.updated_at
        self.assertNotEqual(first_updated, second_updated)

    def test_to_dict(self):
        '''check if to_dict returns a dictionary, if add a class
        key with class name of the object and if updated_at and
        created_at are converted to string object in ISO format.'''
        my_model3 = Place()
        my_dict_model3 = my_model3.to_dict()
        self.assertIsInstance(my_dict_model3, dict)
        for key, value in my_dict_model3.items():
            flag = 0
            if my_dict_model3['__class__'] == 'Place':
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
        obj = models.place.__doc__
        msj = "Module does not has docstring"
        self.assertIsNotNone(obj, msj)  # Classes

    def test_class_docstring(self):
        """
        Test if class have docstring
        """
        obj = models.place.Place.__doc__
        msj = "Class does not has docstring"
        self.assertIsNotNone(obj, msj)  # Classes

    def test_init_docstring(self):
        """
        Test if method has docstring
        """
        obj = models.place.Place.__init__.__doc__
        msj = "Method __init__ does not has docstring"
        self.assertIsNotNone(obj, msj)  # Classes

    def test_str_docstring(self):
        """
        Test if method has docstring
        """
        obj = models.place.Place.__str__.__doc__
        msj = "Method __str__ does not has docstring"
        self.assertIsNotNone(obj, msj)  # Classes

    def test_save_docstring(self):
        """
        Test if method has docstring
        """
        obj = models.place.Place.save.__doc__
        msj = "Method save does not has docstring"
        self.assertIsNotNone(obj, msj)  # Classes

    def test_to_dict_docstring(self):
        """
        Test if method has docstring
        """
        obj = models.place.Place.to_dict.__doc__
        msj = "Method to_dict does not has docstring"
        self.assertIsNotNone(obj, msj)  # Classes

if __name__ == "__main__":
    unittest.main()
