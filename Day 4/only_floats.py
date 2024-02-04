# Write a function called 'only_floats', which has two parameters, a and b, and returns 2 if both arguments are floats, 1 if only one argument is a float, and 0 if neither argument is a float.
# If you pass (12.1, 23) as an argument, your function should return 1.

def only_floats(num1, num2):
    if type(num1) == float and type(num2) == float:
        return 2
    elif type(num1) == float or type(num2) == float:
        return 1
    else:
        return 0
    
print(only_floats(12.1, 23))
