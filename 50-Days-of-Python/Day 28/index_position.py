# Write a function called 'index_position'. This function takes a string as a parameter and returns the positions, or indexes of all lowercase letters in the string.
# For example, "LovE" should return [1, 2]

def index_position(lst):
    indx = []
    for i, item in enumerate(lst):
        if item.islower():
            indx.append(i)
    return indx

str1 = 'LovE'
print(index_position(str1))