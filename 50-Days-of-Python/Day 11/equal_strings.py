# Write a function called 'equal_strings'. 
# The function takes two strings as arguments and compares them.
# If the strings are equal (if they have the same characters and have equal length), it should return 'True'; if they are not, it should return 'False'.
# For example, "love" and "evol" should return 'True'.

def equal_strings(str1, str2):
    str1 = sorted(str1)
    str2 = sorted(str2)
    if str1 == str2:
        return True
    else:
        return False
    
x = 'love'
y = 'evol'
print(equal_strings(x, y))

a = 'Love'
b = 'Hate'
print(equal_strings(a, b))

c = 'Love'
d = 'evol'
print(equal_strings(c, d))

