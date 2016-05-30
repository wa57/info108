#Project Name: Individual Assignment
#Date: 6/1/16
#Programmer Names: Will Ashman
#Project Description: Relational Database using only lists


import os
import utility
import student_table
import class_table

#WA - Routes the user's choice to the appropriate function
def userChoiceHandler(userChoice):
    utility.cls()
    if(userChoice == '1'):
        class_table.addNewClass()
    elif userChoice == '2':
        student_table.addNewStudent()
    elif userChoice == '3':
        class_table.deleteClassRecord()
    elif userChoice == '4':
        student_table.deleteStudentRecord()
    elif userChoice == '5':
        class_table.classReport()
    elif userChoice == '6':
        student_table.studentReport()
    elif userChoice == '7':
        class_table.studentReportByClass()
    elif(userChoice == '8'):
        quit()

#WA - Main function that controls displaying the menu and watching for user selections
def displayMenu():
    utility.cls()
    printMenuHeading()
    printChoices()
    userChoice = input('\nMake a selection: ')
    userChoiceHandler(userChoice)
    repeat()
    input('Press Enter to continue...')

def printMenuHeading():
    print('\nDatabase Operations')
    print('-'*30)

#WA - Reads list of choices from menu_choices.txt file and displays them
def printChoices():
    choices = utility.readRecordsFromFile('data_files/menu_choices.txt')
    counter = 1
    for choice in choices[0]:
        print(str(counter) + '.', choice)
        counter += 1

#WA - Determines if the user wants to make a new selection
def repeat():
    repeat = input('\nMake another selection? (y/n): ')
    if repeat == 'y':
        displayMenu()
    else:
        quit()

displayMenu()
