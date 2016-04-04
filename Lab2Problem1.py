#Project Name: Lab 2 Problem 1
#Date: 4/4/16
#Programmer Name: Will Ashman
#Project Description: Lab 2 Homework

KILOMETERS_TO_MILES = 0.6214

#WA - gather input and pass kilometers to conversion
def main():
    kilometers = float(input('Distance in kilometers: '))
    showMiles(kilometers)

#WA - perform conversion of kilometers and output 
def showMiles(kilometers):
    print('Conversion of', kilometers, 'to miles:', kilometers * KILOMETERS_TO_MILES)

main()

input('Press enter to continue...')
