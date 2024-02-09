# Write a function called 'even_or_average' that asks a user to input five numbers.
# Once the user is done, the code should return the largest even number in the inputted numbers.
# If there are no even numbers in the list, the code should return the average of all five numbers.

def even_or_average():
    average_number = []
    even_number = []
    while True:
        number = input('Enter a number or done: ')
        average_number.append(int(number))
        if int(number) % 2 == 0:
            even_number.append(number)
        if len(average_number) == 5:
            break
    if len(even_number) > 0:
        return f'The largest even number: {max(even_number)}.'
    
    else:
        return f'The average is: {sum(average_number) / len(average_number)}.'
    
print(even_or_average())