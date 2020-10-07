#!/usr/bin/python3
import json
'''
    module to serialize and object
'''


def save_to_json_file(my_obj, filename):
    '''
    hat writes an Object to a text file,
    using a JSON representation
    '''
    with open(filename, mode='w') as f:
        json.dump(my_obj, f)
