# Write a function called 'word_index' that takes one argument, a list of strings, and returns the index of the longest word in the list.
# If there is no longest word (if all the strings are the same length), the function should return zero (0).
# For example, the first list below should return 2.

words1 = ['Hate', 'remorse', 'vengeance']

# and this list should return zero (0).

words2 = ['Love', 'Hate']

def word_index(arr: list):
    for word in arr:
        if all(len(word) == len(arr[0]) for word in arr):
            return 0
    else:
        word == len(max(arr))
        return f'The longest word is at the index: {arr.index(word)}'
        
print(word_index(words1))
print(word_index(words2))