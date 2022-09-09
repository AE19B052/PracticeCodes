#initializing testlist
test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3

uniqueElementList = list(set(test_list))

res = []
for i in uniqueElementList:
    if test_list.count(i) >= k :
        res.append(i)

'''
dict1 = {}
for i in test_list:
    if i not in dict1.keys():
        dict1[i] = 1
    else:
        dict1[i] = dict1[i] + 1

res = []
for i in dict1.keys():
    if dict1[i] >= k:
        res.append(i)
'''
print(res)