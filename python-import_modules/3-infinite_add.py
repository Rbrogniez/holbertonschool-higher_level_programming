#!/usr/bin/python3
from sys import argv as av


if __name__ == "__main__":
    ar = len(av) - 1
    result = 0

    if ar > 1:
        for i in range(ar):
            result += int(av[i + 1])
        print(result)
    else:
        print(0)
