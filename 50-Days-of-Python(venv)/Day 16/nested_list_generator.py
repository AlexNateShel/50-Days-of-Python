nested_list = [[12, 34, 56, 67], [34, 68, 78]]

# Write a code that generates a list of the following numbers from the nested list above:
# 34, 67, 78
# Your output should be another list: [34, 67, 78]. The list output should not have duplicates.

new_list = []
for list1 in nested_list:
    for num in list1:
        if num in [34, 67, 78]:
            if num not in new_list:
                new_list.append(num)

print(new_list)