def centimeters_feet(n, api=False):
	a = n * 0.033
	if api == True:
		return a
	if n == 1:
		print str(n) + ' centimeter = ' + str("{0:.1}".format(a)) + ' feet.'
	else:
		print str(n) + ' centimeters = ' + str ("{0:.2}".format(a)) + ' feet.'


def centimeters_yards(n, api=False):
    a = n * 0.010936
    if api == True:
        return a
    if n == 1:
        print str(n)  + ' centimeter = ' + str(a)  + ' yards.'
    else:
        print str(n) + ' centimeters = ' + str(a) + ' yards.'


def centimeters_miles(n, api=False):
	a = n * 0.0006214
	if api == True:
		return a
	if n == 1:
		print str(n) + ' centimeter = ' + str(a) + ' miles'

	else:
		print str(n) + ' centimeters = ' + str(a) + ' miles'


def both_centimeter():
	try:
		a = float(raw_input('How many centimeters would you like to convert? '))
	except ValueError:
		print 'You need to enter a number!'
		both_centimeter()

	b = raw_input('What would you like to convert to? [F]eet, [Y]ards or [M]iles [Q]uit  ')
	if b == 'F' or b == 'f':
		centimeters_feet(a)
	elif b == 'Y' or b == 'y':
		centimeters_yards(a)
	elif b == 'M' or b == 'm':
		centimeters_miles(a)
	elif b == 'q' or b == 'Q':
		print 'Goodbye \n'
		quit()
	else:
		print 'That unit is not available yet'
		both_centimeter()