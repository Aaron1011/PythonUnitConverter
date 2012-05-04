def kilometers_millimeters(n, api=False):
    b = float(n) * 1000000
    if api == True:
        return b
    if  float(n) == 1:
        print str(n) + ' kilometer = ' + str(b) + ' millimeter(s).'
        quit()
    else:
        print str(n) + ' kilometers = ' + str(b) + ' millimeter(s).'
        quit()

def kilometers_centimeters(n, api=False):
    b = float(n) * 100000
    if api == True:
        return b
    if  float(n) == 1:
        print str(n) + ' kilometer = ' + str(b) + ' centimeter(s).'
        quit()
    else:
        print str(n) + ' kilometers = ' + str(b) + ' centimeter(s).'
        quit()

def kilometers_decimeters(n, api=False):
    b = float(n) * 10000
    if api == True:
        return b
    if  float(n) == 1:
        print str(n) + ' kilometer = ' + str(b) + ' decimeter(s).'
        quit()
    else:
        print str(n) + ' kilometers = ' + str(b) + ' decimeter(s).'
        quit()

def kilometers_meters(n, api=False):
    b = float(n) * 1000
    if api == True:
        return b
    if  float(n) == 1:
        print str(n) + ' kilometer = ' + str(b) + ' meter(s).'
        quit()
    else:
        print str(n) + ' kilometers = ' + str(b) + ' meter(s).'
        quit()


def kilometer():
    try:
        a = float(raw_input('How many kilometers would you like to convert? '))
    except ValueError:
        print 'You need to enter a number!'
        foot()
    b = raw_input('What you you like to convert to? [M]illimeters, [C]entimeters, [D]ecimeters, [Me]ters: ')
    if b == 'M' or b == 'm':
        kilometers_millimeters(a)
    elif b == 'C' or b == 'c':
        kilometers_centimeters(a)
    elif b == 'D' or b == 'd':
        kilometers_decimeters(a)
    elif b == 'Me' or b == 'me' or b == 'mE':
        kilometers_meters(a)
