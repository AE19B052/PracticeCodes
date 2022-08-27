'''
Calculate income tax for the given income by adhering to the below rules

Taxable Income	Rate (in %)

First $10,000	0
Next $10,000	10
The remaining	20
'''

def incomeTax(income):
    if income <= 10000:
        print("Income Tax = 0")
    elif income <= 20000:
        a = income - 10000
        print("Income Tax = ", a*0.1)
    else:
        a = income - 20000
        print("Income Tax = ", (a*0.2) + 1000)
    return 0


Income = int(input("Enter Taxable Income "))
incomeTax(Income)
