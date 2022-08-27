'''
 Write a Program to extract each digit from an integer in the reverse order
'''
import numpy as np
number = int(input("Enter the number "))
if number == 0:
    print("0")
else:
    l = int(1 + np.log10(abs(number)))   #l tells us what digit number is given
    number = str(number)
    for i in range(l):
        print(number[-i-1], end=" ")