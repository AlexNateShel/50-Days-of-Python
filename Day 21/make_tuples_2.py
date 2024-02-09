# Write a function called 'make_tuples' that takes two equal lists and combines them into a list of tuples.
# Your code should check that the input lists are of the same length.
# For example, if 'list a' is [1, 2, 3, 4] and 'list b' is [5, 6, 7, 8], your function should return [(1.5), (2, 6), (3, 7), (4, 8)].
# If the lists are not of equal length, your function should raise a ValueError.

def make_tuples(a, b):
    if len(a) != len(b):
        raise ValueError('Your lists are not of equal length.')
    
    tuple_list = []
    for i in range(len(a)):
        tuple_list.append((a[i], b[i]))
    return tuple_list

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
print(make_tuples(list1, list2))