def feet_inches(n):
    b = float(n) * 12
    if  float(n) == 1:
        print str(n) + ' foot = ' + str(b) + ' inch(es).'
        quit()
    else:
        print str(n) + ' feet = ' + str(b) + ' inch(es).'
        quit()

def feet_yards(n):
    b = float(n) * 12
    if  float(n)  == 1:
        print str(n) + ' foot = ' + str(b) + ' yard(s).'
        quit()
    else:
        print str(n) + ' feet = ' + str(b) + ' yard(s).'

def feet_miles(n):
    b = float(n) / 5280
    if  float(n) == 1:
        print str(n) + ' foot = ' + str(b) + ' mile(s).'
        quit()
    else:
        print str(n) + ' feet = ' + str(b) + ' mile(s).'
        quit()

def foot():
    try:
        a = float(raw_input('How many feet would you like to convert? '))
    except ValueError:
        print 'You need to enter a number!'
        foot()
    b = raw_input('What you you like to convert to? [I]nches, [Y]ards, [M]iles: ')
    if b == 'I' or b == 'i':
        feet_inches(a)
    if b == 'Y' or b == 'y':
        feet_yards(a)
    if b == 'M' or b == 'm':
        feet_miles(a)
