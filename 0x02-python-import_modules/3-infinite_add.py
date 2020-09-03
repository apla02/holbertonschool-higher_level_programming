#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    suma = 0
    for j in sys.argv[1:]:
        suma += int(j)
    print("{}".format(suma))
