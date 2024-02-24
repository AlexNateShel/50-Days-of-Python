s = 'love live and laugh'

# Write a function called multiply words that takes a string as an argument and multiplies the length of each word in the string by the length of other words in the string.
# For example, the string above should return '240: love (4), live (4), and (3), laugh (5)'.
# However, your function should only multiply words with all lowercase letters.
# If a word has one uppercase letter, it should be ignored.
# For example, the following string:
t = 'Hate war love Peace' 
# Should return '12 - war (3), love (4)'.
# Hate and Peace will be ignored because they have at least one uppercase letter.

import math

def multiply_words(s: str):
    words_len = []
    for word in s.split():
        if word.islower():
            words_len.append(len(word))
        words_prod = math.prod(words_len)
    return f"The product of the words lengths is: {words_prod}"

print(multiply_words(s))
print(multiply_words(t))
