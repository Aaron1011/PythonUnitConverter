def feet_inches(n):
    a = n * 12
    if a == 1:
        print str(n) + ' feet = ' + str(a) + ' inch.'
    else:
        print str(n) + ' feet = ' + str(a) + ' inches.'

def foot():
    a = input('How many feet would you like to convert? ')
    b = raw_input('What you you like to convert to? [I]nches, [Y]ards, [M]iles: ')
    if b == 'I' or b == 'i':
        feet_inches(a)
