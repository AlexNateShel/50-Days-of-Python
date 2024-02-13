# You want to implement code that will search for a number in a range.
# You have a decision to make as to whether to store the number in a set or a list.
# Your decision will be based on time.
# You have to pick a data type that executes faster.

# You have a range, and you can either store it in a set or a list, depending on which one executes faster when you are searching for a number in the range. 
# See below:
# a = range(10000000)
# x = set(a)
# y = list(a)
# Let's say you are looking for the number 9999999 in the range above.
# Search for this number in the list 'x' and the set 'y'.
# Your challenge is to find which code executes faster. 
# You will select one that executes fastest between lists and sets.
# Run searches and time them.

import timeit

set_test = '''
a = range(1000000)
b = set(a)
i = 999999
i in b
'''
set_search_time = timeit.timeit(stmt=set_test, number=1000)

list_test = '''
a = range(1000000)
b = list(a)
i = 999999
i in b
'''
list_search_time = timeit.timeit(stmt=list_test, number=1000)

print('Set Search Time:', set_search_time)
print('List Search Time:', list_search_time)

# Output
# Set Search Time: 57.97915690000082
# List Search Time: 24.500165500001458