'''
Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.
'''
#asking for first number
number1 = int(input("number1 = "))
#asking for second number
number2 = int(input("number2 = "))
#Stating conditions
if (number1*number2 <= 1000):
    print(f"Result is {number1*number2}")   #if product is less than or equal to 1000 then printing product
else:ing
    print(f"Result is {number1+number2}")   #if product is greater than 1000 then printing sum
