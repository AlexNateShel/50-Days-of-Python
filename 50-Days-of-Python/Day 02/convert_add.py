# Write a function called 'convert_add' that takes a list of strings as an argument, converts them to integers, and sums the list. 
# For example, ["1", "2", "3"] should be converted to [1, 3, 5] and summed to 9.

def convert_add(list):
    lst = []
    for nums in list:
        lst.append(int(nums))
    return f'The sum is {sum(lst)}'

print(convert_add(['1', '2', '3']))
