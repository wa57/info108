sales = int(input('Sales: '))

#WA - Sets the default commission rate value
commissionRate = 0

#WA - Uses conditional to check if sales amount is
#     under 10000 then sets the rate
if sales < 10000:
    commissionRate = .1

#WA - Uses conditional to check if sales amount is within
#     the range of 10000 and 15000 then sets the rate
if 10000 <= sales <= 15000:
    commissionRate = .15

#WA - Uses conditional to check if sales amount is
#     larger than 15000 then sets the rate
if sales > 15000:
    commissionRate = .2


#WA - Converts the rate to a string and multiplies
#     by 100 to display as a percentage
print('Comission Rate:', str(commissionRate * 100) + '%')
input('Press Enter to continue...')
