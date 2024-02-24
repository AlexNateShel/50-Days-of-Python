str1 = 'the love is real'

# Write a function called 'read_backwards' that takes a string as an argument and reverses it.
# The string above, for example, should return 'real is love the'.

def read_backwards(str2: str):
    str3 = []
    for i in str2.split()[::-1]:
        str3.append(i)
    return ' '.join(str3)

print(read_backwards(str1))