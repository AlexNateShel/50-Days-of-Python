# Write two functions.
# The first function is called 'count_words' which takes a string of words as argument and counts how many words are in the string.
# The second function, called 'count_elements' takes a string of words and counts how many elements are in the string.
# Do not count the whitespaces.
# The first function will return the number of words in a string, and the second one will return the number of elements (less whitespace).
# If you pass "I love learning", the 'count words' function should return 3 words and 'count elements should return 13 elements.

def count_words(str):
    word_count = str.split()
    word_count = len(word_count)
    return f'There are {word_count} words in this string.'

str1 = 'I love learning'
print(count_words(str1))