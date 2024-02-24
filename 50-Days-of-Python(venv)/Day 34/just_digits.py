# In this challenge, copy the text below and save it as a CSV vile.
# Save it in the same folder as your Python file.
# Save it as 'python.csv'.

# Write a function called 'just_digits' that reads the text from the CSV file and returns old digit elements from the file. 
# Your function should return 1991, 2, 200, 3, 2008 as a list of strings.

# "Python was released in 1991 for the first time. 
# Python 2 was released in 2000 and introduced new features, such as list comprehensions and a cycle-detecting garbage collection system (in addition to reference counting).
# Python 3 was released in 2008 and was a major revision of the language that is not completely backwards-compatible."
# Soure: Wikipedia

def just_digits():
    with open('python.csv', 'r') as file:
        open_file = file.read().split()
        list1 = []
        for item in open_file:
            if item.isdigit():
                list1.append(item)
    return list1

print(just_digits())