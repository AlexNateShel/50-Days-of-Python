# Write a function called 'register_check' that checks how many students are in school.
# The function takes a dictionary as an argument.
# If the student is in school, the dictionary says "yes".
# If the student is not in school, the dictionary says "no".
# Your function should return the number of students in school.
# Using the dictionary below, your function should return 3.

register = {'Michael' : 'yes', 'John': 'no', 'Peter': 'yes', 'Mary': 'yes'}

def register_check(d: dict):
    count = 0
    for v in d.values():
        if v == 'yes':
            count += 1
    return f'The number of students in school is', count

print(register_check(register))
