#!/usr/bin/python3
import json
'''
    module to serialize and object
'''


def load_from_json_file(filename):
    '''
    function that creates an Object
    from a “JSON file”:
    '''
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
