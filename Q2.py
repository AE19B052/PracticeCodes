'''
Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
'''

print("Printing current and previous number sum in a range(10)")

previousNumber = 0
i = 0
for i in range(10):
    print(
        f"Current Number {i} Previous Number  {previousNumber}  Sum:  {i + previousNumber}")
    previousNumber = i
    i += 1
