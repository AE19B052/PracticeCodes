'''
Create a new list from a two list using the following condition

Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.
'''
def oddNumberSelection(list):
    a = []
    for i in range(0 , len(list)):
        if list[i]%2 == 1:
            a.append(list[i])
    return a

def evenNumberSelection(list):
    a = []
    for i in range(0 , len(list)):
        if list[i]%2 == 0:
            a.append(list[i])
    return a

def finalList(list_1,list_2):
    fList = oddNumberSelection(list_1) + evenNumberSelection(list_2)
    return fList

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print(finalList(list1, list2))