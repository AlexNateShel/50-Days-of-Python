# Write a function called 'add_reverse'.
# This function takes two lists as arguments, adds each corresponding number, and reverses the outcome.
# For example, if you pass [10, 12, 34] and [12, 56, 78], you code should return [112, 22, 68].
# If the two lists are not of equal length, the code should return a message that "the lists are not of equal length."

def add_reverse(lst1:list, lst2:list):
    combined_list = []
    if len(lst1) == len(lst2):
        for num in range(0, len(lst1)):
            combined_list.append(lst1[num] + lst2[num])
            combined_list.reverse()
        return combined_list
    else:
        return 'The lists are not of equal length.'
        
    

list1 = [10, 12, 34]
list2 = [12, 56, 78]
print(add_reverse(list1, list2))
list3 = [22, 55, 99, 87]
print(add_reverse(list1, list3))