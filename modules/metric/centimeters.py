def centimeters_millimeters(n, api=False):
    b = float(n) * 10
    if api == True:
        return b
    if  float(n) == 1:
        print str(n) + ' centimeter = ' + str(b) + ' millimeter(s).'
         
    else:
        print str(n) + ' centimeters = ' + str(b) + ' millimeter(s).'
         

def centimeters_decimeters(n, api=False):
    b = float(n) / 10
    if api == True:
        return b
    if float(n) == 1:
        print str(n) + ' centimeter = ' + str(b) + ' decimeter(s).'
    else:
        print str(n) + ' centimeters = ' + str(b) + ' decimeter(s).'

def centimeters_meters(n, api=False):
    b = float(n) / 100
    if api == True:
        return b
    if float(n) == 1:
        print str(n) + ' centimeter = ' + str(b) + ' meter(s).'
    else:
        print str(n) + ' centimeters = ' + str(b) + ' meter(s).'
def centimeters_kilometers(n, api=False):
    b = float(n) / 1000
    if api == True:
        return b
    if float(n) == 1:
        print str(n) + ' centimeter = ' + str(b) + ' kilometer(s).'
    else:
        print str(n) + ' centimeters = ' + str(b) + ' kilometer(s).'

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
    if b == 'K' or b == 'k':
        centimeters_kilometers(a)
            
