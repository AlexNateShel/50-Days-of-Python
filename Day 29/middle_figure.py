# Write a function called 'middle_figure' that has two parameters, a and b.
# The two parameters are strings.
# The function joins the two strings and finds the middle element.
# If the combined string has a middle element, the function should return the element; otherwise it should return 'no middle figure'.
# Use "make love" as an argument for a, and "not wars" as an argument for be. 
# Your function should return "e" as the middle element.
# Whitespaces should be removed.

def middle_figure(a: str, b: str):
    modified_str = (a + b).replace(' ', '')
    len_modified_str = len(modified_str)
    middle = len_modified_str // 2
    if len(modified_str) % 2 == 1:
        return 'The middle figure is', modified_str[middle]
    else:
        return 'No middle figure.'
    
a = 'make love'
b = 'not wars'
print(middle_figure(a, b))

