#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import(add, sub, mul, div)
    for i, j in enumerate(sys.argv[:4]):
        if len(sys.argv) == 4:
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            if i == 2 and j == '+':
                print("{} + {} = {}".format(a, b, add(a, b)))
                exit(0)
            elif i == 2 and j == '-':
                print("{} - {} = {}".format(a, b, sub(a, b)))
                exit(0)
            elif i == 2 and j == "*":
                print("{} * {} = {}".format(a, b, mul(a, b)))
                exit(0)
            elif i == 2 and j == '/':
                print("{} / {} = {}".format(a, b, div(a, b)))
                exit(0)
            elif i == 2 and j != ('+', '-', '*', '/'):
                print('Unknown operator. Available operators: +, -, * and /')
                exit(1)
        else:
            print('Usage: ./100-my_calculator.py <a> <operator> <b>')
            exit(1)
