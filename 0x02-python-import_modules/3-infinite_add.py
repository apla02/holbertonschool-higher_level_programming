#!/usr/bin/python3
import sys
suma = 0
for i, j in enumerate(sys.argv[1:]):
    suma += int(j)
    if i == len(sys.argv) - 2:
        print("{}".format(suma))
