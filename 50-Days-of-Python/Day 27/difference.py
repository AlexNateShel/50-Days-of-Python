# Write a function called 'difference' that takes two lists as arguments. 
# This function should return all the elements that are in list a, but not in list b and all the elements in list b but not in list a.
# For example:

list1 = [1, 2, 4, 5, 6]
list2 = [1, 2, 5, 7, 9]

# Should return: [4, 6, 7, 9]
# Use list comprehension in your function.

def difference(arg1: list, arg2: list):
    list1 = [i for i in arg1 if i not in arg2]
    list2 = [j for j in arg2 if j not in arg1]
    return 'The difference between the two sets is ', list1 + list2

print(difference(list1, list2))
