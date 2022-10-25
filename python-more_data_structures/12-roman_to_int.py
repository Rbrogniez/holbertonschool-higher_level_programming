#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    letter = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for x in range(len(roman_string)):
        if x < (len(roman_string)) - 1 \
             and letter[roman_string[x]] < letter[roman_string[x + 1]]:
            result -= letter[roman_string[x]]
        else:
            result += letter[roman_string[x]]
    return result
