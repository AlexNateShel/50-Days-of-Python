# You are given a list of names, and you are asked to write a code that returns all the names that start with "S".
# Your code should return a dictionary of all the names that start with 'S' and how many times they appear in the dictionary.
# Here is a list below:
names = ['Joseph', 'Nathan', 'Sasha', 'Kelly', 'Muhammad', 'Jabulani', 'Sera', 'Patel', 'Sera']

d = {}
for name in names:
    if name.startswith('S'):
        d.update({name: names.count(name)})

print(d)