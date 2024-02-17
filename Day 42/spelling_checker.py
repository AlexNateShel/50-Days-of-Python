# Write a function called 'spelling_checker'.
# This code asks the user to input a word, and if the user inputs the wrong spelling, it should suggest the correct spelling by asking the user if they meant to type that word.
# If the user says no, it should ask the user to enter the word again.
# If the user says yes, it should return the correct word.
# If the word entered by the user is correctly spelled, the function should return the correct word.
# Use the module 'textblob'.

from textblob import TextBlob

def spelling_checker():
    while True:
        word = input('Enter a word : ')
        if word != TextBlob(word).correct():
            question = input(f'Did you mean '
                             f'{TextBlob(word).correct()}?'
                             f'type yes/no : ')
            if question == 'yes':
                break
            else:
                print('Please try again')
        
        elif word == TextBlob(word).correct():
            break
    return f'Your word is, {TextBlob(word).correct()}'


print(spelling_checker())
