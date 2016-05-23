#submission: save "main" (so init.py) python file to a .txt file and submit to Final Individual Assignment Text File (also applies to team assignment)
#multiple files: zip them and submit in Zip File link
#need to submit gameworld as well, has separate submission link

import os
import utility
import student_table

def getUniqueId(table):
    print(len(studentsTable))

"""def printTable(results):
    for row in results:
        print(row[0], row[1], row[2])
"""

def printTable(table):
    print(getAllColumns())
    print(table)

def userChoiceHandler(userChoice):
    if(userChoice == '1'):
        student_id = input("Student ID: ")
        student = student_table.getStudentById(student_id)
        print(student)
    if(userChoice == '2'):
        #newStudentId = getUniqueStudentId() #will
        student_table.getNewStudentInfo()
        #print(columns[col])
        """
        newStudent = [
            5,
            input('New Student First Name: '),
            input('New Student Last Name: '),
            input('New Student ')
        ]
        first_name =
        last_name = input('New Student Last Name: ')
        """
    if(userChoice == '3'):
        print('hi')

        #data = [line.strip() for line in open("db/students_db.txt", 'r')]
        #print(data)


        #for tuple in test:
            #print(list(test))
        #print(test)

        #file.read()

        #with open(outfile, 'wb') as f:
            #csv.writer(f, delimiter=' ').writerows(mat)

    if(userChoice == '8'):
        quit()


def displayMenu():
    printMenuHeading()
    printChoices()

    userChoice = input('Make a selection: ')
    userChoiceHandler(userChoice)
    repeat()

    input('Press Enter to continue...')

def printMenuHeading():
    print('\nDatabase Operations')
    print('-'*19)

def printChoices():
    choices = [
        'Add a Class',
        'Add a Student',
        'Delete a Class Record',
        'Delete a Student Record',
        'Class Report',
        'Student Report',
        'Student Report by Class',
        'Exit'
    ]

    counter = 1
    for choice in choices:
        print(str(counter) + '.', choice)
        counter += 1

def repeat():
    repeat = input('Make another selection? (y/n): ')
    if(repeat == 'y'):
        displayMenu()

def main():
    os.system('clear||cls')
    #printTable(getAllStudents(table))
    print(student_table.studentsTable)
    displayMenu()

main()


#print(getStudentById(2))
#print(getStudentsByFirstName('will'))
#0th element of array is always the column labels row
#for row in table:
    #print(row[0], row[1], row[2])
#WA - Uses replacement fields to set a maximum column width and left align column headers


#def getAllUsers():
    #print('\n{0:<8} {1:<18} {2:<16}'.format('id', 'first_name', 'last_name'))
    #print('-'*46)

#getAllUsers()
#WA - Uses replacement fields to set a maximum column width and left align data set rows.
#     Will also truncate result to 2 decimal places
#ROW print('{0:<8} {1:<18} {2:<16}'.format(str(rate) + '%', '$%.2f' % monthlyPayment, '$%.2f' % totalPayment))
