import utility

studentsTable = utility.readRecordsFromFile('data_files/students_db.txt')

def getAllColumns():
    return ['student_id', 'first_name', 'last_name']

def colToIndex(column):
    return getAllColumns().index(column)

def getNewStudentInfo():
    columns = getAllColumns()
    for col in columns:
        print(col, colToIndex(col))

def getStudentById(student_id):
    id = utility.safelyConvertToInt(student_id)
    for row in studentsTable:
        if(row[colToIndex('student_id')] == id):
            return row

def addStudent(newStudent, table):
    table.append(newStudent)
    return table

def getStudentsByFirstName(first_name, table):
    matched_users = []
    for row in table:
        if(row[colToIndex('first_name')].lower() == first_name.lower()):
            matched_users.append(row)
    return matched_users

def getStudentsByLastName(last_name, table):
    matched_users = []
    for row in table:
        if(row[2].lower() == last_name.lower()):
            matched_users.append(row)
    return matched_users

def getStudentsByFirstAndLastName(first_name, last_name, table):
    matched_users = []
    for row in table:
        if(row[colToIndex('first_name')] == first_name and row[colToIndex('last_name')] == last_name):
            matched_users.append(row)
    return matched_users

def getAllStudents(table):
    return table
