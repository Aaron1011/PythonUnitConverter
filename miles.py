def miles_inches(n):
    b = n * 63360
    if  n == 1:
        print str(n) + ' mile = ' + str(b) + ' inch(es).'
        quit()
    else:
        print str(n) + ' miles = ' + str(b) + ' inch(es).'
        quit()

def mile():
    try:
        a = float(raw_input('How many miles would you like to convert? '))
    except ValueError:
        print 'You need to enter a number!'
        mile()
    b = raw_input('What you you like to convert to? [I]nches, [F]eet, [Y]ards: ')
    if b == "I" or b == "i":
        miles_inches(a)
