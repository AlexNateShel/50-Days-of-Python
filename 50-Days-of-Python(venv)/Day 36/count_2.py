# Write a function called 'count' that takes one argument, a string and returns a dictonary of how many times each element appears in the string.
# For example, 'hello' should return:
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}

def count(str1):
    d = {}
    for i in range(len(str1)):
        x = str1[i]
        count = 0
        for j in range(i, len(str1)):
            if str1[j] == str1[i]:
                count += 1
        countz = dict({x: count})
        if x not in d.keys():
            d.update(countz)
    return d

print(count('hello'))