#!/usr/bin/python3
'''
    Module to test the Base Class
'''
import unittest
from models.base import Base
from models.rectangle import Rectangle, __doc__
from models.square import Square
import inspect
import pep8


class Test_Rectangle_Class(unittest.TestCase):
    '''
        test to check the Rectangle Class
    '''
    def test_documentation(self):
        '''
        checking the documantation
        '''
        self.assertTrue(len(__doc__.strip()) > 0)
        self.assertTrue(len(Base.__doc__.strip()) > 0)
        functions = inspect.getmembers(Base, predicate=inspect.ismethod)
        for name, func in functions:
            self.assertTrue(len(func.__doc__.strip()) > 0)
        functions = inspect.getmembers(Base, predicate=inspect.isfunction)
        for name, func in functions:
            self.assertTrue(len(func.__doc__.strip()) > 0)

    def test_Rectangle_valid(self):
        '''
            test to check id no passed, and weight y height passed
        '''
        r1 = Rectangle(10, 2)
        self.assertEqual(10, r1.width)
        self.assertEqual(2, r1.height)
        self.assertEqual(0, r1.x)
        self.assertEqual(0, r1.y)
        self.assertEqual(3, r1.id)

    def test_pep8(self):
        """
        Test for PEP-8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/rectangle.py"])
        self.assertEqual(result.total_errors, 0)

    def test_Rectangle_Arguments_And_Id(self):
        '''
            test to check id string , weight, and height passed
        '''
        r1 = Rectangle(10, 2, 0, 0, "str")
        self.assertEqual("str", r1.id)

    def test_Rectangle_Wrong_Width(self):
        '''
            test to check id string , weight, and height passed
        '''
        self.assertRaises(TypeError, self.id, ("str", 2, -1, 0))

    def test_Rectangle_Wrong_attr(self):
        '''
            test to check id string , weight, and height passed
        '''
        self.assertRaises(TypeError, self.id, (2, "str", 0, 0))
        self.assertRaises(TypeError, self.id, (-2, 2, 0, 0))
        self.assertRaises(TypeError, self.id, (0, 1, -1, 0))

    def test_Rectangle_More_Args(self):
        '''
            test more arguments
        '''
        self.assertRaises(TypeError, self.id, (2, 1, "str", 0, (2, 2), 5))

if __name__ == '__main__':
    unittest.main()
