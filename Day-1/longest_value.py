# Extra Challenge: Longest Value
# Write a function called 'longest_value' that takes a dictionary as an argument and returns the first longest value of the dictionary.
# For example, the following dictionary should return "apple" as the longest value.
# fruits = {'fruit': 'apple', 'color': 'green'}


def longest_value(d: dict):
    longest = max(d.values(), key=len)
    return longest


fruits = {'fruit': 'apple', 'color': 'green'}
print(longest_value(fruits))
