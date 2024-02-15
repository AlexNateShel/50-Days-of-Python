# Write a function called 'count' that takes one argument, a string and returns a dictonary of how many times each element appears in the string.
# For example, 'hello' should return:
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}

def count(x: str):
    letter_count = {}
    count = 0
    for letter in x:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1

    return letter_count

x = 'hello'
print(count(x))