#!/usr/bin/python3
"""
This is text_indentation module
"""


def text_indentation(text):
    """
    Prints text with added two newlines
    after each of these characters {'.', '?', ':'}.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    x = text.replace('.','.\n \n').replace('?', '?\n \n').replace(':', ':\n \n')
    print(x)


