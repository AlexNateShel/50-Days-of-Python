# Create a function called 'biggest_odd' that takes a string of numbers as an argument and returns the biggest odd number in the string.
# For example, if you pass '23569' as an argument, your function should return 9.
# Use list comprehension.

def biggest_odd(string):
    odd_nums = [i for i in string if int(i) % 2 != 0]
    return f'The biggest odd number is {max(odd_nums)}'

print(biggest_odd('23569'))