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

    text = text.replace('.', '.\n \n')
    text = text.replace('?', '?\n \n')
    text = text.replace(':', ':\n \n')

    print("\n".join([line.strip() for line in text.split("\n")]), end="")
