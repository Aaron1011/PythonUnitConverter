def yards_inches(n):
    a = n * 36
    if n == 1:
        print str(n) + ' yard = ' + str(a) + ' inch(es).'
        quit()
    else:
        print str(n) + ' yards = ' + str(a) + ' inch(es).'

def yards_feet(n):
    a = n * 3
    if n == 1
        print str(n) + ' yard = ' + str(a) + ' feet.'
    else:
        print str(n) + ' yards = ' + str(a) + ' feet.'
def yard():
    try:
        a = float(raw_input('How many yards would you like to convert? '))
    except ValueError:
        print 'You need to enter a number!'
        yard()
    b = raw_input('What would you like to convert to? [I]inches, [F]eet, [M]iles: ')
    if b == 'I' or b == 'i':
        yards_inches(a)
    elif b == 'F' or b == 'f':
        yards_feet(a)
    else:
        print 'That conversion is not available yet.'
