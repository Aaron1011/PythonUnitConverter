def yards_inches(n, api=False):
    a = n * 36
    if api==True:
        return b
    if n == 1:
        print str(n) + ' yard = ' + str(a) + ' inch(es).'
        
    else:
        print str(n) + ' yards = ' + str(a) + ' inch(es).'

def yards_feet(n, api=False):
    a = n * 3
    if api==True:
        return b
    if n == 1:
        print str(n) + ' yard = ' + str(a) + ' feet.'
    else:
        print str(n) + ' yards = ' + str(a) + ' feet.'

def yards_miles(n, api=False):
    a = float(n) / 1760
    if api==True:
        return b
    if n == 1:
        print str(n) + ' yard = ' + str(a) + ' mile(s).'
    else:
        print str(n) + ' yards = ' + str(a) + ' mile(s).'

def yard():
    try:
        a = float(raw_input('How many yards would you like to convert? '))
    except ValueError:
        print 'You need to enter a number!'
        yard()
    b = raw_input('What would you like to convert to? [I]inches, [F]eet, [M]iles: ')
    if b == 'I' or b == 'i':
        yards_inches(a)
    elif b == 'F' or b == 'f':
        yards_feet(a)
    elif b == 'M' or b == 'm':
        yards_miles(a)
    else:
        print b + ' is not a valid choice. You need to enter I, F, or M!.'
        yard()
