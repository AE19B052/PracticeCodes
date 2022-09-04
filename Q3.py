'''
Reversing a List in Python
'''
#defining funtion to swap two elements in list
def swapList( list0,a, b):
    i = list0[a]
    list0[a] = list0[b]
    list0[b] = i

#deifing function to reverse list
def reverseList(list0):
    l = len(list0)
    n = int(l/2)
    for j in range(0,n):
        swapList(list0,j,(-j-1))    #swaping j and n-1-j element
    return list0

list_1 = [3, 4, 5, 6, 7, 8, 9]
#using defined function for print final result
print(reverseList(list_1))