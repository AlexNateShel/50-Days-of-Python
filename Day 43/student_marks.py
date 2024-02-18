# Write a function called 'student_marks' that records the marks achieved by students in a test. 
# The function should ask the user to input the name of the student and then ask the user to input the marks acheived by the student.
# The information should be stored in a dictionary.
# The name is the key, and the mark is a value.
# When the user enters "done", the function should return a dictionary of the names and values entered or an empty dictionary if no values are entered.
# Your code should ensure that:
# If a name contains punctuation characters: (!"#$%&'()*+,-./:;<=>?@[\]^_^{|}~) or numbers (digits) your code should raise a NameError and ask the user to enter a valid name.
# If the user enters invalid values for value, your code should handle the ValueError.
# Your code should run until valid values are inputted.

import string

def student_marks():
    student_dict = {}
    while True:
        try:
            name = input("Enter the student's name: ")
            for letter in name:
                if letter in string.punctuation or letter in string.digits:
                    raise NameError('Please enter a valid name')
            if name == 'done':
                break
            marks = int(input("Enter the student's mark: "))
            student_dict[name] = student_dict.get(marks, 0) + marks
        except (NameError, ValueError) as e:
            print(f'Error: {e}')

    return student_dict

print(student_marks())