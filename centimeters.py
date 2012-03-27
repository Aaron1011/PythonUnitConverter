def centimeters_millimeters(n):
    b = float(n) * 10
    if  float(n) == 1:
        print str(n) + ' centimeter = ' + str(b) + ' millimeter(s).'
        quit()
    else:
        print str(n) + ' centimeters = ' + str(b) + ' millimeter(s).'
        quit()

def centimeter():
    try:
        a = float(raw_input('How many centimeters would you like to convert? '))
    except ValueError:
        print 'You need to enter a number!'
        foot()
    b = raw_input('What you you like to convert to? [M]illimeters, [D]ecimeters, [Me]ters, [K]ilometers: ')
    if b == 'M' or b == 'm':
        centimeters_millimeters(a)
    if b == 'Y' or b == 'y':
        quit()
    if b == 'M' or b == 'm':
        quit()
