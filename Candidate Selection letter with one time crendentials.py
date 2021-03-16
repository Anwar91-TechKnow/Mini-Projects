#             ANWAR SHAIKH
#             Python program set2/012
#             Title: Print letter with dynamic values.
'''This program help us to generate letter with dynamic input with hardcoded
format.
============================================================
''' 
# Please commentout the rest approches and use only one approch at the time of execution. 
#Firt approch

# by using this programme you can generate
#dyanmic letter 
#One time password and User name for candidate.

import string
import random

s1 = string.ascii_uppercase
s2 = string.ascii_lowercase
plen = 8
s = []
s.extend(list(s1))
s.extend(list(s2))
random.shuffle(s)
usr=("".join(s[0:plen]))


P3 = string.digits
P4 = string.punctuation
plen = 8
P = []
P.extend(list(P3))
P.extend(list(P4))
pwd=("".join(random.sample(P, plen)))

offerletter = ''' Dear, <|NAME|> 

This is to inform you that, you have been selected in our company (XYZ Inc)
as 'Software Tester' from the date which you agreed.
we have provided you one time login details kindly setup your account with us.
URL:xyx.career@help.com

Date: <|DATE|>
Full Name: <|FULLNAME|>
Login ID: <|USN|>
Password: <|PWD|>

Thanks,
XYZ Inc.
India.
'''
name=input("Enter your Employee Name: ")
fullname= input("Enter Employee Full Name: ")
date=input("Enter offer Date: ")

offerletter=offerletter.replace("<|NAME|>",name)
offerletter=offerletter.replace("<|FULLNAME|>",fullname)
offerletter=offerletter.replace("<|DATE|>",date)
offerletter=offerletter.replace("<|USN|>",usr)
offerletter=offerletter.replace("<|PWD|>",pwd)
print(offerletter)

print(
"Details for Admin Team:",
"Full Name: ",fullname,
"UserName: ",usr,
"Password: ",pwd)
