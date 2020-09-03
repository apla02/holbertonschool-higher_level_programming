#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    suma = 0
    for i, j in enumerate(sys.argv[1:]):
        suma += int(j)
        if i == len(sys.argv) - 2:
            print("{}".format(suma))
