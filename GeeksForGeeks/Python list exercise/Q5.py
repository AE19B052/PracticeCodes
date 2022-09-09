'''
Convert List to List of dictionaries
'''

test_list = ['Gfg', 3, 'is', 8]
key_list = ['name', 'id']
lengthOfList = len(test_list)

new_list = []   #defining new list to store dictionaries
for i in range(0, lengthOfList, 2):
    new_list.append({key_list[0] : test_list[i], key_list[1] : test_list[i + 1]})
print(new_list)