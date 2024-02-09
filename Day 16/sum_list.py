# Write a function called 'sum_list' with one parameter that takes a nested list of integers as an argument and returns the sum of the integers.
# For example, if you pass [[2, 4, 5, 6], [2, 3, 5, 6]] as an argument, your function should return a sum of 33.

def sum_list(lst:list):
    total = 0
    for lst1 in lst:
        for num in lst1:
            total = num + total
    return f'The sum of the numbers in the list is {total}'

    
        

list1 = [[2, 4, 5, 6], [2, 3, 5, 6]]
print(sum_list(list1))