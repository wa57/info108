#

def main():
    #WA - Runs the intro function which prints instructions for the user
    intro()

    #WA - Gathers number of cups to be converted from the user
    cups_needed = input('Enter the number of cups: ')

    #WA - Passes the gathered cup input into the cups_to_ounces function
    cups_to_ounces(cups_needed)


#Prints program instructions for the user to the console
def intro():
    print ('This program converts measurements')
    print ('in cups to fluid ounces. For your')
    print ('reference the formula is:')
    print ('    1 cup = 8 fluid ounces')
    print ()

#Uses the cups argument passed in via user input
#Multiplies cups by 8 in order to receive the ounces conversion then outputs the result to the console
def cups_to_ounces(cups):
    ounces = cups * 8
    print ('That converts to', ounces, 'ounces.')

#Runs the main function to start the program
main()
