'''
Python program to check whether the string is Symmetrical or Palindrome
'''

#defining a function which checks and tell us if string is symmertic or not
def sym(str0):
    sLen = len(str0)
    halfLen = int(sLen/2)
    if sLen % 2 == 0:
        firstHalf = str0[:halfLen]
        secondHalf = str0[halfLen:]
    else:
        firstHalf = str0[:halfLen]
        secondHalf = str0[halfLen+1:]
    if firstHalf == secondHalf:
        print(str0, " , String is symmertical")
    else:
        print(str0, " , String is non-symmertical")

#defining a function which checks and tell us if string is palindrome or not
def pal(str0):
    sLen = len(str0)
    halfLen = int(sLen/2)
    if sLen % 2 == 0:
        firstHalf = str0[:halfLen]
        secondHalf = reversed(str0[halfLen:])
    else:
        firstHalf = str0[:halfLen]
        secondHalf = reversed(str0[halfLen+1:])
    if firstHalf == secondHalf:
        print(str0, " , String is palindrome")
    else:
        print(str0, " , String is non-palindrome")


testString = 'khokkho'
sym(testString)
pal(testString)
