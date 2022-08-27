'''
Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.
'''


def checkFirstAndLast(list):
    print(f"Given list: {list}")
    if list[0] == list[-1]:
        print("result is true")
    else:
        print("result is false")
    return 0


list1 = [10, 20, 30, 40, 10]
list2 = [75, 65, 35, 75, 30]
checkFirstAndLast(list1)
checkFirstAndLast(list2)
