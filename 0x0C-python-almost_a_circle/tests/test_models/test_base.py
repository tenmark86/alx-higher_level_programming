#!/usr/bin/python3
"""
Test for base.py
"""

import unittest

import pycodestyle

import os

from models.rectangle import Rectangle

from models.square import Square

from models.base import Base


class test_case(unittest.TestCase):
    """holberton"""

    def test_pep8_base(self):
        """
        Test that checks PEP8
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['models/base.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Pycodestyle errors found in base.py"
        )

    def test_pep8_base2(self):
        """
        Test that checks PEP8
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Pycodestyle errors found in test_base.py"
        )

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_list(self):
        """check if id is a list"""
        b1 = Base([1, 2, 3])
        self.assertEqual(b1.id, [1, 2, 3])

    def test_tuple(self):
        """check if id is a tuple"""
        b1 = Base((1, 3, 4))
        self.assertEqual(b1.id, (1, 3, 4))

    def test_NaN(self):
        """check if id is NaN"""
        b1 = Base(float('NaN'))
        self.assertNotEqual(b1.id, float('NaN'))

    def test_twoargs(self):
        """check if id have 2 args"""
        with self.assertRaises(TypeError):
            Base(1, 4)

    def test_dict(self):
        """"check if id is dictionary"""
        b1 = Base({"Holbie": 11, "school": 24})
        self.assertEqual(b1.id, {"Holbie": 11, "school": 24})

    def test_base(self):
        """
        check if base id no args
        """
        b1 = Base(None)
        self.assertEqual(b1.id, 1)

    def test_docum(self):
        """test for documentation"""
        self.assertTrue(len(Base.__doc__) > 0)

    def test_baseNone(self):
        """
        check if base id is None
        """
        Base._Base__nb_objects = 0
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b1 = Base(None)
        self.assertEqual(b1.id, 2)

    def test_base_12(self):
        """
        check if base id with 1 arg
        """
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_doble_base(self):
        """pased two vvalores"""
        b1 = Base(13)
        self.assertEqual(b1.id, 13)
        b1 = Base(42)
        self.assertEqual(b1.id, 42)

    def test_id_inc(self):
        """
        check if base id increment
        """
        Base._Base__nb_objects = 0
        b1 = Base()
        b1 = Base()
        self.assertEqual(b1.id, 2)

    def test_id_inc2(self):
        """
        check if base id increment
        """
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b3.id, 2)

    def test_id_neg(self):
        """
        check base id negaative
        """
        b1 = Base(-1)
        self.assertEqual(b1.id, -1)

    def test_id_str(self):
        """
        check base id str
        """
        b1 = Base("hola")
        self.assertEqual(b1.id, "hola")

    def test_id_float(self):
        """
        check base id float
        """
        b1 = Base(1.0)
        self.assertEqual(b1.id, 1.0)

    def test_id_bool(self):
        """
        check base id bool
        """
        b1 = Base(True)
        self.assertEqual(b1.id, True)

    def test_to_json_string(self):
        """
        Test for to_json_string
        """
        rect_instance = Rectangle(10, 7, 2, 8, 70)
        rect_data = re1.to_dictionary()
        json_data = Base.to_json_string([rect_data])
        self.assertEqual(type(json_data), str)

    def test_empty_to_json_string(self):
        """
        Test for a empty to_json_string
        """
        empty_data = []
        json_data = Base.to_json_string(empty_data)
        self.assertEqual(json_data, "[]")

        empty_data = None
        json_data = Base.to_json_string(empty_data)
        self.assertEqual(json_data, "[]")

    def test_instance(self):
        """
        Test a Base Class instance
        """
        base_instance = Base()
        self.assertEqual(type(base_instance), Base)
        self.assertTrue(isinstance(base_instance, Base))

    def test_to_json_string(self):
        """
        Test a normal to_json_string functionality
        """
        rect_data = {'id': 31, 'x': 14, 'y': 11, 'width': 3, 'height': 3}
        json_data = Base.to_json_string([rect_data])

        self.assertTrue(isinstance(rect_data, dict))
        self.assertTrue(isinstance(json_data, str))
        self.assertCountEqual(
            json_data,
            '{["id": 31, "x": 14, "y": 11, "width": 3, "height": 3]}'
        )

    def test_to_json_string_error(self):
        """
        Test for to_json_string error
        """
        json_data = Base.to_json_string(None)
        self.assertEqual(json_data, "[]")

        warn = ("to_json_string() missing 1 required positional argument: " +
                "'list_dictionaries'")

        with self.assertRaises(TypeError) as msg:
            Base.to_json_string()

        self.assertEqual(warn, str(msg.exception))

        warn = "to_json_string() takes 1 positional argument but 2 were given"

        with self.assertRaises(TypeError) as msg:
            Base.to_json_string([{43, 87}], [{22, 17}])

        self.assertEqual(warn, str(msg.exception))

    def test_save_to_file(self):
        """
        Test for save_to_file
        """
        with self.assertRaises(AttributeError) as msg:
            Base.save_to_file([Base(1), Base(2)])

        self.assertEqual(
             "'Base' object has no attribute 'to_dictionary'",
             str(msg.exception)
        )

    def test_load_from_file(self):
        """
        Test for load_from_file
        """
        if os.path.exists("Base.json"):
            os.remove("Base.json")

        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        if os.path.exists("Square.json"):
            os.remove("Square.json")

        rect_output = Rectangle.load_from_file()
        self.assertEqual(rect_output, [])

        square_output = Square.load_from_file()
        self.assertEqual(square_output, [])

        warn = "load_from_file() takes 1 positional argument but 2 were given"

        with self.assertRaises(TypeError) as msg:
            Rectangle.load_from_file('Monty Python')

        self.assertEqual(warn, str(msg.exception))
