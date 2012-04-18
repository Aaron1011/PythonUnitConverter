def centimeters_millimeters(n):
    b = float(n) * 10
    if  float(n) == 1:
        print str(n) + ' centimeter = ' + str(b) + ' millimeter(s).'
        quit()
    else:
        print str(n) + ' centimeters = ' + str(b) + ' millimeter(s).'
        quit()

def centimeters_decimeters(n):
    b = float(n) / 10
    if float(n) == 1:
        print str(n) + ' centimeter = ' + str(b) + ' decimeter(s).'
    else:
        print str(n) + ' centimeters = ' + str(b) + ' decimeter(s).'

def centimeters_meters(n):
    b = float(n) / 100
    if float(n) == 1:
        print str(n) + ' centimeter = ' + str(b) + ' meter(s).'
    else:
        print str(n) + ' centimeters = ' + str(b) + ' meter(s).'

def centimeter():
    try:
        a = float(raw_input('How many centimeters would you like to convert? '))
    except ValueError:
        print 'You need to enter a number!'
        foot()
    b = raw_input('What you you like to convert to? [M]illimeters, [D]ecimeters, [Me]ters, [K]ilometers: ')
    if b == 'M' or b == 'm':
        centimeters_millimeters(a)
    if b == 'D' or b == 'd':
        centimeters_decimeters(a)
    if b == 'Me' or b == 'me' or b == 'mE':
        centimeters_meters(a)
