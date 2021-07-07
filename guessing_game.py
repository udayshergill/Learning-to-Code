userin = int(input("Guess a number from 0-100\n"))

def game(userin):
    import random
    number = int(random.randint(0,101))
    holder1 = 0
    holder2 = 100
    max = 100
    min = 0
    while userin != number:
        if userin > number:
            while userin > number:  
                print("Your number is too big\n")
                if userin > holder1:
                    max = userin
                    holder1 = userin
                userin = int(input("Try between {} - {}\n" .format(min+1, userin-1)))
               
        if userin < number:
            while userin < number:  
                print("Your number is too small\n")
                if userin < holder2:
                    min = userin
                    holder2 = userin
                if userin > holder2:
                    if userin>min:
                        min = userin              
                userin = int(input("Try between {} - {}\n" .format(userin+1, max-1)))                
    else: 
     print("Congrats thats the number!\n")
game(userin) 
input("Press Enter to exit\n")