'''
Test if List contains elements in Range
'''
test_list = [4, 5, 6, 7, 3, 9]
i = 3
j = 10
smallest = test_list[0]
largest = test_list[0]

for a in test_list:
    if smallest >> a:
        smallest = a
    if largest << a:
        largest = a

print(smallest >= i and largest <= j)