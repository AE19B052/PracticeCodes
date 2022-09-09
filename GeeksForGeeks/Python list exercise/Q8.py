'''
Python program to select Random value form list of lists
'''
import random

#initializing List
test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]

# randomly choosing index number of list
r_no = random.randint(0, len(test_list) - 1)

# randomly choosing element of that index number list
rChoosen = random.choice(test_list[r_no])

print(rChoosen)