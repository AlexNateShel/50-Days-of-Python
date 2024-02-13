# Write a function called 'inter_section' that takes two lists and finds the intersection (the elements that are present in both lists).
# The function should return a tuple of intersections with the number at index 0 switched with the number at index -1.
# Use list comprehension in your solution.
# Use the lists below. 
# Your function should return: (80, 65, 30).

list1 = [20, 30, 60, 65, 75, 80, 85]
list2 = [42, 30, 80, 65, 88, 95]

def inter_section(a, b):
    inter_list = [num for num in a if num in b]
    first = inter_list[-1]
    last = inter_list[0]
    inter_list[0] = first
    inter_list[-1] = last
    return tuple(inter_list)


print(inter_section(list1, list2))
