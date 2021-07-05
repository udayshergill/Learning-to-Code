import time
def cost(numd, wood):
  if (wood == "oak"):
    if (numd == 3 or numd < 3):
      print("The Oak Desk cost 200 Dollars\n")
      return 200
    elif (numd > 3):
      oakamount = numd - 3 
      oakamount = oakamount* 25
      oakamount = oakamount + 200
      print("The Oak Desk cost {} Dollars\n" .format(oakamount))
      return oakamount
  if (wood == "mohagany"):
   if (numd == 3 or numd < 3):
     print ("This Mohagany Desk costs 300 Dollars\n")
     return 300
   elif(numd > 3):
     mohaganyamount = numd - 3
     mohaganyamount = mohaganyamount * 45
     mohaganyamount = mohaganyamount + 300
     print("This Mohagany Desk costs {} Dollars\n" .format(mohaganyamount))
     return mohaganyamount
  if (wood == "hickory"):
    if (numd == 3 or numd < 3):
     print("This Hickory desk costs 400 Dollars\n")
     return 400
    elif(numd > 3):
     hickoryamount = numd -3
     hickoryamount = hickoryamount * 60
     hickoryamount = hickoryamount + 400
     print("The cost of this Hickory desk is {} Dollars\n" .format(hickoryamount))
     return hickoryamount

print("Hello I will caculate the cost of your desk with your given parameters\n")
time.sleep(1.25)
numd = int(input("How many drawers would you want?\n"))
time.sleep(1.25)
wood = input("Would you like an oak, mohagany, or hickory desk?\n")
time.sleep(1.25)
cost(numd, wood)

input("Press enter to close\n")