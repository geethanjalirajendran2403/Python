#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))




#Eazy Level - Order not randomised:

#password = ""
#for char in range(1, nr_letters+1):
  #ran_char = random.choice(letters)
  #password = password + ran_char

#password1 = ""
#for char1 in range(1, nr_symbols+1):
  #ran_char1 = random.choice(symbols)
  ##password1 = password1 + ran_char1

#password2 = ""
#for char2 in range(1, nr_numbers+1):
 # ran_char2 = random.choice(numbers)
 # password2 = password2 + ran_char2

#total_password = password + password1 + password2

#print(f"Here is your password:{total_password}")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []
for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

    
random.shuffle(password_list)


password = ""
for char in password_list:
  password += char
print(f"Your password is {password}")  
