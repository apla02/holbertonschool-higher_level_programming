#!/usr/bin/python3
'''
    function to handle open and read files
'''


def append_write(filename="", text=""):
    '''
    function to write and overwrite a text in a file
    '''

    with open(filename, mode="a", encoding='utf-8') as f:

        return f.write(text)
