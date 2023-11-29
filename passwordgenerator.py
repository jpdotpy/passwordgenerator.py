import random
import string

length = int(input('Enter Length Of Pass: '))

chars = string.ascii_letters
chars += string.digits
chars += string.punctuation
chars += string.ascii_uppercase

password = " "

for i in range(length):
     password += random.choice(chars)
    

print("Your Password Is:",password)
