'''
Python Program to print all Possible Combinations from the three Digits
'''
import itertools as it
#initializing the list
testList = [1, 2, 3]

resList = list(it.permutations(testList , 3))
for i in resList:
    print(i)