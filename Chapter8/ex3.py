def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

#WA - If there is a lower case character in the string it will return True
any_lowercase1('STRiNG')

#WA - Will always return the string 'True', arguments are not used except for iteration
any_lowercase2('string')

#WA - Will return true if any character in the string is lowercase
any_lowercase3('STRiNG')

#WA - Will return false by default unless a character is found that is lower case
any_lowercase4()

#WA - Will return false if any character is lowercase in the string
any_lowercase5()
