#Project Name: Lab 3 Problem 1
#Date: 4/13/16
#Programmer Name: Will Ashman
#Project Description: Program to award points based on the amount of books purchased in a month

def main():
    #WA - Takes user input and converts to float
    booksPurchased = float(input('Number of books purchased this month: '))
    print()

    #WA - Checks if input is greater than or equal to 0
    if booksPurchased >= 0:
        simpleIfFunction(booksPurchased)
        nestedIfFunction(booksPurchased)
        elifFunction(booksPurchased)
    else:
        print('Invalid Entry')

    print()
    input('Press Enter to continue...')

#WA - Checks value of books purchased to determine the number of points awarded using standard if statements
def simpleIfFunction(booksPurchased):
    #WA - Default number of points awarded
    pointsAwarded = 0

    if booksPurchased == 1:
        pointsAwarded = 5

    if booksPurchased == 2:
        pointsAwarded = 15

    if booksPurchased == 3:
        pointsAwarded = 30

    if booksPurchased > 3:
        pointsAwarded = 60

    #WA - Prints number of points awarded to the console
    print('The simpleIfFunction awarded', pointsAwarded, 'points.')

#WA - Uses nested conditionals to determine number of points awarded
def nestedIfFunction(booksPurchased):
    #WA - Default number of points awarded
    pointsAwarded = 0

    if booksPurchased == 1:
        pointsAwarded = 5
    else:
        if booksPurchased == 2:
            pointsAwarded = 15
        else:
            if booksPurchased == 3:
                pointsAwarded = 30
            else:
                if booksPurchased > 3:
                    pointsAwarded = 60

    #WA - Prints number of points awarded to the console
    print('The nestedIfFunction awarded', pointsAwarded, 'points.')

#WA - Uses elif to determine number of points awarded
def elifFunction(booksPurchased):
    #WA - Default number of points awarded
    pointsAwarded = 0

    if booksPurchased == 1:
        pointsAwarded = 5
    elif booksPurchased == 2:
        pointsAwarded = 15
    elif booksPurchased == 3:
        pointsAwarded = 30
    elif booksPurchased > 3:
        pointsAwarded = 60

    print('The elifFunction awarded', pointsAwarded, 'points.')

main()
