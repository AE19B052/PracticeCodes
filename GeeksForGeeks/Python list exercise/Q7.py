'''
Problem --> Find Uncommon elements in Lists of List
'''

#initializing lists
test_list1 = [ [1, 2], [3, 4], [5, 6] ]
test_list2 = [ [3, 4], [5, 7], [1, 2] ]
#here we are going to use sets fuctions so we will create sets. But set take hashable type so we will convert all the inner list to tuple using map  
test_set1 = set(map(tuple, test_list1))
test_set2 = set(map(tuple, test_list2))

# '^' is a bitwise operator of name XOR. This is used here to find uncommon elements
uncommonElementSet = test_set1 ^ test_set2
uncommonElementList = list(map(list, uncommonElementSet))

print("Uncommon Elements of list :- ", test_list1 ,"\n and list :- ", test_list2 , "\n is ", uncommonElementList)