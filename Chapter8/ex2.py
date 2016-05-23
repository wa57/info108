#WA - defaults string value to the string 'reverse'
string = 'reverse'
def reverseString(string):
    #WA - uses string slicing to reverse the array, string.reverse() also works
    string = string[::-1]
    for char in string:
        print(char)

reverseString(string)
