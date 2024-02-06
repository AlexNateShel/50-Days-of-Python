# Write a function called 'prime_numbers'.
# This function asks the user to enter a number (an integer) as an argument and returns a list of all the prime numbers within its range.
# For example, if the user enters '10', your code should return [2, 3, 5, 7]

def prime_numbers():
    number = int(input('Enter a number: '))
    prime = []
    for i in range(0, number + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                prime.append(i)
    return prime


print(prime_numbers())