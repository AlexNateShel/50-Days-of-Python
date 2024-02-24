# Write a function called 'odd_even' that has one parameter and takes a list of numbers as an argument.
# The function returns the difference between the largest even number in the list and the smallest odd number in the list.
# For example, if you pass [1, 2, 3, 4, 6] as an argument, the function should return 6 - 1 = 5.

def odd_even(arg: list):
    even = []
    odd = []
    for num in arg:
        if num % 2 == 0:
            even.append(num)
        if num % 2 != 0:
            odd.append(num)
    return max(even) - min(odd)

x = [1, 2, 3, 4, 6]
print(odd_even(x))