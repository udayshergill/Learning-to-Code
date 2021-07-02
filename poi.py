def poi(m1,m2,b1,b2):
    m = m2 - m1
    b = b1 - b2
    if m == 0:
        print("These lines are parrell meaning there is no point of intersection")
        return("Parrell Lines")
    else:
        x = b / m
    print("Find the POI with theses steps\n")
    print("First combine both the formulas by having y1 = y2\n")
    print("It should look like this {} + {}x = {}x + {}\n" .format(b2, m2, m1, b1))
    print("Isolate for x by rearragning the formula into {}x - {}x = {} - {}\n" .format(m2,m1,b1,b2))
    print("Simplify the values into {}x = {}\n" .format(m,b))
    print("divide the {} by {} to get x = {}\n" .format(b,m,x))
    print("Now take the {} and sub it in the orginal equation as x\n" .format(x))
    print("Solve for y in the equation y = {}({}) + {}" .format(m1,x,b1))
    y = m1 * x
    print(y)
    y += b1
    print("Your point of interection will be {}, {}" .format(x, y))

eq1 = (input("Please give the first equation is y=mx+b format\n"))
m1start = eq1.find("=") + len("=")
m1end = eq1.find("x")
m1 = int(eq1[m1start:m1end])
holder1 = (eq1.find("+")) + 1
b1 = int(eq1[holder1:len(eq1)])

eq2 = (input("Please give the second equation is y=mx+b format\n"))
m2start = eq2.find("=") + len("=")
m2end = eq2.find("x")
m2 = int(eq2[m2start:m2end])
holder2 = (eq2.find("+")) + 1
b2 = int(eq2[holder2:len(eq2)])

poi(m1,m2, b1, b2)