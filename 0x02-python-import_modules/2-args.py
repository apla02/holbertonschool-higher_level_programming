#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len_arg = len(sys.argv) - 1
    if len_arg == 0:
        print("{} argument.".format(len_arg))
    elif len_arg == 1:
        print("{} argument:".format(len_arg))
    else:
        print("{} arguments:".format(len_arg))
    for i, j in enumerate(sys.argv[1:]):
        print("{}: {}".format(i, j))
