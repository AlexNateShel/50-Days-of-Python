# Write a function called 'create_user'.
# This function asks the user to enter their name, age, and password.
# For example, if the user enters Peter as his name, 18 as his age, and "love" as his password, the function should save the information as:
# {'name': 'Peter', 'age': 18, 'password': 'love'}
# Once the information is saved, the function should print to the user, 'User saved, Please login'
# The function should then ask the user to re-enter their name and password.
# If the name and password match what is save in the dictionary, the function should return 'Logged in successfully'.
# If the name and password do not match what is saved in the dictionary, the function should print 'Wrong password or username, please try again.'
# The function should keep running until the user enters the correct logging details.

def create_user():
    users = {}
    name = input('Enter your name: ')
    age = int(input('Enter your age: '))
    password = input('Enter your password: ')
    users.update({'name': name})
    users.update({'age': age})
    users.update({'password': password})
    print('User save, Please login.')

    while True:
        user_name = input('Enter your username: ')
        password = input('Enter your password: ')
        if user_name == users.get('name') and password == users.get('password'):
            print('Logged in succesfully.')
            return 'Logged in successfully.'
        else:    
            print('Wrong password or username, please try again.')
        

create_user()
