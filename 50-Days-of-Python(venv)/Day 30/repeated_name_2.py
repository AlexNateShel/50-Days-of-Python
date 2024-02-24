# Write a function called 'repeated name' that finds the most repeated name in the following list.
# Your function should return a tuple of the name and how many times it appears. 
# The list below should return: ("Peter", 3)

from collections import Counter

names = ['John', 'Peter', 'John', 'Peter', 'Jones', 'Peter']

def repeated_name(names):
    return max(Counter(names).most_common(1))

print(repeated_name(names))