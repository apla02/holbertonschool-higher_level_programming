#!/usr/bin/python3
'''
a new class of base
'''
import json
import csv


class Base:
    '''
        Represent a Base class
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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
            convert a dictionary to JSON string
        '''
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
            JSON string representation
            of list_objs to a file
        '''
        filename = cls.__name__ + ".json"
        lista_dic = []
        if list_objs is None:
            lista_dic = []
        for i in list_objs:
            lista_dic.append(i.to_dictionary())
        with open(filename, mode="w") as f:
            f.write(cls.to_json_string(lista_dic))

    @staticmethod
    def from_json_string(json_string):
        '''
            convert from JSON string to dictionary
        '''
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
            convert from JSON string to dictionary
        '''
        if cls.__name__ is "Rectangle":
            dummy = cls(2, 2)
        if cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''
            returns a list of instances
        '''
        filename = cls.__name__ + ".json"
        list2 = []
        try:
            with open(filename) as f:
                list1 = list(cls.from_json_string(f.read()))
            for i in list1:
                list2.append(cls.create(**i))
        except Exception:
            pass
        return list2

    @classmethod
    def save_to_file_csv(cls, list_objs):
        list1 = []
        filename = cls.__name__ + ".csv"
        with open(filename, newline='') as csvfile:
            write_this = csv.writer(fcsvfile, delimiter=" ")
