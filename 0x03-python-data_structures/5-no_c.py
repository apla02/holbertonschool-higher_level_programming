#!/usr/bin/python3
def no_c(my_string):
    str = ""
    for i in my_string:
        if i == "C" or i == "c":
            str += ""
        else:
            str += i
    return(str)
