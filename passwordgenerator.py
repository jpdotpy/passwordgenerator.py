import random
import string

length = int(input('Enter Length Of Pass: '))

chars = string.ascii_letters
chars += string.digits
chars += string.punctuation
chars += string.ascii_uppercase

mypassword = " "

for i in range(length):
     mypassword += random.choice(chars)
    

print("Your Password Is:",mypassword)
