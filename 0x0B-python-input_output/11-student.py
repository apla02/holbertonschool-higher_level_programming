#!/usr/bin/python3
'''
    class of Student
'''


class Student:
    '''
    represents a Student class
    '''

    def __init__(self, first_name, last_name, age):
        '''
        instantiation of attributes of instance
        args:
            name
            last_name
            age
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''
        method
        '''
        return self.__dict__
