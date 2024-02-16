# Create a function called 'generate_password' that generates any length of password for the user.
# The password should have a random mix of uppercase letters, lowercase letters, numbers, and punctuation symbols.
# The function should ask the user how strong they want the password to be. 
# The user should pick from 'weak', 'strong', or 'very strong'.
# If the user picks 'weak', the function should generate a 5-character password.
# If the user picks 'strong', generate an 8-character password, and if they pick 'very strong' generate a 12-character password.

import string
import random


def generate_password():
    pool = string.ascii_letters + string.digits + string.punctuation
    password1 = []
    length = input('Pick your password length'
                   'weak, strong, or very strong: ')
    
    if length == 'weak':
        length = 5
    elif length == 'strong':
        length = 8
    elif length == 'very strong':
        length = 12
    for i in range(length):
        password = str(random.choice(pool))
        password1.append(password)
    return 'Your password is', ''.join(password1)


print(generate_password())