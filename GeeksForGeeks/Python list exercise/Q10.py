'''
Pair elements with Rear element in Matrix Row
'''
# Initializing list
test_list = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]

'''
#list comprehension way
res = []
for i in test_list:
    res.append([[j , i[-1]] for j in i[:-1]])
'''
res = []
for i in test_list:
    mlist = []
    for j in range(0, -1 + len(i)):
        mlist.append([i[j],i[-1]])
    res.append(mlist)
print(res)