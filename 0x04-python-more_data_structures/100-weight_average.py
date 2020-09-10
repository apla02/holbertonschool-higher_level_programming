#!/usr/bin/python3
def weight_average(my_list=[]):
    score, average, result = 0, 0, 0
    if my_list:
        for i, j in my_list:
            score += i * j
            average += j
        result = score / average
    return result
