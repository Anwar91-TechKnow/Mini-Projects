#calculator of items:
import time

sum = 0
while True:

    def optiona():
        price = input("Enter the price of an iteam or say Quit : \n")
        if price != "Quit":
            sum = Price+int(price)
            print("The sum of your items so far", sum)
        else:
            print("Thank you for shopping with us")
            print("your Total bill is: ", sum)


    # second example where continue and break both used:
    def optionb():
        while (True):
            inp = int(input("Enter The Number"))
            if inp > 100:
                print("Congracts you have entered number greater than 100")
                break
            else:
                print("Try Again")
                continue

    option =int(input("Please Select your option 1 or 2 "))
    if option==1:
        optiona()
        time.sleep(10)
    else:
        optionb()
        time.sleep(10)

