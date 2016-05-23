#WA - Get first and second word from user
string1 = input('First word: ')
string2 = input('Second word: ')

#WA - default string3 to specified value
string3 = 'I love programming'

#WA - Use the 'in' operator to determine whether the string specified is present, outputs boolean
print('First word is in the third string:', string1 in string3)
print('Second word is in the third string:', string2 in string3)

#WA - Use the replace method to replace occurence of 'love' with 'hate'
string4 = string3.replace('love', 'hate')
print(string4)
