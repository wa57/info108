#Project Name: Lab 5 Homework
#Date: 5/18/16
#Programmer Name: Will Ashman
#Project Description: Lab 5 Homework

def main():
    ssn = input('Please enter the social security number in this format: DDD-DD-DDDD: ')

    #WA - Split the social security number on "-" to obtain 3 distinct parts
    splitSSN = ssn.split('-')

    #WA - Pass the raw social security number as well as the ssn split into 3 parts into the printResults method.
    printResults(ssn, splitSSN)


def printResults(ssn, splitSSN):
    #WA - Use the index method to find the two occurences of "-" in the ssn
    print('Found - at position', ssn.index('-', 0, 4))
    print('Found - at position', ssn.index('-', 5, 11))

    #WA - Print the 3 parts of the SSN which were split on the "-"
    print('The social security number split into 3 parts:', splitSSN[0] + ',', splitSSN[1] + ',', splitSSN[2])

    #WA - Initialize the counter so we can use it to track the iteration step
    counter = 0

    #WA - Iterate through split ssn which is a list containing all 3 parts
    for part in splitSSN:
        #WA - Print the step number (+1 because it starts at 0)
        #WA - Prints whether the part is all numbers using the isdigit() method
        #WA - Prints the length of the part using the len() method
        print('Part', counter + 1, 'is all digits:', splitSSN[counter].isdigit(), 'and has', len(splitSSN[counter]), 'characters.')

        #WA - Increment the counter once iteration is finished
        counter += 1

main()
