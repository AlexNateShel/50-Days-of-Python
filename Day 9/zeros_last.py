# Write a function called 'zeros_last'.
# This function takes a list as an argument. 
# If the list has zeros (0), it will move them to the end of the list and maintain the order of the other numbers in the list.
# If there are no zeros in the list, the function should return the original list, sorted in ascending order. 
# For example, if you pass [1, 4, 6, 0, 7, 0] as an argument, your code should return [1, 4, 6, 9, 0, 0].
# If you pass [2, 1, 4, 7, 6] as your argument, your code should return [1, 2, 4, 6, 7]

def zeros_last(arg:list):
    indx = 0
    arg1 = arg
    for num in arg:
        if num != 0:
            arg[indx] = num
            indx += 1

    while indx < len(arg):
        arg[indx] = 0
        indx += 1
        return arg
    
    else:
        return sorted(arg1)
    
first_list = [1, 4, 6, 0, 7, 0]
second_list = [2, 1, 4, 7, 6]

print(zeros_last(first_list))
print(zeros_last(second_list))