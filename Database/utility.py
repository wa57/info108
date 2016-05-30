import os

#WA - Attempts to convert a string to an integer with error handling in a try/except block
def safelyConvertToInt(string):
    try:
        return int(string)
    except Exception:
        print('error: alphanumeric')
        pass

#WA - Accepts a filepath string and list as arguments and writes the records to the file given
def writeRecordsToFile(filepath, records):
    try:
        file = open(filepath, 'w')
        for row in records:
            file.write('%s,' % row)
        file.close()
    except:
        print('Something went wrong saving the records.')

#WA - Accepts a filepath string and reads the specified file's contents
#     The standard format is a list of lists with each nested list being an individual student or class record
#     The read will return a string of 'lists', we use eval to convert them into actual list objects
#     If there is only one record in the .txt file it will iterate through the list incorrectly, so we have to make sure it is nested
def readRecordsFromFile(filepath):
    file = open(filepath, 'r')
    records = []
    for line in file.readlines():
        for row in eval(line):
            records.append(row)
    if not isNested(records):
        records = [records]
    file.close()
    return records

#WA - Multi-platform screen clear for Unix and Windows operating systems
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#WA - Checks if there is any instance of a list within a list to determine if it is nested
def isNested(records):
    return any(isinstance(item, list) for item in records)

#WA - Formats the column names to convert to a more readable state, e.g. first_name > First Name
def formatColName(column):
    return column.replace('_', ' ').title()
