#!/usr/bin/python3
import json
'''
    module to serialize and object
'''


def from_json_string(my_str):
    '''
    function retuconverts string to objects
    represented by a JSON string
    '''
    return json.loads(my_str)
