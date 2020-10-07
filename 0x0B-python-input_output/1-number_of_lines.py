#!/usr/bin/python3
'''
    function to handle open and read files
'''


def number_of_lines(filename=""):
    '''
    function to count lines in a file
    '''

    with open(filename, encoding='utf-8') as f:
        count = 0
        for line in f:
            count += 1
        return count
