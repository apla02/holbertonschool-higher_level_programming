#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    lastdigit = number % 10
elif number < 0:
    lastdigit = number % -10

ld = "Last digit of"
less = "and is less than 6 and not 0"

if lastdigit > 5:
    print('{} {} is {} and is greater than 5'.format(ld, number, lastdigit))
elif lastdigit == 0:
    print('{} {} is {} and is 0'.format(ld, number, lastdigit))
elif lastdigit < 6 and not 0:
    print('{} {} is {} {}'.format(ld, number, lastdigit, less))
