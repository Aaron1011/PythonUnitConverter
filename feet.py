def feet_inches(n):
    b = int(n) * 12
    if  int(n) == 1:
        print str(n) + ' feet = ' + str(b) + ' inch.'
        quit()
    else:
        print str(n) + ' feet = ' + str(b) + ' inches.'
        quit()

def foot():
    try:
        a = int(raw_input('How many feet would you like to convert? '))
    except ValueError:
        print 'You need to enter a number!'
        foot()
    b = raw_input('What you you like to convert to? [I]nches, [Y]ards, [M]iles: ')
    if b == 'I' or b == 'i':
        feet_inches(a)
