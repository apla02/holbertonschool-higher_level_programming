#!/usr/bin/python3
"""[summary]
"""


def text_indentation(text):
    """indentation a string

    Args:
        text (str): [string]
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    text = text.replace(". ", ".")
    text = text.replace("? ", "?")
    text = text.replace(": ", ":")
    text = text.replace(".", ".\n\n")
    text = text.replace("?", "?\n\n")
    text = text.replace(":", ":\n\n")
    print(text, end="")
