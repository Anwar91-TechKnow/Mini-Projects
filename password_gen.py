import string
import random
import time

def method1():
    s1 = string.ascii_uppercase
    # print(s1)
    s2 = string.ascii_lowercase
    # print(s2)
    s3 = string.digits
    # print(s3)
    s4 = string.punctuation
    # print(s4)
    plen = plen1
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # print(s)
    random.shuffle(s)
    # print(s)
    print(" Your Password by method 1 ")
# now we are taking random number same as user provided number
    print("".join(s[0:plen]))

def method2():
    s1 = string.ascii_uppercase
    # print(s1)
    s2 = string.ascii_lowercase
    # print(s2)
    s3 = string.digits
    # print(s3)
    s4 = string.punctuation
    # print(s4)
    plen = plen1
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # print(s)
    print(" Your Password by method 2 ")
# now we are taking random number same as user provided number
    # at second way you dont need to use random.shuffle so instead of that you need to
    print("".join(random.sample(s, plen)))



plen1= int(input("Enter your desired password length : "))
choice = int(input("Enter 1 for method first and 2 for seocond method "))
if choice==1:
    print(method1())
    time.sleep(5)
elif choice==2:
    print(method2())
    time.sleep(5)
else:
    print("Please use correct method")




