'''
Problem --> Convert lists of list to Dictionary
'''

# initializing list
test_list = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]

newDic = {}
for miniList in test_list:
    a = tuple(miniList[0:2])    #taking first two element and making them tuple
    b = tuple(miniList[2:])     #taking other two element and making them tuple
    newDic[a] = b   #here we are adding new item in dictionary

'''
can be written in shorter form

for miniList in test_list:
    newList[tuple(miniList[0:2])] = tuple(miniList[2:])
'''

print(newDic)
