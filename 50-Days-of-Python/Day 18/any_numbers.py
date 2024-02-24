# Write a function called 'any_numbers' that can receive any number of positional arguments (integers and floats) and return the average of those integers.
# If you pass 12, 90, 12, and 34 as arguments, your function should return 37.0 as the average. 
# If you pass 12 and 90, your function should return 51.0 as the average.

def any_numbers(*args):
    average = sum(args) / len(args)
    return f' The average of {args} is {average}.'

print(any_numbers(12, 90, 12, 34))
print(any_numbers(12, 90))
