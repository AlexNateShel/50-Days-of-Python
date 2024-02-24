# Write a function called 'analyse_string' that takes a string as an argument and returns
# the number of special characters (# $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~ ),
# numeric characters, and total characters (the length of the string minus whitespaces) in the string.
# Return everything in a dictionary format:

# {"specail_char": "number", "numeric_char": "number", "total_char": "number"}

# Use the string below as an argument:
# 'Python has a string format operator %. This functions analogously to printf format strings in C, e.g. "spam=%seggs%d"% ("blah", 2) evaluates to "spam=blah eggs=2?".'

import string

def analyse_string(s):
    special_char = []
    numeric_char = []
    d = {
        'numeric': '',
        'special_char': '',
        'total_char': ''
    }

    for i in s.replace(' ', ''):
        if i in string.punctuation:
            if i not in special_char:
                special_char.append(i)
            d['special_char'] = len(special_char)
        if i in string.digits:
            if i not in numeric_char:
                numeric_char.append(i)
            d['numeric'] = len(numeric_char)
        else:
            d['total_char'] = len(s.replace(' ', ''))
    return d

x = 'Python has a string format operator %. This functions analogously to printf format strings in C, e.g. "spam=%seggs%d"% ("blah", 2) evaluates to "spam=blah eggs=2?"' 
print(analyse_string(x))