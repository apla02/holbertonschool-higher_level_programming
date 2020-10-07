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
        dictionary = {}
        if type(attrs) == list:
            for i in attrs:
                if type(i) is str and i in self.__dict__.keys():
                    dictionary[i] = self.__dict__[i]
                    return dictionary
        return self.__dict__

    def reload_from_json(self, json):
        '''
        method to replace the atributtes in jason dictionary
        '''
        for key, value in json.items():
            self.__dict__[key] = value
