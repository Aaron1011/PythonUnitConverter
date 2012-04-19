def millimeters_centimeters(n):
    b = float(n) / 10
    if  float(n) == 1:
        print str(n) + ' millimeter = ' + str(b) + ' centimeter(s).'
        quit()
    else:
        print str(n) + ' millimeters = ' + str(b) + ' centimeter(s).'
        quit()

def millimeters_decimeters(n):
    b = float(n) / 100
    if  float(n) == 1:
        print str(n) + ' millimeter = ' + str(b) + ' decimeter(s).'
        quit()
    else:
        print str(n) + ' millimeters = ' + str(b) + ' deciimeter(s).'
        quit()

def millimeters_meters(n):
    b = float(n) / 1000
    if  float(n) == 1:
        print str(n) + ' millimeter = ' + str(b) + ' meter(s).'
        quit()
    else:
        print str(n) + ' millimeters = ' + str(b) + ' meter(s).'
        quit()


def millimeter():
    try:
        a = float(raw_input('How many millimeters would you like to convert? '))
    except ValueError:
        print 'You need to enter a number!'
        millimeter()
    b = raw_input('What you you like to convert to? [C]entimeters, [D]ecimeters, [M]eters, [K]ilometers: ')
    if b == 'C' or b == 'c':
       millimeters_centimeters(a)
    if b == 'D' or b == 'd':
       millimeters_decimeters(a)
    if b == 'M' or b == 'm':
        millimeters_meters(a)
    if b == 'K' or b == 'k':
        quit()
