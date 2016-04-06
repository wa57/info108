#Project Name: Lab 2 Problem 2
#Date: 4/4/16
#Programmer Name: Will Ashman
#Project Description: Lab 2 Homework

#WA - gather and pass input to be calculated
def main():
    loan = float(input('Monthly loan payment: '))
    insurance = float(input('Monthly insurance expense: '))
    gas = float(input('Monthly gas expense: '))
    oil = float(input('Monthly oil expense: '))
    tire = float(input('Monthly tire expense: '))
    maintenance = float(input('Monthly maintenance expense: '))
    showExpense(loan, insurance, gas, oil, tire, maintenance)

#calculate monthly expense and then use result to calculate annual expense
def showExpense(loan, insurance, gas, oil, tire, maintenance):
    monthly = loan + insurance + gas + oil + tire + maintenance
    annual = monthly * 12
    print('Total Monthly Expense: $' + '%.2f' % monthly)
    print('Total Yearly Expense: $' + '%.2f' % annual)

main()
input('Press enter to continue...')
