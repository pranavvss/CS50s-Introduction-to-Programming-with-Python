# implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer
#then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.
# If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
#And if 99% or more remains, output F instead to indicate that the tank is essentially full.
#If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.

def display(fuel_percent):
    if fuel_percent >= 99:
        return "F"
    elif fuel_percent <= 1:
        return "E"
    else:
        return f"{fuel_percent}%"

def main():
    while True:
        try:
            fuel_fraction = input("How much fuel is left? (input as a fraction): ")
            numerator, denominator = map(int, fuel_fraction.split('/')) # maps as integers
            if numerator > denominator  or denominator <= 0:
                raise ValueError
            fuel_percent = int(round(numerator/denominator * 100))
            print(display(fuel_percent))
            break
        except(ValueError, ZeroDivisionError):
            pass

if __name__ == '__main__':
    main()




