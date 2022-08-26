'''
Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.
'''

number1 = int(input("number1 = "))
number2 = int(input("number2 = "))

if (number1*number2 <= 1000):
    print(f"Result is {number1*number2}")
else:
    print(f"Result is {number1+number2}")
