'''
Check Palindrome Number
'''
number = input("Enter a number")

if type(int(number)) == int:
    # input is in string form, kept that way
    reverse_number = number[::-1]
    if reverse_number == number:
        print("Yes. given number is palindrome number")
    else:
        print("No. given number is not palindrome number")
else:
    print("invalid input")
