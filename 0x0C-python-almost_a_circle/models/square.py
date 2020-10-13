#!/usr/bin/python3
'''
    A new class of Square
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
        Class Square inherits from Rectangle
        Args:
            inherits from Rectangle: id, width, height, x, y
            width and height : size
    '''
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''
            return the value of attribute
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''
            set the value of the attribute size
        '''
        self.width = value
        self.height = value

    def __str__(self):
        '''
            method to return the string representation of class Square
        '''
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        '''
            method to update a Square
        '''
        if kwargs is not None and len(args) == 0:
            for key, value in kwargs.items():
                if key in ["id", "size", "x", "y"]:
                    setattr(self, key, value)
        elif args is not None:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass

    def to_dictionary(self):
        '''
            return a dictionary representation of a Square
        '''
        dic = dict(zip(["id", "size", "x", "y"], [
            self.id, self.size, self.x, self.y]))
        return dic
