#!/usr/bin/python3
'''
Module to test the Base Class
'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import inspect


class Test_base(unittest.TestCase):
    '''
        testing base
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

    def test_Id_None(self):
        '''
            Sending id empty
        '''
        b1 = Base()
        self.assertTrue(b1)
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        self.assertEqual(Base._Base__nb_objects, 2)

    def test_Id_Passed(self):
        '''
            test to check id valid
        '''
        b1 = Base(13)
        self.assertEqual(b1.id, 13)
        b2 = Base(-12)
        self.assertEqual(b2.id, -12)
        b3 = Base(3.2)
        self.assertEqual(b3.id, 3.2)
        b4 = Base(0)
        self.assertEqual(b4.id, 0)
        b5 = Base("str")
        self.assertEqual(b5.id, "str")
        b6 = Base([1, 2, 3])
        self.assertEqual(b6.id, [1, 2, 3])



    def test_More_Arguments(self):
        '''
            test to check more argumments passed an Error
        '''
        self.assertRaises(TypeError, self.id, (1, 2))

    if __name__ == '__main__':
        unittest.main()
