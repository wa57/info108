import os

#WA - Attempts to convert a string to an integer with error handling in a try/except block
def safelyConvertToInt(string):
    try:
        return int(string)
    except Exception:
        print('error: alphanumeric')
        pass

def openFile(filepath):
    try:
        file = open(filepath)
        for line in file:
            print(line)
        fin.close()
    except:
        print('Something went wrong')
        print('please check dir and filename')

def writeRecordsToFile(filepath, records):
    try:
        file = open(filepath, 'w')
        for row in records:
            file.write('%s,' % row)
        file.close()
    except:
        print('Something went wrong saving the records.')

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

def formatColName(column):
    return column.replace('_', ' ').title()
