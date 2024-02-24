# Write a function called 'all_the_same' that takes one argument, a string, a list, or a tuple, and checks if all the elements are the same.
# Use the instance function to check that the input data is either a string, a list, or a tuple, or else raise a TypeError that says that "Input must be a string, a list, or a tuple."
# If the elements are the same, the function should return True. 
# If not, it should return False.
# For example, ["Mary", "Mary", "Mary"] should return True.

def all_the_same(data):
    if isinstance(data, (str, list, tuple)):
        check_list = all(i == data[0] for i in data)
        return check_list
    else:
        raise TypeError('Input must be a string, a list, or a tuple.')

    
string1 = 'aaaaaaa'
list1 = ['Mary', 'Mary', 'Mary']
tuple1 = (7, 7, 7)
str2 = 'abababa'
print(all_the_same(string1))
print(all_the_same(list1))
print(all_the_same(tuple1))
print(all_the_same(str2))
