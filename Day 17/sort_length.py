names = ["Peter", "Jon", "Andrew"]

# Write a function called 'sort_length' that takes a list of strings as an argument and sorts the strings in ascending order according to their length.
# For example, the list above should return:
# ['Jon', 'Peter', 'Andrew']
# Do not use the built in sort functions.

def sort_length(lst:list):
    for word in range(len(lst)):
        for x in range(len(lst) - 1):
            if len(lst[x]) > len(lst[x + 1]):
                lst[x], lst[x + 1] = lst[x + 1], lst[x]
    return lst

print(sort_length(names))