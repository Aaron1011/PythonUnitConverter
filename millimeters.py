def millimeters_centimeters(n):
    b = float(n) / 10
    if  float(n) == 1:
        print str(n) + ' millimeter = ' + str(b) + ' centimeter(s).'
        quit()
    else:
        print str(n) + ' millimeters = ' + str(b) + ' centimeter(s).'
        quit()

def millimeter():
    try:
        a = float(raw_input('How many millimeters would you like to convert? '))
    except ValueError:
        print 'You need to enter a number!'
        foot()
    b = raw_input('What you you like to convert to? [C]entimeters, [D]ecimeters, [M]eters, [K]ilometers: ')
    if b == 'C' or b == 'c':
       millimeters_centimeters(a)
    if b == 'D' or b == 'd':
        quit()
    if b == 'M' or b == 'm':
        quit()
    if b == 'K' or b == 'k':
        quit()
