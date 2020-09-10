#!/usr/bin/python3
def uniq_add(my_list=[]):
    adds = 0
    my_list = [1, 2, 3, 1, 4, 2, 5]
    for i in set(my_list):
        adds += i
    return(adds)
