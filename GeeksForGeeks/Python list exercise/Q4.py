'''
Sum of number digits in List
'''
import numpy as np

#function to find sum of digits
def sumOfDigit(a):
    a = int(a)
    l = 1 + int(np.log10(a))
    sum0 = 0
    for i in range(0, l):
        r = a%10
        a = int(a/10)
        sum0 = r + sum0
    return sum0
         

test_list = [12, 67, 98, 34]

#using list comprehension to form a list which contains sum of digits
test_list = list(sumOfDigit(i) for i in test_list)
print(test_list)