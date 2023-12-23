import random
lowercase = []
for letters in range(ord('a'), ord('z') + 1):
    lowercase += chr(letters)

uppercase = []
for letters in range(ord('A'), ord('Z') + 1):
    uppercase += chr(letters)
letters_upper_lower = lowercase + uppercase
print("WELCOME TO PASSWORD GENERATOR\n")

symbols_string = ['!', '#', '$', '%', '&', '*', '/', '@', '^', '<', '>', '|', '?', '(', ')', '[', ']', '~']

numbers_string = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

letters = input("Enter how many letters you want in your password: ")
letters = int(letters)
symbols = input("Enter how many symbols you want in your password: ")
symbols = int(symbols)
numbers = input("Enter how many numbers you want in your password: ")
numbers = int(numbers)
print("\n")

password1 = ""
for i in range(0,letters):
    char = random.choice(letters_upper_lower)
    password1 += char
#print(password1)

password2 = ""
for i in range(0,symbols):
    symbol = random.choice(symbols_string)
    password2 += symbol
#print(password2)

password3 = ""
for i in range(0,numbers):
    num = random.choice(numbers_string)
    password3 +=  num
#print(password3)

concat_password = password1 + password2 + password3
print(concat_password)
