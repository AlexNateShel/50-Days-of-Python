# You have a nest dictionary below. 
# Write a function called 'sum_nested_dict', that takes one argument, a dictionary, and returns the sum of all the values in the dictionary.
# The nested dictionary below, should return 15.

nested_dict = {'a': 1, 'b': {'c': 2, 'd': {'e': 3, 'f': 4}}, 'g': 5}

def sum_nested_dict(nested_dict: dict):
    total = 0
    for value in nested_dict.values():
        if isinstance(value, dict):
            total += sum_nested_dict(value)
        else:
            total += value
    return total

print(sum_nested_dict(nested_dict))