#WA - Enter number of researchers
researchers = int(input('\nEnter the number of researchers: '))

#WA - Top level researcher loop, iterates through number of researchers entered
for researcher in range(researchers):
    #WA - Prints out researcher name
    print('\nResearcher number', researcher + 1)

    #WA - Initializes totalInsects
    totalInsects = 0

    #WA - Iterates through 7 days
    for day in range(1,8):
        #WA - Asks for insects collected on each day
        insectsCollected = int(input('Enter the number of insects collected on day '+str(day)+': '))

        #WA - Adds insects collected to total number for that researcher
        totalInsects += insectsCollected

    #WA - Prints out results of each researcher
    print('Total insects collected by researcher', str(researcher + 1) + ': ', totalInsects)
