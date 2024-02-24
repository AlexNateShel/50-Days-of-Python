# Write a function called 'translate' that takes the following words and translates them into Pig Latin.

my_string = 'i love python'

# Here are the rules:
#   1. If a word starts with a vowel (a, e, i, o, u) add 'yay' at the end.
#      For example, 'eat' will become 'eatyay'.
#   2. If a word starts with anything other than a vowel, move the first letter to the end of and add 'ay' to the end.
#      For example, 'day' will become 'ayday'.

def translate(str):
    pig_latin = []
    for i, word in enumerate(str.split()):
        if word[0] in 'aeiou':
            pig_latin.append(word[i] + 'yay')
        else:
            pig_latin.append(word[1:] + word[0] + 'ay')
    return pig_latin

print(translate(my_string))