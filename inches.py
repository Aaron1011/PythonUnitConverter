def inches_feet(n):
    a = n / 12
    if a == 1:
        print str(n) + ' inches = ' + str(a) + ' foot.'
    else:
        print str(n) + ' inches = ' + str(a) + ' feet.'

def inches_yards(n):
    a = n / 36
    if a == 1:
        print str(n) + ' inches = ' + str(a) + ' yard.'
    else:
        print str(n) + ' inches = ' + str(a) + ' yards.'

def inches_miles(n):
    a = n / 63360
    if a == 1:
        print str(n) + ' inches = ' + str(a) + ' mile.'
    else:
        print str(n) + ' inches = ' + str(a) + ' miles.'

def inch():
        a = input('How many inches would you like to convert? ')
        b = raw_input('What would you like to convert to? [F]eet, [Y]ards, [M]iles: ')
        if b == 'F' or b == 'f':
            inches_feet(a)
        elif b == 'Y' or b == 'y':
            inches_yards(a)
        elif b == 'M' or b == 'm':
            inches_miles(a)
