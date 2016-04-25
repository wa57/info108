#Project Name: Lab 3 Problem 2
#Date: 4/13/16
#Programmer Name: Will Ashman
#Project Description: Program to determine if a number is divisible via logical operators

def main():
    #WA - Gathers user input and converts to integer
    number = int(input('Enter a number: '))
    print()

    #WA - Passes integer into determination functions
    determineAnd(number)
    determineOR(number)

    print()
    input('Press Enter to continue...')

#WA - Checks if the input integer is divisible by 5 AND 6 using the logical and operator
def determineAnd(number):
    if isDivisible(number, 5) and isDivisible(number, 6):
        print(number, 'is divisible by 5 and 6.')
    else:
        print(number, 'is not divisible by 5 and 6.')

#WA - Checks if the input integer is divisble by 5 OR 6 using the logical or operator
def determineOR(number):
    if isDivisible(number, 5) or isDivisible(number, 6):
        print(number, 'is divisible by 5 or 6.')
    else:
        print(number, 'is not divisible by 5 or 6.')

#WA - Helper function using modulo to determine if there is no remainder, therefore completely divisible
def isDivisible(dividend, divisor):
    return (dividend % divisor) == 0

main()
