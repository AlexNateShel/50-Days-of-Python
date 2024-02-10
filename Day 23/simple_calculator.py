# Create a simple calculator.
# The calculator should be able to perform the following basic math operations: add, subtract, divide, and multiply.
# The calculator should take input from users. 
# The calculator should be able to handle 'ZeroDivisionError', 'NameError', and 'ValueError'.

def calculator():
    try:

        num1 = int(input('Enter a number: '))
        operation = input('Choose an operator("+, -, *, /,"): ')
        num2 = int(input('Enter another number: '))
        if operation not in ('+, -, *, /') or len(operation) > 1:
            print('Please choose a valid operator.')
    except ValueError:
        print('Please enter a valid number.')
    except ZeroDivisionError:
        print('You cannot divide a number by zero, select another number.')
    else: 
        if operation == '+':
            return f'{num1} + {num2} = {num1 + num2}'
        elif operation == '-':
            return f'{num1} - {num2} = {num1 - num2}'
        elif operation == '*':
            return f'{num1} * {num2} = {num1 * num2}'
        elif operation == '/':
            return f'{num1} / {num2} = {num1 / num2}'
    return 'Try again.'


print(calculator())