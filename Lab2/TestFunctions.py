#WA - Gathers a positive, negative, and inclusive number between 48-122
#WA - As well as a string from the user
posInteger = float(input('Positive integer: '))
negInteger = float(input('Negative integer: '))
myChar = int(input('Integer between 48 and 122 inclusive: '))
myString = input('String: ')

#WA - outputs absolute value of postInteger and negInteger
print('Absolute value of', str(posInteger) + ':', abs(posInteger))
print('Absolute value of', str(negInteger) + ':', abs(negInteger))

#WA - output Unicode character associated with integer
print('Unicode translation of', str(myChar) + ':', chr(myChar))

#WA - output length of myString
print('Length of string', '"' + myString + '"' + ':', len(myString))

#WA - output posInteger to the power of 4
myPower = posInteger ** 4
print('Number', posInteger, 'to the power of 4:', myPower)
