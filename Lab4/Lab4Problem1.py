#Project Name: Lab 4 Homework
#Date: 4/28/16
#Programmer Name: Will Ashman
#Project Description: Lab 4 Homework
#Resource used for table formatting: http://knowledgestockpile.blogspot.com/2011/01/string-formatting-in-python_09.html

#WA - Import the math module to perform calculations
import math

def main():
    #WA - Get and validate user input
    loanAmount = getInput('\nEnter the amount of the loan (number greater than 0): ')
    loanYears = getInput('\nEnter the number of years as an integer: ')

    #WA - Pass input into calculateLoanPayments to be calculated
    calculateLoanPayments(loanAmount, loanYears)

    #WA - Asks user if they want another table to be created. If y is entered, main is rerun
    createAnotherTable = input('\nDo you want to create another table? (y/n): ')
    if(createAnotherTable == 'y'):
        main()

def calculateLoanPayments(loanAmount, loanYears):
    #WA - Uses replacement fields to set a maximum column width and left align column headers
    print('\n{0:<8} {1:<18} {2:<16}'.format('Rate', 'Monthly Payment', 'Total Payment'))
    print('-'*46)

    #WA - Iterates through specified range starting with 4 and running until 8, incremented by 1 each cycle
    for rate in range(4, 9, 1):
        #WA - Divides annual rate by months in 1 year (12) to get percentage.
        #     Result is divided by 100 to obtain decimal value usable in the following formulas
        monthlyRate = (rate / 12) / 100
        #WA - Uses provided formulas to calculate monthlyPayment and the totalPayment for the provided rate
        monthlyPayment = loanAmount * monthlyRate / (1 - math.pow(1 / (1 + monthlyRate), loanYears * 12))
        totalPayment = monthlyPayment * loanYears * 12
        #WA - Uses replacement fields to set a maximum column width and left align data set rows.
        #     Will also truncate result to 2 decimal places
        print('{0:<8} {1:<18} {2:<16}'.format(str(rate) + '%', '%.2f' % monthlyPayment, '%.2f' % totalPayment))

#WA - Accepts a message and performs check to verify input is not a negative number,
#     uses a while loop to prompt user until valid input is given
def getInput(message):
    userInput = float(input(message))
    while userInput < 0:
        userInput = float(input(message))
    return userInput


main()
