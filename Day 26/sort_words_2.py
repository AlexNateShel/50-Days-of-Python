# Write a function called 'sort_words' that takes a string of words as an argument, removes the whitespaces, and returns a list of letters sorted in alphabetical order.
# Letters will be seperated by commas.
# All letters should appear once in the list.
# This means that you sort and remove duplicates. 
# For example, "love life" should return as ['e, f, i, l, o, v']

def sort_words(sentence):
    letter_list = []
    sentence = sentence.replace(' ', '')
    for i in sentence:
        if i not in letter_list:
            letter_list.append(i)
    letter_list.sort()
    sorted_letters = [','.join(letter_list)]
    return sorted_letters

str1 = 'love live'
print(sort_words(str1))