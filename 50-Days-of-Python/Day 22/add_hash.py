# Create three functions. 
# The first, called 'add_hash' takes a string and adds a hash (#) between the words.
# The second function is called 'add_underscore' removes the hash (#) and replaces it with an underscore.
# The third function, called 'remove_underscore', removes the underscore and replaces it with nothing.
# If you pass 'Python' as an argument for the three functions, and call them at the same time like:

# print(remove_underscore(add_underscore(add_hash('Python'))))
# it should return 'Python'.

def add_hash(x: str):
    return '#'.join(x)

def add_underscore(x):
    return str(x).replace('#', '_')

def remove_underscore(x):
    return str(x).replace('_', '')


str1 = 'Python'

print(remove_underscore(add_underscore(add_hash(str1))))
