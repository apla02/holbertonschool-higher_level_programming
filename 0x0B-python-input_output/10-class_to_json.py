#!/usr/bin/python3
'''
    class_to_json fuction
'''
import json

def class_to_json(obj):
    '''
    function that returns the dictionary description
    with simple data structure for JSON serialization of an object
    '''

    return vars(obj)
    #obj.__dic__
