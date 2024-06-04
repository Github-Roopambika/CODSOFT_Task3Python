# Program to create a password generator by Roopambika Mohanty
import random
import string

Characters = string.ascii_letters + string.digits + string.punctuation 
length= int(input("\nEnter the desired length of the password\n"))
password_str=""
for i in range(length):
  password_str += random.choice(Characters)

print("The generated password is" , password_str)