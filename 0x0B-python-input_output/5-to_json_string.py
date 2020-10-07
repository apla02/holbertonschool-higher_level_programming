#!/usr/bin/python3
import json
'''
    this module to serialize and object
'''


def to_json_string(my_obj):
    '''
        function converts objects to string
    '''
    return json.dumps(my_obj)
