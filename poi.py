def poi(m1,m2,b1,b2):
    import time
    m = m2 - m1
    b = b1 - b2
    if m == 0:
        print("These lines are parrell meaning there is no point of intersection")
        return("Parrell Lines")
    else:
        x = b / m
    print("Find the POI with theses steps\n")
    time.sleep(1.5)
    print("First combine both the formulas by having y1 = y2\n")
    time.sleep(1.5)
    print("It should look like this {} + {}x = {}x + {}\n" .format(b2, m2, m1, b1))
    time.sleep(1.5)
    print("Isolate for x by rearragning the formula into {}x - {}x = {} - {}\n" .format(m2,m1,b1,b2))
    time.sleep(1.5)
    print("Simplify the values into {}x = {}\n" .format(m,b))
    time.sleep(1.5)
    print("divide the {} by {} to get x = {}\n" .format(b,m,x))
    time.sleep(1.5)
    print("Now take the {} and sub it in the orginal equation as x\n" .format(x))
    time.sleep(1.5)
    print("Solve for y in the equation y = {}({}) + {}\n" .format(m1,x,b1))
    time.sleep(1.5)
    y = m1 * x
    y += b1
    print("Your point of interection will be {}, {}\n" .format(x, y))
    time.sleep(5)

eq1 = (input("Please give the first equation in y=mx+b format\n"))
m1start = eq1.find("=") + len("=")
m1end = eq1.find("x")
m1 = int(eq1[m1start:m1end])
finder1 = eq1.find("+")
if finder1 > 0:
    holder1 = (eq1.find("+")) + 1
else:
    holder1 = (eq1.find("-"))
b1 = int(eq1[holder1:len(eq1)])

eq2 = (input("Please give the second equation in y=mx+b format\n"))
m2start = eq2.find("=") + len("=")
m2end = eq2.find("x")
m2 = int(eq2[m2start:m2end])
finder2 = eq2.find("+")
if finder2 > 0:
    holder2 = (eq2.find("+")) + 1
else:
    holder2 = (eq2.find("-")) 
b2 = int(eq2[holder2:len(eq2)])

poi(m1,m2, b1, b2)

input("Press Enter to Close\n")
