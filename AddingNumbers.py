import time
numberint = int(0)
print("Hello I will be adding your numbers\n")
time.sleep(0.5)
numberamount = int(input("How many numbers are you adding?\n"))
time.sleep(0.5)
while numberamount>0:
    newnumber = int(input("What is the number you want to add\n"))
    time.sleep(0.1)
    numberint += newnumber
    numberamount -= 1
print("Your number is " + str(numberint))
