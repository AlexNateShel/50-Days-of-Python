# Write a function called 'python_snakes' that takes a number as an argument and creates the pyramid shape using the number's range.
# (Hint: Use the loops and emoji libraries for snake emojis.) 
# If you pass 7 as an argument, your should should print out the following:
#       🐍  

#      🐍  🐍  

#     🐍  🐍  🐍  

#    🐍  🐍  🐍  🐍  

#   🐍  🐍  🐍  🐍  🐍  

#  🐍  🐍  🐍  🐍  🐍  🐍

# 🐍  🐍  🐍  🐍  🐍  🐍  🐍

from emoji import emojize

def python_snakes(num: int):
    for x in range(0, num):
        for y in range(num, x, -1):
            print(end=' ')
        for z in range(0, x+1):
            print(emojize(':snake:'), end='  ')
        print('\n')

print(python_snakes(7))