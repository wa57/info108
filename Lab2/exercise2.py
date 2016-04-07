def main():
    value = 99
    print('The value is', value)
    value = change_me(value)
    print('Back in main the value is', value)

def change_me(arg):
    print('I am changing the value.')
    arg = 0
    print('Now the value is', arg)
    return(arg)

main()
