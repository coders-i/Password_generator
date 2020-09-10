import string
from random import *
import random
from time import sleep
import os

print("\t\tWelcome To Password Genrator Application")
print("\n\n\tInput Your Needs")
char=int(input("\n\tNumber of Character in Password : " ))
schar=int(input("\n\tNumber of Special Character in Password : "))
num=int(input("\n\tNumber of Integer in Password : "))
pass1="".join(choice(string.digits) for x in range(num))
pass2="".join(choice(string.ascii_letters) for x in range(char))
pass3="".join(choice(string.punctuation) for x in range(schar))
Password=pass1+pass2+pass3
l=list(Password)
random.shuffle(l)
Password="".join(l)
print("\n\tYour Password is : %s"%Password)

op=input("\n\tWant to Copy a Password to Clipboard???(Y/N)")
if(op=="Y" or op=="y"):
	command='echo ' + Password.strip() + '| clip'
	os.system(command)
	print("\n\tCopied Succesfully!!!")

print("\n\tThankyu for using Password Genrator")

sleep(5)
