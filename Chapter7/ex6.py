totalInsects = 0
day = 1
while day <= 7:
    insectsCollected = int(input('Enter the number of insects collected on day '+str(day)+': '))
    totalInsects += insectsCollected
    day += 1
print('Total insects collected:', totalInsects)
