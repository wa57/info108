print('Minutes', ' ','Calories Burned')
print('-'*25)

#WA - Begin table creation loop, top level row
for minutes in range(10, 35, 5):
    #WA - Initiailize row as an empty string
    row = ''

    #WA - Begin column creation of which there are 2 (Minutes, Calories Burned)
    for column in range(2):
        #WA - If it is the first iteration, then append just the minutes column
        if(column == 0):
            row += str(minutes)
        #WA - If second iteration, append the calculated calories burned
        else:
            #WA - Extra formatting to line up with column headings
            row += ' '*8 + str(3.9 * minutes)

    #WA - Print out the row
    print(row)
