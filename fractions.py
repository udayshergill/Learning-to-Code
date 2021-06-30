def numerator(fraction):
    fraction = str(fraction)
    number = fraction.split("/")
    print("{} is the numerator" .format(number[0]))
    return(int(number[0]))

def denominator(fraction):
    fraction = str(fraction)
    number = fraction.split("/")
    print("{} is the denominator" .format(number[1]))
    return(int(number[1]))

fraction = input("Please provide a fraction I will split\n")

print("The fraction was {}/{}" .format(numerator(fraction), denominator(fraction)))