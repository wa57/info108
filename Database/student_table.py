import utility

studentsTable = utility.readRecordsFromFile('data_files/students_db.txt')

def getAllColumns():
    return ['student_id', 'class_id', 'first_name', 'last_name', 'grade']

def colToIndex(column):
    return getAllColumns().index(column)

def addNewStudent():
    newStudent = []
    for column in getAllColumns():
        field = input(utility.formatColName(column) + ': ')
        newStudent.append(field)
    studentsTable.append(newStudent)
    saveStudentsTable()

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

def printStudent(student):
    columns = getAllColumns()
    print('-'*30)
    for idx, item in enumerate(student):
        print(utility.formatColName(columns[idx]) + ':', item)
    print('-'*30)

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

def saveStudentsTable():
    utility.writeRecordsToFile('data_files/students_db.txt', studentsTable)

#WA - Iterates through the students table to find students with a specific class name
def getStudentsByClassId(class_id):
    matches = []
    for student in studentsTable:
        if student[colToIndex('class_id')] == class_id:
            matches.append(student)
    return matches

def getStudentById(student_id):
    id = utility.safelyConvertToInt(student_id)
    for row in studentsTable:
        if(row[colToIndex('student_id')] == id):
            return row

def getStudentByClassAndId(student_id, class_id):
    matched_student = []
    for row in studentsTable:
        if(row[colToIndex('student_id')] == student_id and row[colToIndex('class_id')] == class_id):
            matched_student = row
    return matched_student

def deleteStudent():
    print('delete student')
