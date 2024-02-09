# Write a function called 'capitalize'. 
# This function takes a string as an argument and capitalizes the first letter of each word.
# For example, "i like learning", becomes "I Like Learning".

def capitalize(str):
    upper = [ ]
    for char, word in enumerate(str.split()):
        if word[0].islower():
            upper.append(word.capitalize())
        else:
            upper.append(word)
    return ' '.join(upper)


str2 = 'i like learning'
print(capitalize(str2))

