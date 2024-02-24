# You are given a string of words. 
# Some of the words in the string contain uppercase letters.
# Write a code that will return all the words that have an uppercase letter. 
# Your code should return a list of the words.
# Eah word in the list should be reverse.
# Here is how your output should look:

# ['gninrAel', 'tUb', 'uoY', 'yLppa', 'flesRuoy', 'eVeihca']

import string

str1 = 'leArning is hard, bUt if You appLy youRself you can achieVe success'

upper_words = [ ]
for word in str1.split():
    for letter in word:
        if letter in string.ascii_uppercase:
            upper_words.append(''.join(word[::-1]))
            
print(upper_words)
