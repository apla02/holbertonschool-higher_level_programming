#!/usr/bin/python3
'''
a new class of base
'''


class Base:
    '''
        Respresent a Base class
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        instantiation of new instance
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
