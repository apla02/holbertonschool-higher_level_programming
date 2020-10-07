#!/usr/bin/python3
'''
    module to serialize and object
'''
import json


def from_json_string(my_str):
    '''
    function retuconverts string to objects
    represented by a JSON string
    '''
    return json.loads(my_str)
