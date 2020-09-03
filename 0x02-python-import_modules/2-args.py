#!/usr/bin/python3
import sys
len_arg = len(sys.argv) - 1
if len_arg == 0:
    print("{} arguments.".format(len_arg))
elif len_arg == 1:
    print("{} argument:".format(len_arg))
else:
    print("{} arguments:".format(len_arg))
for i, j in enumerate(sys.argv):
        if i > 0:
            print("{}: {}".format(i, j))
