s = 'Hi my name is Richard'

# Write a function called 'string_length' that takes a string of words (words and spaces) as an argument.
# This function should return the length of all the words in the string.
# Return the results in the form of a dictionary.
# The string above should return:
# {'Hi': 2, 'my': 2, 'name': 4, 'is': 2, 'Richard': 7}

def string_length(s: str) -> dict:
    list1 = []
    words_dict = {}
    for word in s.split():
        list1.append(word)
    for word in list1:
        words_dict[word] = len(word)
    return words_dict

print(string_length(s))