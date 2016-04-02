#Project Name: Lab 1 Problem 2
#Date: 4/1/16
#Programmer Name: Will Ashman
#Project Description: Lab 1 Homework

print('Please input 5 floats.')

#WA - Gather numbers to be averaged
average = 0
for num in range(1,6):
    average += float(input('Number ' + str(num) + ': '))

#WA - Output averaged numbers
print('The average is ' + str(average/5) + '.')
input('Press enter to continue.')
