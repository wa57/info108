def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(str(n))
        countdown(n-1)

countdown(3)
