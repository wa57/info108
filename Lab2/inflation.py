#WA - Gathers oldPrice and newPrice and passes to calcInflation to be calculated
def main():
    oldPrice = float(input('Price of an item 1 year ago: '))
    newPrice = float(input('Price of an item today: '))
    calcInflation(oldPrice, newPrice)
    input('Press Enter to continue...')

#WA - Calculates inflation rate using standard inflation formula, then formats output to be a percentage with 2 leading decimal places
def calcInflation(oldPrice, newPrice):
    inflation = (newPrice - oldPrice) / oldPrice
    print('Inflation Rate:', '{:.2%}'.format(inflation))

main()
