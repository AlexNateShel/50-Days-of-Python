# Write a function called 'guess_a_number'.
# The function should ask a user to guess a randomly generated number.
# If the user guesses a higher number, the code should tell them that the guess is too high.
# If the user guesses a lower number, the code should tell them that the guess is too low.
# The user should get a maximum of three (3) guesses. 
# When the user guesses right, the code should declare them a winner.
# After three wrong guesses, the code should declare them losers.

import random

random_number = random.randint(0, 10)

def guess_a_number():
    count = 0
    while count < 3:
        guess = int(input('Guess a number between 0 and 10: '))
        count += 1 
        if count == 3:
            print('You have run out of guesses.'
                  'You lose.')
            break
        elif guess > random_number:
            print('The number you guessed is too high.'
                  'Try again')
        elif guess < random_number:
            print('The number you guess is too low.'
                  'Try again.')
        else:
            print('Correct. You win.')
            break
        
guess_a_number()