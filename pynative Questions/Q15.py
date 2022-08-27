'''
Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

Note here exp is a non-negative integer, and the base is an integer.
'''
def exponent(base, exp):
    result = 1
    for i in range(0, exp):
        result = result * base
    print(base, " raises to power of ", exp, " : ", result)


b = int(input("Base = "))
e = int(input("Exponent = "))
exponent(b, e)
