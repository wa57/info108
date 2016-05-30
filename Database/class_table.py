import utility
import student_table

#WA - Reads in class records from class_db.txt and stores it in global classTable variable
classTable = utility.readRecordsFromFile('data_files/class_db.txt')

#WA - Returns a list of the table's columns
def getAllColumns():
    return ['class_id', 'class_name', 'instructor_first_name', 'instructor_last_name']

#WA - Converts a column string to the corresponding index located in the table's columns list
def colToIndex(column):
    return getAllColumns().index(column)

#WA - Merges a student record and the corresponding class record into a single list
def joinStudentsByClass(students, course):
    joinedRows = []
    instructorName = course[colToIndex('instructor_first_name')] + ' ' + course[colToIndex('instructor_last_name')]
    for student in students:
        studentName = student[student_table.colToIndex('first_name')] + ' ' + student[student_table.colToIndex('last_name')]
        newRow = [course[colToIndex('class_id')], instructorName, studentName, student[student_table.colToIndex('grade')]]
        joinedRows.append(newRow)
    return joinedRows

#WA - Prints out the student report by class table by joining the two table's rows
def studentReportByClass():
    studentsAndClasses = []
    for course in classTable:
        students = student_table.getStudentsByClassId(course[colToIndex('class_id')])
        studentsAndClasses = studentsAndClasses + joinStudentsByClass(students, course)
    printStudentReportByClass(studentsAndClasses)

#WA - Uses replacement fields to set a maximum column width and left align column headers
def printStudentReportByClass(studentsAndClasses):
    print('\n{0:<10} {1:<20} {2:<20} {3:<15}\n'.format('Class Id', 'Instructor', 'Student', 'Grade'))
    print('-'*60)
    for row in studentsAndClasses:
        print('\n{0:<10} {1:<20} {2:<20} {3:<15}'.format(row[0], row[1], row[2], row[3]))

#WA - Gets user input and adds the new list to the table
def addNewClass():
    newClass = []
    for column in getAllColumns():
        field = input(utility.formatColName(column) + ': ')
        newClass.append(field)
    classTable.append(newClass)
    saveClassTable()

#WA - Gets the class and deletes the record from the list
def deleteClassRecord():
    class_id = input('Class Id: ')
    classToDelete = getClassById(class_id)
    if classToDelete == None:
        print('0 matches found for Class Id:', class_id)
    print('\n1 Class Found')
    printClass(classToDelete)
    deleteChoice = input('Delete class? ')
    if deleteChoice.lower() == 'y':
        del classTable[classTable.index(classToDelete)]
        print('Class', classToDelete[colToIndex('class_id')],'successfully deleted')
        saveClassTable()

#WA - Prints a single class record
def printClass(classInfo):
    columns = getAllColumns()
    print('-'*30)
    for idx, item in enumerate(classInfo):
        print(utility.formatColName(columns[idx]) + ':', item)
    print('-'*30)

#WA - Retrieves a class record from the table based on its class_id
def getClassById(class_id):
    match = []
    for row in classTable:
        if(row[colToIndex('class_id')] == class_id):
            match = row
    return match

#WA - Uses replacement fields to set a maximum column width and left align column headers
def classReport():
    print('\n{0:<10} {1:<15} {2:<25} {3:<25}'.format('Class Id', 'Class Name', 'Instructor First Name', 'Instructor Last Name'))
    print('-'*74)
    for course in classTable:
        print('\n{0:<10} {1:<15} {2:<25} {3:<25}'.format(course[0], course[1], course[2], course[3]))

#WA - Writes the classTable list to the class_db.txt file
def saveClassTable():
    utility.writeRecordsToFile('data_files/class_db.txt', classTable)
