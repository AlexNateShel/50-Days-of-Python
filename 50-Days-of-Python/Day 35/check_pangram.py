# Write a function called 'check_pangram' that takes a string and checks if it is a pangram.
# A pangram is a sentence that contains all the letters of the alphabet. 
# If it is a pangram, the function should return True, otherwise it should return False.
# The following sentence is a pangram, so it should return True:

# sentence = 'the quick brown fox jumps over a lazy dog'
import string

def check_pangram(sentence):
    letters = []
    alphabet = string.ascii_lowercase
    sentence = sentence.replace(' ', '')
    for letter in sentence:
        if letter not in letters:
            letters.append(letter)
    letters.sort()
    sentence = ''.join(letters)
    if alphabet == sentence:
        return True
    else:
        return False
               


sentence = 'the quick brown fox jumps over a lazy dog'
print(check_pangram(sentence))