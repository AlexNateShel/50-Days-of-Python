# Write a function called 'average_calories' that calculates the average calorie intake of a user.
# The function should ask the user to input their calorie intake for any number of days, amd once they hit 'done', it should calculate and return the average intake.

def average_calorie():
    calories = []
    while True:
        calorie = input('Enter you calories or done to stop: ')
        if calorie == 'done':
            break
        calories.append(int(calorie))
    return f'The average daily calorie intake is: {sum(calories) / len(calories):.2f}'


print(average_calorie())
