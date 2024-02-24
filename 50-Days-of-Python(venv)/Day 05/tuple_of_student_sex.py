# You work for a school, and your boss wants to know how many female and male students are enrolled in the school.
# The school has saved the students on a list.
# Your task is to write a code that will count how many males and females are in the list. 
# Here is a list below:

students = ['Male', 'Female', 'female', 'male', 'male', 'male', 'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']

# Your code should return a list of tuples. The list above should return: [('male', 7), ('female', 6)]

def count_students(arg: list):
    gender = []
    count = []
    for names in students:
        gender.append(names.lower())
    for boy in gender:
        if boy == 'male':
            count.append((boy, gender.count(boy)))
            break
    for girl in gender:
        if girl == 'female':
            count.append((girl, gender.count(girl)))
            break
    return count

print(count_students(students))
