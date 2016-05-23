"""a) _____ Assume “choice” is a variable that references a string.
The following if statement determines whether choice is equal to ‘Y’ or ‘y’.:

if choice == ‘Y’ or choice == ‘y’:
Rewrite this statement so it only makes one comparison and does not use the or operator.

b) _____ Write a loop that counts the number of space characters that appear in
the string referenced by “myString”. myString = “The best things in life are free.”

c) _____ Write a function that accepts a string as an argument and returns
true if the argument ends with the substring “.com”. Otherwise, the function
should return false.

"""
choice = 'Y'
if choice.lower() == 'y':
    print(True)

myString = 'The best things in life are free.'
emptySpaces = 0
for char in myString:
    if(char == ' '):
        emptySpaces += 1
print(emptySpaces)

def isURI(string):
    #WA - starts at the end of the string and slices the last 4 characters (the domain)
    if(string[-4:] == '.com'):
        return True
    return False

uri = input('URI: ')
print(isURI(uri))
