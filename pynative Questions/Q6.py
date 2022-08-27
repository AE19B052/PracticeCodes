'''
Iterate the given list of numbers and print only those numbers which are divisible by 5
'''
giveList = [10, 20, 33, 46, 55]
l = list.__len__(giveList)
print(f"Given list is {giveList} \nDivisible by 5")
for i in range(l):
    if giveList[i]%5 == 0:
        print(giveList[i])