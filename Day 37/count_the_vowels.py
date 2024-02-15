# Create a function called 'count_the_vowels'. 
# The function takes on argument, a string, and returns the number of vowels in the string.
# If the data type of the input is not of the string type, the function should return "invalid input".
# If the argument has no vowels, your function should return "The string has no vowels."
# If a vowel appears in a string more than once, it should be counted as one. 
# For example, "hello" should return two (2) vowels; "saas" should return one (1) vowel; and "sly" should return "The string has no vowels."
# Your code should count lowercase and uppercase vowels.

def count_the_vowels(word: str):
    count = 0
    vowels = ['a', 'i', 'e', 'o', 'u']
    vowels_count = []

    if type(word) != str:
        return 'Invalid input'
           
    for letter in word:
        if letter in vowels:
            if letter not in vowels_count:
                vowels_count.append(letter)
    
    if len(vowels_count) > 1:
        return f'There are {len(vowels_count)} vowels in "{word}".'
    elif len(vowels_count) == 1:
        return f'There is {len(vowels_count)} vowel in "{word}".'
    else:
        return f'There are no vowels in "{word}".'





str1 = 'hello'
str2 = 'saas'
str3 = 'sly'
str4 = 100
str5 = ''
print(count_the_vowels(str1))
print(count_the_vowels(str2))
print(count_the_vowels(str3))
print(count_the_vowels(str4))