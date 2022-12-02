'''
Python program to capitalize the first and last character of each word in a string
'''


def firstAndLastCapital(s):
    s = s[0].upper() + s[1:-1] + s[-1].upper()
    return s


test_str = "welcome to geeksforgeeks"
a = test_str.split(' ')
res = []
for i in a:
    res.append(firstAndLastCapital(i))
res = " ".join(res)
print(res)
