#!/usr/bin/python3
"""
Test for square.py
"""


from models.base import Base

from models.rectangle import Rectangle

from models.square import Square

import unittest

import pycodestyle


class TestSquare(unittest.TestCase):
    """test for square"""

    def test_pep8_scuare(self):
        """
        Test that checks PEP8 in square
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['models/square.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Pycodestyle errors found in square.py"
        )

    def test_pep8_test_scuare(self):
        """
        Test that checks PEP8 in test_square
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Pycodestyle errors found in test_square.py"
        )

    def test_size(self):
        """size of square"""
        Base._Base__nb_objects = 0
        r1 = Square(3)
        self.assertEqual(r1.size, 3)

    def test_size_0(self):
        """size is zero"""
        with self.assertRaises(ValueError) as x:
            r1 = Square(0)
        self.assertEqual(str(x.exception), "width must be > 0")

    def test_getter(self):
        r1 = Square(5)
        self.assertEqual(r1.size, 5)

    def test_setter(self):
        r1 = Square(5)
        r1.size = 8
        self.assertEqual(r1.size, 8)

    def test_string(self):
        r1 = Square(3)

        with self.assertRaises(TypeError):
            r1.size = "Hi"

    def test_negative(self):
        r1 = Square(6)

        with self.assertRaises(ValueError):
            r1.size = -5

    def test_zero(self):
        r1 = Square(6)

        with self.assertRaises(ValueError):
            r1.size = 0

    def test_decimal(self):
        r1 = Square(6)

        with self.assertRaises(TypeError):
            r1.size = 1.5

    def test_tuple(self):
        r1 = Square(7)

        with self.assertRaises(TypeError):
            r1.size = (2, 8)

    def test_empty(self):
        r1 = Square(7)

        with self.assertRaises(TypeError):
            r1.size = ''

    def test_none(self):
        r1 = Square(5)

        with self.assertRaises(TypeError):
            r1.size = None

    def test_list(self):
        r1 = Square(4)

        with self.assertRaises(TypeError):
            r1.size = [4, 7]

    def test_dict(self):
        r1 = Square(5)

        with self.assertRaises(TypeError):
            r1.size = {"hi": 5, "world": 8}

    def test_width(self):
        r1 = Square(5)
        r1.size = 6
        self.assertEqual(r1.width, 6)
        self.assertEqual(r1.height, 6)

    def test_to_dictionary(self):
        Base._Base__nb_objects = 0

        s1 = Square(10, 2, 1, 9)
        s1_dictionary = s1.to_dictionary()
        expected = {'id': 9, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s1_dictionary, expected)

        s1 = Square(1, 0, 0, 9)
        s1_dictionary = s1.to_dictionary()
        expected = {'id': 9, 'x': 0, 'size': 1, 'y': 0}
        self.assertEqual(s1_dictionary, expected)

        s1.update(5, 5, 5, 5)
        s1_dictionary = s1.to_dictionary()
        expected = {'id': 5, 'x': 5, 'size': 5, 'y': 5}
        self.assertEqual(s1_dictionary, expected)
