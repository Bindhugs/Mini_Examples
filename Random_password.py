#Generating random password 

import random
chars = 'abcdefghijklmnopqrstuvwxyz123456789'
password = ' '

for i in range(5):
    password += random.choice(chars)

print("Password: ",password)