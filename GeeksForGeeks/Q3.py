'''
Uppercase Half String
'''
def firstHalfCapital(s):
    l = len(s)
    hl = int(0.5*l)
    s = s[:hl].upper() + s[hl:]
    return s

def secondHalfCapital(s):
    l = len(s)
    hl = int(0.5*l)
    s = s[:hl] + s[hl:].upper()
    return s

# initialize test string
test_str = 'geeksforgeeks'

print(firstHalfCapital(test_str))
print(secondHalfCapital(test_str))
