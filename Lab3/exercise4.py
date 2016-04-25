if 0:
    print('0 is true')
else:
    print('0 is false')
print()

if 1:
    print('1 is true')
else:
    print('1 is false')
print()

if -1:
    print('-1 is true')
else:
    print('-1 is false')

extra = 2
if extra < 0:
    print('small')
else:
    if extra == 0:
        print('medium')
    else:
        print('large')
        
extra = 2
if extra < 0:
    print('small')
elif(extra == 0):
    print('medium')
else:
    print('large')
