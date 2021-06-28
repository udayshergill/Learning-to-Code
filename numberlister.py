import time
print("Hello I will list all the numbers before the number you give me\n")
time.sleep(1.25)
def numberlister(x):
    x = int(x)
    holder = x
    while(x > 0):
        x -= 1
        print(x)
        time.sleep(0.5)
    reverse = input("Would you like to list the reverse order?\n")
    if reverse == "yes":
        while x!= holder:
            print(x)
            time.sleep(0.5)
            x += 1
        return(print("Have a good day"))
    elif reverse == "no":
        return(print("Goodbye"))

numberlister(input("What number would you like to start from\n"))
