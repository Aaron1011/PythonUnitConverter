def inches_feet(n, api=False):
    a = n / float(12)
    if api==True:
        return a
    if n == 1:
        print str(n) + ' inch = ' + str(a) + ' feet.'
        
    else:
        print str(n) + ' inches = ' + str(a) + ' feet.'
    inch() #Returns control to inch module
        
def inches_yards(n, api=False):
    a = n / float(36)
    if api==True:
        return a
    if n == 1:
        print str(n) + ' inchn = ' + str(a) + ' yard(s).'
    else:
        print str(n) + ' inches = ' + str(a) + ' yard(s).'
    inch() 

def inches_miles(n, api=False):
    a = n / float(63360)
    if api==True:
        return a
    if n == 1:
        print str(n) + ' inch = ' + str(a) + ' mile(s).'
    else:
        print str(n) + ' inch = ' + str(a) + ' mile(s).'
    inch() 

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
