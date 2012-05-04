def miles_inches(n, api=False):
    if api==True:
        return b
    b = n * 63360
    if  n == 1:
        print str(n) + ' mile = ' + str(b) + ' inch(es).'
        
    else:
        print str(n) + ' miles = ' + str(b) + ' inch(es).'
        

def miles_feet(n, api=False):
    b = n * 5280
    if api==True:
        return b
    if  n == 1:
        print str(n) + ' mile = ' + str(b) + ' feet.'
        
    else:
        print str(n) + ' miles = ' + str(b) + ' feet.'
        

def miles_yards(n, api=False):
    b = n * 1760
    if api==True:
        return b
    if  n == 1:
        print str(n) + ' mile = ' + str(b) + ' yard(s).'
        
    else:
        print str(n) + ' miles = ' + str(b) + ' yard(s).'
         

def mile():
    try:
        a = float(raw_input('How many miles would you like to convert? '))
    except ValueError:
        print 'You need to enter a number!'
        mile()
    b = raw_input('What you you like to convert to? [I]nches, [F]eet, [Y]ards: ')
    if b == "I" or b == "i":
        miles_inches(a)
    if b == 'F' or b == 'f':
        miles_feet(a)
    if b == 'Y' or b == 'y':
        miles_yards(a)
