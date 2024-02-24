# Write a function called 'save_json'.
# This function takes a dictionary as an argument and saves it on a file in JSON format.

# Write another function called 'read_json' that opens the file that you just saved and reads its content.
# Use the function below as an argument.
# names = {'name': 'Carol', 'sex': 'female', 'age': 55}


import json

names = {'name': 'Carol', 'sex': 'female', 'age': 55}

# first function

def save_json(dict1):
    with open('file.json', 'w') as my_file:
        # saving the file and adding indentation
        json.dump(dict1, my_file, indent=4)


save_json(names)

# second function

def read_json():
    with open('file.json', 'r') as my_file:
        json_file = json.load(my_file)
    return json_file

print(read_json())