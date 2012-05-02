def inches_millimeters(n):
    a = n * 25.4
    if n == 1:
        print str(n) + ' inch = ' + str(a) + ' centimeters.'
    else:
        print str(n) + ' inches = ' + str(a) + ' centimeters.'

def inches_centimeters(n):
    a = n * 2.54
    if n == 1:
        print str(n) + ' inch = ' + str(a) +  ' centimeters.'
    else:
        print str(n) + ' inches = ' + str(a) +  ' centimeters.'

def both_inch():
    try:
        a = float(raw_input('How many inches would you like to convert? '))
    except ValueError:
        print 'You need to enter a number!'
        inch()
    b = raw_input('What would you like to convert to? [M]illimeters, [C]entimeters. [D]ecimeters, [Me]ters, [K]ilometers? ')    
    if b == 'M' or b == 'm':
        inches_millimeters(a)
    elif b == 'C' or b == 'c':
        inches_centimeters(a)
