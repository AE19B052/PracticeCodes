'''
Python – Reverse Row sort in Lists of List
'''
# initializing list
test_list = [[4, 1, 6], [7, 8], [4, 10, 8]]

def reverseSort(list1):
    list1.sort()
    list1.reverse()
    return list1

#result List
'''resList = list(reverseSort(i) for i in test_list)'''
resList = list(map(reverseSort, test_list))
print(resList)