# Day 1: Division and Square-root
# Write a function called 'divide_or_square' that takes one argument (a number) and returns the square root of the number if it is divisible by 5, or if its remainder if it is not divisible by 5.
# For example, if you pass 10 as an argument, then your function should return 3.16 as the square root. 

# Without using the math library

def divide_or_square(num):
    if num % 5 == 0:
        sqrt = num ** 0.5
        return f'The square-root of the number is {sqrt:.2f}'
    else:
        rmdr = num % 5
        return f'The remainder of the {num} divided by 5 = {rmdr:.2f}'
    
x = float(input('Enter a numeric value: '))
print(divide_or_square(x))