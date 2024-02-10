# Create a simple calculator.
# The calculator should be able to perform the following basic math operations: add, subtract, divide, and multiply.
# The calculator should take input from users. 
# The calculator should be able to handle 'ZeroDivisionError', 'NameError', and 'ValueError'.

import operator

def calculator():
    try:
        
        first_number = int(input('Enter a number: '))
        opt = input('Select the operation that you\'d like to perform: ( + )  ( - )  ( * ) ( / ) : ')
        second_number = int(input('Enter another number: '))
        if opt not in ('+, -, *, /'):
            print('Please select a valid symbol of operation.')
    except ValueError:
        print('Please enter a valid number.')
    except ZeroDivisionError:
        print('You cannot divide a number by zero, choose another number.')
    else:
        if opt == '+':
            return f'{first_number} + {second_number} = {operator.add(first_number, second_number)}'
        elif opt == '-':
            return f'{first_number} - {second_number} = {operator.sub(first_number, second_number)}'
        elif opt == '*':
            return f'{first_number} * {second_number} = {operator.mul(first_number, second_number)}'
        elif opt == '/':
            return f'{first_number} / {second_number} = {operator.truediv(first_number, second_number)}'

print(calculator())