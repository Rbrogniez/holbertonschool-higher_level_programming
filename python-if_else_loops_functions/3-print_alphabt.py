#!/usr/bin/python3
for alpha_letters in range(97, 123):
    if chr(alpha_letters) != 'q' and chr(alpha_letters) != 'e':
        print('{}'.format(chr(alpha_letters)), end="")
