# Write a function called 'even_or_average' that asks a user to input five numbers.
# Once the user is done, the code should return the largest even number in the inputted numbers.
# If there are no even numbers in the list, the code should return the average of all five numbers.

def even_or_average():
    numbers = input('Enter 5 numbers: ').split()
    largest = None
    total = 0
    count = 0
    for num in numbers:
        num = int(num)
        if num % 2 == 0:
            if largest == None:
                largest = num
            elif largest < num:
                largest = num
            else:
                largest = largest
            return largest
        else:
            count += 1
            total = total + num
            average = total / count
    return average

print(even_or_average())
