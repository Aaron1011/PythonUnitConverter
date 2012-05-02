def inches_feet(n):
    a = n / float(12)
    if n == 1:
        print str(n) + ' inch = ' + str(a) + ' feet.'
        quit()
    else:
        print str(n) + ' inches = ' + str(a) + ' feet.'
        quit()
def inches_yards(n):
    a = n / float(36)
    if n == 1:
        print str(n) + ' inchn = ' + str(a) + ' yard(s).'
    else:
        print str(n) + ' inches = ' + str(a) + ' yard(s).'

def inches_miles(n):
    a = n / float(63360)
    if n == 1:
        print str(n) + ' inch = ' + str(a) + ' mile(s).'
    else:
        print str(n) + ' inch = ' + str(a) + ' mile(s).'

def inch():
    try:
        a = float(raw_input('How many inches would you like to convert? '))
    except ValueError:
        print 'You need to enter a number!'
        inch()
    b = raw_input('What would you like to convert to? [F]eet, [Y]ards, [M]iles: ')    
    if b == 'F' or b == 'f':
        inches_feet(a)
    elif b == 'Y' or b == 'y':
        inches_yards(a)
    elif b == 'M' or b == 'm':
        inches_miles(a)
