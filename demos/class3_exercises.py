room = 503
print("I am staying in room number", room)
print("I am staying in room number" + str(room))
print("I am staying in room number" + str(room))
print("I am staying in room number " + str(room) + ".")

units_sold = 10
sales_amount = 300
print("We sold", units_sold, "units", \
	"for a total of", sales_amount,".")

yourName = 'will'

print('Hello World!', 'My name is', yourName + '.')
print('Hello World!\n', 'My name is', yourName + '.')
print('This is a free apostrophe! \'')
print('This is a free quote! \' ')
print('This is a free quote and backlash! \' \\')

print('\t\t Classroms\n')
print('\t\t102\tINFO200')
print('\t\t105\tINFO201')
print('\t\t106\tINFO202')


#part 4
strVar = 3289.1234567890
intVar = 3289

print('%6.2f' %strVar)
print('$%10.2f' %strVar)

print()
print()
print('\t$%6.2f' %strVar,'\t$%6.2f' %strVar,'\t$%6.2f' %strVar)

print('%5d' %strVar)
print('%o' %intVar)
print('%x' %intVar)
print('%X' %intVar)

hours = input('How many hours did you work? ')
print(type(hours))
print('At $10 per hour, you earned $' + hours * 10 + '.')
