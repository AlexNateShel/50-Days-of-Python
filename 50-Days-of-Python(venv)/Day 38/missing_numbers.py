# Write a function called 'missing_numbers' that takes a list of sequence numbers as argument, and finds the missing numbers in the sequence.
# For example, the list below should return:
# [4, 8, 10, 13, 16, 29, 30]

list1 = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17, 
         18, 19,20, 21, 22, 24, 25, 26, 27, 28, 31]

def missing_numbers(arr: list) -> list:
    missing_nums = []
    for i in range(arr[0], arr[-1] + 1):
        if i not in arr:
            missing_nums.append(i)
        
    return missing_nums

print(missing_numbers(list1))