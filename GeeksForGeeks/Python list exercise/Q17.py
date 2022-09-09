'''
Replace index elements with elements in Other List
'''


test_list1 = ['Gfg', 'is', 'best']
test_list2 = [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]

L1 = list(test_list1[i] for i in test_list2)
print(L1)