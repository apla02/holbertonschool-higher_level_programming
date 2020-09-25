#!/usr/bin/python3
"""indenttion  of a string


"""


def text_indentation(text):
    """indent a string

    Args:
        text (str): a string

    Raises:
        TypeError: must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace('. ', '.\n\n')
    text = text.replace('? ', '?\n\n')
    text = text.replace(': ', ':\n\n')
    print(text, end='')
