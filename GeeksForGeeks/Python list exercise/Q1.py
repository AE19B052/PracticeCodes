'''
python program to interchange first and last elements in a list
'''

#defining a function to swap 2 elements in list
def swapElement(list0 , a , b):
    i = list0[a]
    list0[a] = list0[b]
    list0[b] = i
    return list0

#since in this code we are swapping first and last element we will write a = 0 & b = -1

#some test cases
list_1 = [12, 35, 9, 56, 24]
list_2 = [1, 2, 3]

#calling function and printing final list
print(swapElement(list_1, 0, -1))
print(swapElement(list_2, 0, -1))