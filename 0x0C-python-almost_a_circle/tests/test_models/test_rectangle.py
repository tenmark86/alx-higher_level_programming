#!/usr/bin/python3
"""
Test for rectangle.py
"""

import unittest

import pycodestyle

from models.base import Base

from models.rectangle import Rectangle


class test_case(unittest.TestCase):
    """Test for rectangle.py"""

    def test_pep8(self):
        """
        Test that checks PEP8
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['models/rectangle.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Pycodestyle errors found in rectangle.py"
        )

    def test_pep8_base(self):
        """
        Test that checks PEP8
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Pycodestyle errors found in test_rectangle.py"
        )

    def setUp(self):
        """def base setup"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """check if call id"""
        res = Rectangle(10, 2)
        self.assertEqual(res.id, 1)

    def test_width_float(self):
        """width is a float"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            Rectangle(4.36, 3, 5, 4)

    def test_width_Nan(self):
        """width is Nan"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            Rectangle(float('NaN'), 7, 4, 8)

    def test_height_NaN(self):
        """height inf"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            Rectangle(1, float('NaN'), 3, 6)

    def test_id2(self):
        """check multipl call id"""
        res = Rectangle(10, 2)
        res2 = Rectangle(2, 4, 0, 0, 12)
        res3 = Rectangle(2, 4)
        self.assertEqual(res3.id, 2)

    def test_complete(self):
        """ check for attributes values"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(10, 2, 4, 5, 24)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 4)
        self.assertEqual(r2.y, 5)

    def test_private_x(self):
        """x is a private attribute"""
        self.assertFalse(hasattr(Rectangle, "__x"))

    def test_private_y(self):
        """y is a private attribute"""
        self.assertFalse(hasattr(Rectangle, "__y"))

    def test_private_height(self):
        """height is private attribute"""
        self.assertFalse(hasattr(Rectangle, "__height"))

    def test_private_widht(self):
        """width is a private attribute"""
        self.assertFalse(hasattr(Rectangle, "__width"))

    def test_errors(self):
        """check differents errors"""
        with self.assertRaises(TypeError) as x:
            r0 = Rectangle(5)
        self.assertEqual(
                "__init__() missing 1 required positional argument: 'height'",
                str(x.exception))
        _str = ("__init__() missing 2 required positional" +
                " arguments: 'width' and 'height'")
        with self.assertRaises(TypeError) as x:
            r1 = Rectangle()
        self.assertEqual(_str, str(x.exception))

    def test_inheritance(self):
        """check for inheritance"""
        r1 = Rectangle(9, 3)
        self.assertTrue(isinstance(r1, Base))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(isinstance(Rectangle, Base))

    def test_attributes(self):
        """check for atributes"""
        with self.assertRaises(TypeError) as x:
            Rectangle(None, 2)
        self.assertEqual("width must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            Rectangle("Hello", 2)
        self.assertEqual("width must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            Rectangle(2, "World")
        self.assertEqual("height must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            Rectangle(1, 2, "Holbie", 3)
        self.assertEqual("x must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            Rectangle(1, 2, 2, "Matias")
        self.assertEqual("y must be an integer", str(x.exception))

        with self.assertRaises(ValueError) as x:
            Rectangle(0, 2)
        self.assertEqual("width must be > 0", str(x.exception))

        with self.assertRaises(ValueError) as x:
            Rectangle(2, 0)
        self.assertEqual("height must be > 0", str(x.exception))

        with self.assertRaises(ValueError) as x:
            Rectangle(2, -3)
        self.assertEqual("height must be > 0", str(x.exception))

        with self.assertRaises(ValueError) as x:
            Rectangle(2, 5, -5, 6)
        self.assertEqual("x must be >= 0", str(x.exception))

    def test_area(self):
        """Check area"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(75, 2)
        self.assertEqual(r2.area(), 150)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(3, 2)
            r1.area("Hello")
        self.assertEqual(
                "area() takes 1 positional argument but 2 were given", str(
                    x.exception))

    def test_update(self):
        """check update"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        r1.update()
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_errors(self):
        """check for update errors"""
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError) as x:
            r1.update("Holbie")
        self.assertEqual("id must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1.update(65, 89, "holbie")
        self.assertEqual("height must be an integer", str(x.exception))

    def test_height_inf(self):
        """height is inf"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            Rectangle(1, float('inf'), 4, 3)

    def test_width_inf(self):
        """width is inf"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            Rectangle(float('inf'), 2, 3, 5)

    def test_update2(self):
        """check update with kwargs"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(r1.height, 1)

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.height, 2)

    def test_update2_errors(self):
        """check for update2 errors"""
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError) as x:
            r1.update(id='Holbie')
        self.assertEqual("id must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1.update(height=65, x=2, width="hola")
        self.assertEqual("width must be an integer", str(x.exception))

    def test_dictionary(self):
        """check for dictionary"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        r_dictionary = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(len(r1_dictionary), len(r_dictionary))
        self.assertEqual(type(r1_dictionary), dict)
