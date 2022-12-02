'''
Tip Calculator

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
'''
print("Welcome to Tip Calculator")
# take intial total bill
bill = float(input("Enter the total Bill amount: "))
# asking customer the percentage og tip
tip_percentage = float(input("Enter the percentage of Total Bill you want to give as tip: "))
tip_factor = tip_percentage/100
# asking how many people are spliting the bill
people = float(input("Enter the number of people spliting the bill: "))
# Calculating the Total bill with tip
total_bill = bill * (1 + tip_factor)
# Calculating how much each person will pay
each_person = total_bill/people
#rounding of to 2 decimal places
'''
final_amount_each_person = round(each_person, 2)
if we use above, there was a formaing problem
'''
final_amount_each_person = "{:.2f}".format(each_person)

print(f"Each person should pay: {final_amount_each_person}")
