'''
Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.
'''
# defining a function to swap 2 elements in list


def swapElement(list0, a, b):
    i = list0[a]
    list0[a] = list0[b]
    list0[b] = i
    return list0


# taking input form user
inputString = input('Enter elements of list seprated by space : ')
list_1 = inputString.split()  # list created

# taking input to ask which element to interchange
a = int(input("enter numbers you want to interchange, first element postion = "))
b = int(input("second element postion = "))

# calling function and printing final list
print(swapElement(list_1, a-1, b-1))
