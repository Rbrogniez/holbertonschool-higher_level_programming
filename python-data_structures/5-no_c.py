#!/usr/bin/env python3

def no_c(my_string):
    result = ''
    for i in my_string:
        if i == 'C' or i == 'c':
                i = ''
        result +=i

    return (result)
