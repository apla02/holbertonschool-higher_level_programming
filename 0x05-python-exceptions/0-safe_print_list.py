#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        num = 0
        for i, j in enumerate(my_list):
            if i < x:
                print(j, end="")
                num += 1
        print()
        return num
    except IndexError:
        return num
