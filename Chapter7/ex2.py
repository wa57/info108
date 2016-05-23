"""
2._____ Write a while loop that asks the user to enter two numbers. The
numbers should be added and the sum displayed. The loop should ask the user if
he or she wishes to perform the operation again. If so, the loop should repeat,
otherwise it should terminate.
"""
repeat = 'y'
while repeat == 'y':
    number = float(input('\nEnter a number: '))
    number1 = float(input('\nEnter a second number: '))
    print('\n',number + number1)
    repeat = input('\nRepeat? (y/n) ')
    
