def inches_millimeters(n, api=False):
    a = n * 25.4
    if api == True:
        return b
    if n == 1:
        print str(n) + ' inch = ' + str(a) + ' millimeters.'
    else:
        print str(n) + ' inches = ' + str(a) + ' millimeters.'

def inches_centimeters(n, api=False):
    a = n * 2.54
    if api == True:
        return b
    if n == 1:
        print str(n) + ' inch = ' + str(a) +  ' centimeters.'
    else:
        print str(n) + ' inches = ' + str(a) +  ' centimeters.'

def inches_decimeters(n, api=False):
    a = n * 0.254
    if api == True:
        return b
    if n == 1:
        print str(n) + ' inch = ' + str(a) +  ' decimeters.'
    else:
        print str(n) + ' inches = ' + str(a) +  ' decimeters.'
        
def inches_meters(n, api=False):
    a = n * 0.0254
    if api == True:
        return b
    if n == 1:
        print str(n) + ' inch = ' + str(a) + ' meters.'
    else:
        print str(n) + ' inches = ' + str(a) + ' meters.'
        
def inches_kilometers(n, api=False):
    a = n * 0.0000254
    if api == True:
        return b
    if n == 1:
        print str(n) + ' inch = ' + str(a) + ' kilometers.'
    else:
        print str(n) + ' inches = ' + str(a) + ' kilometers.'

def both_inch():
    try:
        a = float(raw_input('How many inches would you like to convert? '))
    except ValueError:
        print 'You need to enter a number!'
        both_inch()
    b = raw_input('What would you like to convert to? [M]illimeters, [C]entimeters. [D]ecimeters, [Me]ters, [K]ilometers? ')    
    if b == 'M' or b == 'm':
        inches_millimeters(a)
    elif b == 'C' or b == 'c':
        inches_centimeters(a)
    elif b == 'D' or b == 'd':
        inches_decimeters(a)
    elif b == 'me' or b == 'Me':
        inches_meters(a)
    elif b == 'k' or b == 'K':
        inches_kilometers(a)
    else:
        #print 'That unit is not available yet!'
        both_inch()
