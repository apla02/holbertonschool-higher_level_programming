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
            name: name of stdudent
            last_name: last name of student
            age: age of student
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        method to retrieves the dictionary repr of a class
        '''
        dictionar = {}
        if type(attrs) is list:
            for i in attrs:
                if type(i) is str and i in self.__dict__.keys():
                    dictionar[i] = self.__dict__[i]
            return dictionar
        else:
            return self.__dict__
