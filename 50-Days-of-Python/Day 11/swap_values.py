# Write a function called 'swap_values'.
# This function takes a list of numbers and swaps the first element with the last element.
# For example, if you pass [2, 4, 67, 7] as a parameter, your function should return [7, 4, 67, 2].

def swap_values(num_list: list):
    first = num_list[0]
    last = num_list[-1]
    num_list[0] = last
    num_list[-1] = first
    return num_list

nums = [2, 4, 67, 7]
print(swap_values(nums))
