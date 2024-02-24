# Create a function called 'words_with_vowels'.
# This function takes a string of words and returns a list of only the words that have vowels in them.
# "You have no rhythm", for example, should return ["you", "have", "no"].

def words_with_vowels(a):
    vowels = []
    for word in a.split():
        for i in word:
            if i in 'aeiou':
                if word not in vowels:
                    vowels.append(word)
    return vowels

x = 'You have no rhythm'
print(words_with_vowels(x))