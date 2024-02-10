# Write a function called 'nested_list' that takes any number of lists and creates a 2-dimensional nested list of lists. 
# Your code must check that the inputs are of the list data type.
# For example, if you pass the following arguments: [1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5].
# Your code should return [[1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5]]
# If you pass (1, 2, 3, 5), [1, 2, 3, 4], [1, 3, 4, 5] as arguments, your function should return 'Invalid arguments. Please check your arguments.'

def nested_list(*args: list):
    for lst in args:
        if type(lst) != list:
            return 'Invalid arguments. Please check your arguments.'
    
    list1 = []
    for i in range(len(args)):
        for j in args:
            list1.append(j)
        break
    
    return list1


lst1 = [1, 2, 3, 5]
lst2 = [1, 2, 3, 4]
lst3 = [1, 3, 4, 5]
print(nested_list(lst1, lst2, lst2))