def decimeters_centimeters(n):
    b = float(n) * 10
    if  float(n) == 1:
        print str(n) + ' decimeter = ' + str(b) + ' centimeter(s).'
        quit()
    else:
        print str(n) + ' decimeters = ' + str(b) + ' centimeter(s)'
        quit()

def decimeter():
    try:
        a = float(raw_input('How many decimeters would you like to convert? '))
    except ValueError:
        print 'You need to enter a number!'
        decimeter()
    b = raw_input('What you you like to convert to? [C]entimeters, [M]eters, [K]ilometers: ')
    if b == 'C' or b == 'c':
        decimeters_centimeters(a)
    if b == 'Y' or b == 'y':
        quit()
    if b == 'M' or b == 'm':
        quit()
