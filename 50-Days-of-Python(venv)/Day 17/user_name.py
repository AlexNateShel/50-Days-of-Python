# Write a function called 'user_name', that creates a username for the user.
# The function should ask a user to input their name.
# The function should then reverse the name and attach a randomly issued number between 0 and 9 at the end of the name.
# The function should return the username.

import random

def user_name():
    name = input('Enter your name: ')
    name = name[::-1].lower()
    a = random.randint(0,9)
    user_name = name + str(a)
    return f"Your username is '{user_name}'."

print(user_name())


    
