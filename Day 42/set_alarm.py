# Write a function called 'set_alarm' that sets an alarm clock for the user.
# The function should ask the user to enter the time they want the alarm to go off. 
# The user should enter the time in hours and minutes.
# The function should run until the user enters a valid input.
# Once the user enters a valid input, the function should then print the time when the alarm will go off.
# When it's alarm time, the code should let off a sound.
# Use the 'winsound' module for sound.

import winsound
import datetime

def set_alarm():
    while True:
        hour = input('Please enter the hour (0-23): ')
        if hour.isdigit() and 0 <= int(hour) <=23:
            break
        print('Invalid hour. Please enter a valid hour')

    while True:
        minute = input('Please enter the minute (0-59): ')
        if minute.isdigit() and 0 <= int(minute) <= 59:
            break
        print('Invalid minute. Pleas enter a valid minute.')

    
    alarm_time = "{:02d}:{:02d}".format(int(hour), int(minute))
    print('You have set the alarm for', alarm_time)

    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if alarm_time == now:
            print('Wake up')
            print('Wake up')
            print('Wake up')
            winsound.PlaySound('SystemExit', winsound.SND_ALIAS)
            break

set_alarm()
