# Write a function called 'sort_words' that takes a string of words as an argument, removes the whitespaces, and returns a list of letters sorted in alphabetical order.
# Letters will be seperated by commas.
# All letters should appear once in the list.
# This means that you sort and remove duplicates. 
# For example, "love life" should return as ['e, f, i, l, o, v']

def sort_words(words: str):
    list1 = [ ] 
    for word in words.split():
        for letter in word:
            if not letter in list1:
                list1.append(letter)
    list1.sort()  
    letter_list = [','.join(list1)]
    return letter_list

str1 = 'love life'
print(sort_words(str1))
