"""
1._____ Write a while loop that lets the user enter a number. The number
should be multiplied by 2, and the result assigned to a variable named “product”.
The program should continue to multiply by 2 and print &quot;product&quot; out as long as
“product” is less than 1000.
"""

number = int(input('Enter a number: '))
while number < 1000:
    number = number * 2
    print(number)
input('Press Enter to continue...')
