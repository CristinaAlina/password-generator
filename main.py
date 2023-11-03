#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

generated_pass = ''
for letter in range(0, nr_letters):
    generated_pass += random.choice(letters)

for symbol in range(0, nr_symbols):
    generated_pass += random.choice(symbols)

for number in range(0, nr_numbers):
    generated_pass += random.choice(numbers)

print(f'Your password is: {generated_pass}')

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# Using loops

generated_pass = []
for letter in range(0, nr_letters):
    generated_pass.append(random.choice(letters))

for symbol in range(0, nr_symbols):
    generated_pass.append(random.choice(symbols))

for number in range(0, nr_numbers):
    generated_pass.append(random.choice(numbers))

print(generated_pass)
random.shuffle(generated_pass)
print(generated_pass)

password = "".join(generated_pass)
print(f'Your password is: {password}')

# Using choices() function - without loop (introduced in Python 3.6)
generated_pass = []

generated_pass.extend(random.choices(letters, k=nr_letters))

generated_pass.extend(random.choices(symbols, k=nr_symbols))

generated_pass.extend(random.choices(numbers, k=nr_numbers))

print(generated_pass)
random.shuffle(generated_pass)
print(generated_pass)

password = "".join(generated_pass)
print(f'Your password is: {password}')
