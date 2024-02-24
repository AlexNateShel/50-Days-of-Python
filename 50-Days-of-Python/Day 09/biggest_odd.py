# Create a function called 'biggest_odd' that takes a string of numbers as an argument and returns the biggest odd number in the string.
# For example, if you pass '23569' as an argument, your function should return 9.
# Use list comprehension.

def biggest_odd(string):
    odd = []
    for i in string:
        i = int(i)
        if i % 2 != 0:
            odd.append(i)
    return max(odd)


print(biggest_odd('23569'))