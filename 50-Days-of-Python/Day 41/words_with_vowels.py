# Create a function called 'words_with_vowels'.
# This function takes a string of words and returns a list of only the words that have vowels in them.
# "You have no rhythm", for example, should return ["you", "have", "no"].

def words_with_vowels(str):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    vowel_words = []
    for word in str.split():
        if any(char in vowels for char in word):
            if word not in vowel_words:
                vowel_words.append(word)
        else: continue
    return vowel_words

x = 'You have no rhythm'
print(words_with_vowels(x))
    