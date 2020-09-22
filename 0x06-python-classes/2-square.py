#!/usr/bin/python3
class Square():
    '''
    This class represents a Square.
    '''
    def __init__(self, size=0):
        '''
        Initialization of objects

        Args:
            size(int): size of square, must be integer and greater than zero
        '''

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size