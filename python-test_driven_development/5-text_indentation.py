#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")

    x = text.replace('.','.\n \n').replace('?', '?\n \n').replace(':', ':\n \n')
    print(x)


