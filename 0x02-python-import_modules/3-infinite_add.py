#!/usr/bin/python3
import sys
if __name__ == "__main__":
    suma = 0
    for j in sys.argv[1:]:
        suma += int(j)
    print("{}".format(suma))
