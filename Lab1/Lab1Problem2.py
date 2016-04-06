#Project Name: Lab 1 Problem 1
#Date: 4/1/16
#Programmer Name: Will Ashman
#Project Description: Lab 1 Homework

#WA - Gather Length, Width, Height for calculation
print('Please input the room dimensions.')
length = float(input('Length: '))
width = float(input('Width: '))
height = float(input('Height: '))

#WA - Floor and ceiling share the same area (assumed), so we calculate that independently for readability
floorAndCeiling = (length * width) * 2

#WA - Calculate all 4 walls, since the room is rectangular we need to calculate length walls and width walls respectively
walls = ((height * width) * 2) + ((height * length) * 2)

#WA - Add floor/ceiling and walls to get the total area of the room
totalArea = floorAndCeiling + walls

print('The total area is: ' + str(totalArea))
input('Press enter to continue.')
