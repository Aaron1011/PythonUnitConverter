def decimeters_millimeters(n, api=False):
    b = float(n) * 100
    if api == True:
        return b
    if  float(n) == 1:
        print str(n) + ' decimeter = ' + str(b) + ' millimeter(s).'
        quit()
    else:
        print str(n) + ' decimeters = ' + str(b) + ' millimeter(s)'
        quit()


def decimeters_centimeters(n, api=False):
    b = float(n) * 10
    if api == True:
        return b
    if  float(n) == 1:
        print str(n) + ' decimeter = ' + str(b) + ' centimeter(s).'
        quit()
    else:
        print str(n) + ' decimeters = ' + str(b) + ' centimeter(s)'
        quit()

def decimeters_meters(n, api=False):
    b = float(n) / 10
    if api == True:
        return b
    if  float(n) == 1:
        print str(n) + ' decimeter = ' + str(b) + ' meter(s).'
        quit()
    else:
        print str(n) + ' decimeters = ' + str(b) + ' meter(s)'
        quit()

def decimeters_kilometers(n, api=False):
    b = float(n) / 100
    if api == True:
        return b
    if  float(n) == 1:
        print str(n) + ' decimeter = ' + str(b) + ' kilometer(s).'
        quit()
    else:
        print str(n) + ' decimeters = ' + str(b) + ' kilometer(s)'
        quit()

def decimeter():
    try:
        a = float(raw_input('How many decimeters would you like to convert? '))
    except ValueError:
        print 'You need to enter a number!'
        decimeter()
    b = raw_input('What you you like to convert to? [M]illimeters, [C]entimeters, [Me]ters, [K]ilometers: ')
    if b == 'M' or b == 'm':
        decimeters_millimeters(a)
    if b == 'C' or b == 'c':
        decimeters_centimeters(a)
    if b == 'K' or b == 'k':
        decimeters_kilometers(a)
    if b == 'Me' or b == 'me':
        decimeters_meters(a)
