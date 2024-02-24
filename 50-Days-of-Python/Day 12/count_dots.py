# Write a function called 'count_dots'. 
# This function takes a string separated by dots as a parameter and counts how many dots are in the string.
# For example, "h.e.l.p." should return 4 dots, and "he.lp." should return 2 dots.

def count_dots(str):
    count = 0
    for z in str:
        if z == '.':
            count += 1
        else:
            continue
    return f'The string has {count} dots.'

str1 = 'h.e.l.p.'
print(count_dots(str1))
str2 = 'he.lp.'
print(count_dots(str2))