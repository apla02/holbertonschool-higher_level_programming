#!/usr/bin/python3
'''
    Module to test the Base Class
'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Rectangle_Class(unittest.TestCase):
    '''
        test to check the Rectangle Class
    '''
    def test_Rectangle_Id_Nopassed(self):
        '''
            test to check id no passed, and weight y height passed
        '''
        r1 = Rectangle(10, 2)
        self.assertEqual(3, r1.id)

    def test_Rectangle_Arguments_And_Id(self):
        '''
            test to check id, weight, and height passed
        '''
        r1 = Rectangle(10, 2, 5)
        self.assertEqual(5, r1.id)

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
