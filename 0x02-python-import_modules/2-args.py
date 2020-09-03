#!/usr/bin/python3
import sys
if __name__ == "__main__":
    len_arg = len(sys.argv) - 1
    if len_arg == 0:
        print("{} arguments.".format(len_arg))
    elif len_arg == 1:
        print("{} argument:".format(len_arg))
    else:
        print("{} arguments:".format(len_arg))
    for i, j in enumerate(sys.argv):
        if i >= 1:
            print("{}: {}".format(i, j))
