#!/usr/bin/python3
'''
    function to handle open and read files
'''


def write_file(filename="", text=""):
    '''
    function to write a text in a file
    '''

    with open(filename, mode="w", encoding='utf-8') as f:

        return f.write(text)
