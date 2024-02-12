# Write a function that has one parameter and takes a list of words as an argument. 
# The function returns the longest word from the list.
# Name the function 'longest_word'.
# The function should return the longest word and the number of letters in that words.
# For example, if you pass ['Java', 'JavaScript', 'Python'], your funtion should return [10, JavaScript] as the longest word.

def longest_word(list1):
    long_word = []
    for word in list1:
        long_word.append([len(word), word])
    return max(long_word)

list1 = ['Java', 'JavaScript', 'Python']
print(longest_word(list1))