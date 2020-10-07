#!/usr/bin/python3
'''
    function to handle open and read files
'''


def read_lines(filename="", nb_lines=0):
    '''
    function to read exactly n lines in a file
    '''
    total_lines = number_of_lines(filename)

    with open(filename, encoding='utf-8') as f:

        if nb_lines <= 0 or nb_lines >= total_lines:
            print(f.read(), end="")

        for i in range(nb_lines):
            print(f.readline(), end="")


def number_of_lines(filename=""):
    '''
    function to count lines in a file
    '''

    with open(filename, encoding='utf-8') as f:
        count = 0
        for line in f:
            count += 1
        return count
