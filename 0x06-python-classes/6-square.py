#!/usr/bin/python3
"""
Define a class Square
"""


class Square():
    '''
    This class represents a Square.
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''Initialization of objects

        Args:
            size(int): size of square, must be integer and greater than zero
            position(tuple): cordinates of the squeare
        '''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''property  to retrieve it'''
        return self.__size

    @size.setter
    def size(self, value):
        ''' property  setter to set it

            Args:
            value : must be an integer and greater than zero"
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        ''' property  to retrieve it '''
        return self.__position

    @position.setter
    def position(self, value):
        ''' property  setter to set it

            Args:
            value : must be an integer and greater than zero"
        '''
        if type(value) is tuple and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1]>= 0:
                    self.__position = position
        raise TypeError("position must be a tuple of 2 positive integers")


    def area(self):
        '''
            define a method to get an area of square class
        '''
        return self.__size ** 2

    def my_print(self):
        '''
            Print a square from stdout
            if size is zero print a new line
        '''
        if self.__size == 0:
            print("")
        for line in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print("{}{}".format((self.__position[0]* " "), ("#" * self.__size)))
