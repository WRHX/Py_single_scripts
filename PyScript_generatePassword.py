import random
import string
import numpy
import pyperclip

a_uc = list(string.ascii_uppercase) #create list with uppercase alphabet
a_lc = list(string.ascii_lowercase) #create list with lowercase alphabet
numbers = [0,1,2,3,4,5,6,7,8,9]

container = [a_uc,a_lc,numbers]

length = int(input('Enter the number of characters you want your password to be:'))
password = [None]*(length)

for n in range(0,(length)):
    q = random.randint(0,2)
    if q == 0 or q==1:
        element = random.randint(0,25)
        password[n] = str(container[q][element])
    elif q==2:
        element = random.randint(0,9)
        password[n] = str(container[q][element])
pyperclip.copy("".join(password))
print("".join(password))
print("The password is copied to the clipboard. Press Ctrl + V to paste it.")
input()




