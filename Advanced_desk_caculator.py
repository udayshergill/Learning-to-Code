
import time
print("Hello I will calculate the cost of your new desk\n")
time.sleep(1)
wood = str(input("Please provide the wood you want from the three options\nOak, Mohagany, or Hickory\n"))
numd = int(input("Please provide how many drawers you would like\n"))
def run_program(wood, numd):
  getwood(wood, numd)

def getwood(wood, numd):
  if (wood == "Oak"):
    w = wood
    print("Your wood type is {}" .format(w))
  elif (wood == "Mohagany"):
    m = wood
    print("Your wood type is {}" .format(m))
  elif (wood == "Hickory"):
    h = wood
    print("Your wood type is {}" .format(h))
  getdrawers(numd, wood)

def getdrawers(numd, wood):
  print("You have {} drawers" .format(numd))
  math(numd, wood)

def math(numd,wood):
  if (wood == "Oak"):
    if (numd == 3):
      print("The Oak Desk cost 200 Dollars")
    elif (numd > 3):
      o = numd - 3 
      o *= 25
      o += 200
      print("The Oak Desk cost {}" .format(o))
    elif (numd < 3):
      i = numd * 25
      i += 125
      print("The Oak Desk cost {}" .format(i))
  if (wood == "Mohagany"):
   if (numd == 3):
     print ("This Mohagany Desk costs 300 Dollars")
   elif(numd > 3):
     m = numd - 3
     m *= 45
     m += 300
     print("This Mohagany Desk costs {}" .format(m))
   elif(numd < 3):
      n = numd * 45
      n += 165
      ("The Mohagany Desk cost {}" .format(n))
  if (wood == "Hickory"):
    if (numd == 3):
     print("This Hickory desk costs 400 Dollars")
    elif(numd > 3):
     h = numd -3
     h *= 60
     h += 400
     print("The cost of this Hickory desk is {}" .format(h))
    elif(numd < 3):
      g = numd * 60
      g += 220
      ("The Hickory Desk cost {}" .format(g))
  print("Thank You\n")
  
run_program(wood,numd)
time.sleep(1)
input("Press enter to close")