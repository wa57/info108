sales = int(input('Sales: '))

commissionRate = 0

if sales < 10000:
    commissionRate = .1

if 10000 <= sales <= 15000:
    commissionRate = .15

if sales > 15000:
    commissionRate = .2

print('Comission Rate:', str(commissionRate * 100) + '%')
input('Press Enter to continue...')
