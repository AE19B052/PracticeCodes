'''
Print downward Half-Pyramid Pattern with Star
* * * * *  
* * * *  
* * *  
* *  
*
'''
i = 5
j = 0
while i > 0:
    for j in range(i):
        print("*", end=" ")
    i = i - 1
    print(" ")