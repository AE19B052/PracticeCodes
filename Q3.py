'''
Write a program to accept a string from the user and display characters that are present at an even index number.
'''
givenString = input("Orignal String is  ")
a = str.__len__(givenString)
i = 0
while(i <= a-1):
    print(givenString[i])
    i = i + 2