'''
How to count unique values inside a list
'''
'''
# taking an input and making it list
inputString = input("enter element of number list with space between them : ")
inputList = inputString.split(" ")
'''

# initailizing testList
testList = [1, 2, 2, 5, 8, 4, 4, 8]
covertedSet = set(testList)
print(len(covertedSet))