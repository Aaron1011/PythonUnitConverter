def meters_feet(n, api=False):
	a = n * 3.2808

	if api == True:
		return a
	if n == 1:
		print str(n) + ' meter = ' + str(a) + ' feet.'
	else:
		print str(n) + ' meters = ' + str(a) + ' feet.'
	both_meter()

def meters_yards(n, api=False):
	a = n * 1.0936

	if api == True:
		return a
	if n == 1:
		print str(n) + ' meter = ' + str(a) + ' yards.'
	else:
		print str(n) + ' meters = ' + str(a) + ' yards.'
	both_meter()


def meters_miles(n, api=False):
	print 'meters_miles module'
	a = n * 0.00000062137

	if api == True:
		return a
	if n == 1:
		print str(n) + ' meter = ' + str(a) + ' miles.'
	else:
		print str(n) + ' meters = ' + str(a) + ' miles.'
	both_meter()

def meters_inches(n, api=False):
	a = n * 39.370

	if api == True:
		return a
	if n == 1:
		print str(n) + ' meter = ' + str(a) + ' inches.'
	else:
		print str(n) + ' meters = ' + str(a) + ' inches.'
	both_meter()	




def both_meter():
    try:
        a = float(raw_input('How many meters would you like to convert? '))
    except ValueError:
        print 'You need to enter a number!'
        both_meter()

    b = raw_input('What would you like to convert to? [F]eet, [Y]ards or [M]iles [Q]uit  ')
    
    if b == 'F' or b == 'f':
        meters_feet(a)
    elif b == 'Y' or b == 'y':
		meters_yards(a)
    elif b == 'm' or b == 'M':
        meters_miles(a)
	if b == 'Q' or b == 'q':
		print 'Goodbye \n'
		quit()

	else:
		print 'That unit is not available yet'
		both_meter()