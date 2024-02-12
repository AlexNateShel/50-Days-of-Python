# Write a function called 'repeated name' that finds the most repeated name in the following list.
# Your function should return a tuple of the name and how many times it appears. 
# The list below should return: ("Peter", 3)

names = ['John', 'Peter', 'John', 'Peter', 'Jones', 'Peter']

def repeated_name(names: list):
    name_dict = {}
    for name in names:
        if name not in name_dict:
            name_dict[name] = 1
        else:
            if name in name_dict:
                name_dict[name] += 1
        max_value = max(name_dict.values())
        max_name = max(name_dict, key=name_dict.get)
        tuple = (max_name, max_value)
    return tuple


print(repeated_name(names))