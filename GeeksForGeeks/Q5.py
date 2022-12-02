'''
Python program to check if a string has at least one letter and one number
'''
letter = False
number = False

testString = 'welcome2ourcountry34'

for i in testString:
    if i.isalpha():
        letter = True
    if i.isdigit():
        number = True

print(letter and number)
