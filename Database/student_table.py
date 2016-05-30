import utility

#WA - Reads in student records from student_db.txt and stores it in global studentsTable variable
studentsTable = utility.readRecordsFromFile('data_files/students_db.txt')

#WA - Returns a list of the table's columns
def getAllColumns():
    return ['student_id', 'class_id', 'first_name', 'last_name', 'grade']

#WA - Converts a column string to the corresponding index located in the table's columns list
def colToIndex(column):
    return getAllColumns().index(column)

#WA - Gets user input and adds the new list to the table
def addNewStudent():
    newStudent = []
    for column in getAllColumns():
        field = input(utility.formatColName(column) + ': ')
        newStudent.append(field)
    studentsTable.append(newStudent)
    saveStudentsTable()

#WA - Gets the student and deletes the record from the list
def deleteStudentRecord():
    student_id = input('Student Id: ')
    class_id = input('Class Id: ')
    student = getStudentByClassAndId(student_id, class_id)
    if len(student) == 0:
        print('0 matches found for Student Id:', student_id, 'and Class Id:', class_id)
    print('\n1 Student(s) Found')
    printStudent(student)
    deleteChoice = input('Delete student? ')
    if deleteChoice.lower() == 'y':
        del studentsTable[studentsTable.index(student)]
        print('\nStudent', student[colToIndex('student_id')],'successfully deleted')
        saveStudentsTable()

#WA - Prints a single student record
def printStudent(student):
    columns = getAllColumns()
    print('-'*30)
    for idx, item in enumerate(student):
        print(utility.formatColName(columns[idx]) + ':', item)
    print('-'*30)

#WA - Uses replacement fields to set a maximum column width and left align column headers
def studentReport():
    print('\n{0:<15} {1:<15} {2:<15} {3:<15} {4:<15}'.format('Student Id', 'Class Id', 'First Name', 'Last Name', 'Grade'))
    print('-'*70 + '\n')
    for student in studentsTable:
        print('{0:<15} {1:<15} {2:<15} {3:<15} {4:<15}'.format(
            student[colToIndex('student_id')],
            student[colToIndex('class_id')],
            student[colToIndex('first_name')],
            student[colToIndex('last_name')],
            student[colToIndex('grade')])
        )

#WA - Writes the classTable list to the class_db.txt file
def saveStudentsTable():
    utility.writeRecordsToFile('data_files/students_db.txt', studentsTable)

#WA - Iterates through the students table to find students with a specific class name
def getStudentsByClassId(class_id):
    matches = []
    for student in studentsTable:
        if student[colToIndex('class_id')] == class_id:
            matches.append(student)
    return matches

#WA - Retrieves a student record from the table based on its student_id
def getStudentById(student_id):
    id = utility.safelyConvertToInt(student_id)
    for row in studentsTable:
        if(row[colToIndex('student_id')] == id):
            return row

#WA - Retrieves a matched student record based on a student_id and class_id
def getStudentByClassAndId(student_id, class_id):
    matched_student = []
    for row in studentsTable:
        if(row[colToIndex('student_id')] == student_id and row[colToIndex('class_id')] == class_id):
            matched_student = row
    return matched_student
