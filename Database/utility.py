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
    file.close()
    return records
