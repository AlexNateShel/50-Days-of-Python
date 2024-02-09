# Write a function called 'flat_list' that takes one argument, a nested list. 
# The function converts the nested list into a one-dimensional list. 
# For example, [[2, 4, 5, 6]] should return [2, 4, 5, 6].

def flat_list(lst1:list):
    list1 = []
    for items in lst1:
        for x in items:
            list1.append(x)
    return list1


list2 = [[2, 4, 5, 6]]

print(flat_list(list2))
