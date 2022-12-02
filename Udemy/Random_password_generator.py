'''
Random PASSWORD Generator
'''
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Length of the password
password_length = int(input("Enter the length of password you wanna generate: "))
#Number of Symbols in password
number_of_symbols = int(input("Enter the number of Symbols you want in password: "))
#Number of Numbers in password
number_of_numbers = int(input("Enter the number of numbers you want in password: "))
#Number of Letters in password
number_of_letters = password_length - number_of_numbers -number_of_symbols

#Choosing elements of password
password = []
for i in range(0,number_of_letters):
    password.append(random.choice(letters))
for i in range(0, number_of_symbols):
    password.append(random.choice(symbols))
for i in range(0, number_of_numbers):
    password.append(random.choice(numbers))

#Randomizing the order of password
random.shuffle(password)

#code for printing password in string form
str1 = ""
print(str1.join(password))