# Day 1: Division and Square-root
# Write a function called 'divide_or_square' that takes one argument (a number) and returns the square root of the number if it is divisible by 5, or if its remainder if it is not divisible by 5.
# For example, if you pass 10 as an argument, then your function should return 3.16 as the square root. 


import math

def divide_or_square(x):
    if x % 5 == 0:
        return math.sqrt(x)
    else:
        remainder = x % 5
        return remainder


var = int(input('Enter a number: '))
print(divide_or_square(var))