# Write a function called 'count_dots'. 
# This function takes a string separated by dots as a parameter and counts how many dots are in the string.
# For example, "h.e.l.p." should return 4 dots, and "he.lp." should return 2 dots.

def count_dots(str):
    x = str.split('.')
    return f'The string has {len(x)-1} dots.'

str1 = 'h.e.l.p.'
str2 = 'he.lp.'
print(count_dots(str1))
print(count_dots(str2))