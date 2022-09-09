'''
Remove all the occurrences of an element from a list in Python
'''
testList = [1, 1, 2, 3, 4, 5, 1, 2]
rEle = 1

testList = list(i for i in testList if i != rEle)
print(testList)

'''
n = testList.count(rEle)
for i in range(n):
    testList.remove(rEle)
print(testList)
'''