'''
Python program to print even length words in a string
'''
# function which prints string if its length is even
def evenLenWord(s):
    s = list(s.split(' '))
    for i in s:
        if len(i) % 2 == 0:
            print(i)
    return 0

#Test String
testString = "This is a python language"

evenLenWord(testString)