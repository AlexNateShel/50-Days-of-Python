# Write a function called 'find_index' that takes two arguments; a list of integers, and an integer.
# The function should return the indexes of the integers in the list.
# If the integer is not in the list, the function should convert all the numbers in the list into the given integer.
# For example, if the list is [1, 2, 4, 6, 7, 7] and the integer is 7, your code should return [4, 5] as the indexes of 7 in the list.
# If the list is [1, 2, 4, 6, 7, 7] and the integer is 8, your code should return [8, 8, 8, 8, 8, 8] because 8 is not in the list.

def find_index(arg: list, n: int) -> list:
    list1 = []
    for i, val in enumerate(arg):
        if val == n:
            list1.append(i)
        if n not in arg:
            for j in arg:
                list1.append(n)
            return list1
    
    return list1
        
        
x = [1, 2, 4, 6, 7, 7]
print(find_index(x, 7))
print(find_index(x, 8))
