# Write a function called 'largest_number' that takes a list of integers as an argument and re-arranges the individual digits to create the largest possible number.
# For example, if you pass the following as an argument:
list1 = [3, 67, 87, 9, 2]
# Your code should return the number in this exact format: 9,877,632 as the largest number.

def largest_number(arg: list):
    list1 = []
    n = str(arg).strip('[,]').replace(',', '').replace(' ', '')
    for i in n:
        list1.append(int(i))
    list1.sort(reverse=True)
    large_number = int(''.join(map(str, list1)))
    return 'The largest number is, {:,}'.format(large_number)

print(largest_number(list1))