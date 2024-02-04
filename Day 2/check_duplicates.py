# Write a function called 'check_duplicates' that takes a list of strings as an argument.
# The function should check if the list has any duplicates.
# If there are duplicates, the function should return a list of duplicates.
# If there are no duplicates, the function should return "no duplicates". 
# For example, the list of fruits below should return ["apple", "banana"], and the list of names should return "no duplicates".
# fruits = ['apple', 'orange', 'banana', 'apple', 'banana']
# names = ['Yoda', 'Moses', 'Joshua', 'Mark'] 

def check_duplicates(list):
    duplicates = []
    for word in list:
        if list.count(word) > 1:
            if not word in duplicates:
                duplicates.append(word)
    if duplicates:
        return duplicates
    else:
        return "No duplicates"
        
    
names = ['Yoda', 'Moses', 'Joshua', 'Mark']
fruits = ['apple', 'orange', 'banana', 'apple', 'banana']
print(check_duplicates(fruits))
print(check_duplicates(names))