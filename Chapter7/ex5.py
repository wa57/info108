totalInsects = 0
for day in range(1,8):
    insectsCollected = int(input('Enter the number of insects collected on day '+str(day)+': '))
    totalInsects += insectsCollected
print('Total insects collected:', totalInsects)
