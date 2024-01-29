#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Create easy level password string
easy_password = ""

#loop for generating random letters
for char in range(0, nr_letters):
  random_char = random.choice(letters)
  easy_password += random_char

#loop for generating random symbols
for symb in range(0, nr_symbols):
  random_symb = random.choice(symbols)
  easy_password += random_symb

#loop for generating random numbers
for num in range(0, nr_numbers):
  random_num = random.choice(numbers)
  easy_password += random_num

#Print password to console
print(f"Your password is: {easy_password}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#Create list for storing password characters
password_list = []
#Create password string
hard_password = ""

#loop for generating random letters
for char in range(0, nr_letters):
  random_char = random.choice(letters)
  password_list.append(random_char)

#loop for generating random symbols
for symb in range(0, nr_symbols):
  random_symb = random.choice(symbols)
  password_list.append(random_symb)

#loop for generating random numbers
for num in range(0, nr_numbers):
  random_num = random.choice(numbers)
  password_list.append(random_num)

#Shuffle the characters stored within the password list
random.shuffle(password_list)

#Add each character in the shuffled password list to the hard password string in their new order
for count in range(0, len(password_list)):
  hard_password += password_list[count]

#Print password to console
print(f"Your password is: {hard_password}")