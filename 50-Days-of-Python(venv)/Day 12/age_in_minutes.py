# Write a function called 'age_in_minutes' that tells a user how old they are in minutes.
# Your code should ask the user to enter their year of birth, and it should return their age in minutes (by subtracting their year of birth from the current year). 
# Here are things to look out for:
#   a. The user can only input a 4-digit year of birth. For example, 1930 is a valid year.
#      However, entering any number longer or shorter than 4 digits, should rendet the input invalid.
#      Notify the user that they must enter a four-digit number.
#   b. If a user enters a year before 1900, your code should tell the user that the input is invalid.
#      If the user enters the year after the current year, the code should tell the user to input a valid year.
# The code should run until the user inputs a valid year. Your function should return the user's age in minutes.
# For example, if someone enters 1930, as their year of birth, your function should return:
#   "You are 48,355,200 minutes old."

from datetime import datetime

def age_in_minutes():
    current_year = datetime.now().year
    while True:
        year = input('Enter the year you were born: ')
        if len(year) != 4:
            print('Enter a valid year of birth.')
        elif int(year) < 1900 or int(year) > current_year:
            print('Enter a valid year of birth.')
        else:
            years_lived = current_year - int(year)
            minutes_in_year = 365 * 24 * 60
            minutes_lived = years_lived * minutes_in_year
            return f'You have lived for {minutes_lived} minutes.'

print(age_in_minutes())    