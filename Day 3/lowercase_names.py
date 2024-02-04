# You are given a list of names below. 
# This list is made up of names with lowercase and uppercase letter.
# Your task is to write a code that will return a tuple of all the names in the list that only have lowercase letters.
# Your tuple should have names sorted alphabetically in descending order. 
# Using the list below, your code should return ('kerry', 'dickson', 'carol', 'adam')

names = ['kerry', 'dickson', 'John', 'Mary', 'carol', 'Rose', 'adam']

lowercase = []
for name in sorted(names, reverse=True):
    if name.islower():
        lowercase.append(name)
        tuple_names = tuple(lowercase)

print(tuple_names)
