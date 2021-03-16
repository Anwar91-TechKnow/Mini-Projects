'''                    PYTHON LEARNING ACTIVIY
                    Learning Python by :ANWAR SHAIKH
                Welcome to Python programming All the best !!!!
'''


#1.Here we are taking two numbers form User
#2.Giving user choice to select any of the option 
#3.As per user chocice will execute the same and will show the results

import time
print("Welcome to my Peronalised Calculator: ANWAR SHAIKH")
sum=0
while True:
    # try:
        a=int(input("Enter First number = "))
    #     print(a)
    # except ValueError:
    #     print("Ops !! not a Number")
    # try:
        b=int(input("Enter Second number = "))
    #     print(b)
    # except ValueError:
    #     print("Ops !! not a Number")

        option=input("Select the function which you want use from given list:Sum,dedcution, division, mulfication = ")
        if option=="sum":
            sum=a+b
            print("The Sum of two given digit is = ",sum)
            time.sleep(20)
        elif option=="dedcution":
            c=a-b
            print("The dedcution of two given digit is = ",c)
            time.sleep(10)
        elif option=="division":
            d=a/b
            print("The division of two given digit is = ",d)
            time.sleep(10)
        elif option=="multification":
            e=a*b
            print("The mulfication of two given digit is = ",e)
            time.sleep(10)
        else:
            print("  Error Code:D44rd >>>>>>>Please use correct option<<<<<<<  ")
            continue
