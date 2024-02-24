# You work for a local school in your area. 
# The school has a list of names of students saved in a list format.
# The school has asked you to write a program that takes a list of names and sorts them alphabetically.
# The names should be sorted by last name.
# Here is a list of names:

names = ['Beyonce Knowles', 'Alicia Keys', 'Katie Perry', 'Chris Brown', 'Tom Cruise']

# Your code should not just sort them alphabetically; it should also switch the names (the last must be first).
# Here is how your code output should look:
# ['Brown Chris', 'Cruise Tom', 'Keys Alicia', 'Perry Katie', 'Knowles Beyonce']
# Write a function called 'sorted_names'.

def sorted_name(names: list):
    list2 = []

    for i in names:
        list2.append(i.split())
    
    list3 = []
    x = lambda x: x[-1]
    for j in sorted(list2, key=x):
        list3.append(' '.join([j[-1], j[0]]))
    return list3

print(sorted_name(names))