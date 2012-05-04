def meters_millimeters(n, api=False):
    b = float(n) * 1000
    if api == True:
        return b
    if  float(n) == 1:
        print str(n) + ' meter = ' + str(b) + ' millimeter(s).'
        quit()
    else:
        print str(n) + ' meters = ' + str(b) + ' millimeter(s)'
        quit()

def meters_centimeters(n, api=False):
    b = float(n) * 100
    if api == True:
        return b
    if  float(n) == 1:
        print str(n) + ' meter = ' + str(b) + ' centimeter(s).'
        quit()
    else:
        print str(n) + ' meters = ' + str(b) + ' centimeter(s)'
        quit()

def meters_decimeters(n, api=False):
    b = float(n) * 10
    if api == True:
        return b
    if  float(n) == 1:
        print str(n) + ' meter = ' + str(b) + 'decimeter(s).'
        quit()
    else:
        print str(n) + ' meters = ' + str(b) + ' decimeter(s)'
        quit()

def meters_kilometers(n, api=False):
    b = float(n) / 1000
    if api == True:
        return b
    if  float(n) == 1:
        print str(n) + ' meter = ' + str(b) + 'kilometer(s).'
        quit()
    else:
        print str(n) + ' meters = ' + str(b) + ' kilometer(s)'
        quit()

def meter():
    try:
        a = float(raw_input('How many meters would you like to convert? '))
    except ValueError:
        print 'You need to enter a number!'
        meter()
    b = raw_input('What you you like to convert to? [M]illimeters, [C]entimeters, [D]ecimeters, [K]ilometers: ')
    if b == 'M' or b == 'm':
        meters_millimeters(a)
    elif b == 'C' or b == 'c':
        meters_centimeters(a)
    elif b == 'D' or b == 'd':
        meters_decimeters(a)
    elif b == 'K' or b == 'k':
        meters_kilometers(a)
    else:
        print 'That unit is not available!'
