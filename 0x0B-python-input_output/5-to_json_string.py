#!/usr/bin/python3
'''
    this module to serialize and object
'''
import json


def to_json_string(my_obj):
    '''
        function converts objects to string
    '''
    return json.dumps(my_obj)
