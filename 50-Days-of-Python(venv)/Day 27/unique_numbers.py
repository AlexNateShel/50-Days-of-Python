# Write a function called 'unique_numbers' that takes a list of numbers as an argument.
# Your function is going to find all the unique numbers in the list. 
# It will then sum up the unique numbers.
# You will calculate the difference between the sum of all the numbers in the original list and the sum of the unique numbers in the list.
# If the difference is an even number, your function should return the original list. 
# If the difference is an odd number, your function should return a list with only unique numbers.
# For example, [1, 2, 4, 5, 6, 7, 8, 8] should return [1, 2, 4, 5, 6, 7, 8, 8]

def unique_numbers(numbers: list):
    unique_nums = [ ]
    for num in numbers:
        if num not in unique_nums:
            unique_nums.append(num)
    difference = sum(unique_nums) - sum(numbers)
    if difference % 2 == 0:
        return numbers
    if difference % 2 != 0:
        return unique_nums
    

list1 = [1, 2, 4, 5, 6, 7, 8, 8] 
list2 = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6]
print(unique_numbers(list1))
print(unique_numbers(list2))