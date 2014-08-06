"""
Metric to English Conversions module.
These are conversions of Millimeters to either Feet, Yards or Miles
"""
def millimeters_feet(n, api=False):
	a = n * 0.0032808	

	if api == True:
		return a
	if n == 1:
		print str(n) + ' millimeter = ' + str(a) + ' feet.'
	else:
		print str(n) + ' millimeters = ' + str(a) + ' feet.'
	both_millimeter()

def millimeters_yards(n, api=False):
	a = n * 0.0010936

	if api == True:
		return a
	if n == 1:
		print str(n) + ' millimeter = ' + str(a) + ' yards.'
	else:
		print str(n) + ' millimeters = ' + str(a) + ' yards.'
	both_millimeter()

def millimeters_miles(n, api=False):
	a = n * 0.0000006214

	if api == True:
		return a
	if n == 1:
		print str(n) + ' millimeter = ' + str(a) + ' miles.'
	else:
		print str(n) + ' millimeters = ' + str(a) + ' miles.'
	both_millimeter()


def both_millimeter():
	try:
		a = float(raw_input('How many millimeters would you like to convert? '))
	except ValueError:
		print 'You need to enter a number!'
		both_millimeter()

	b = raw_input('What would you like to convert to? [F]eet, [Y]ards or [M]iles [Q]uit  ')
	if b == 'F' or b == 'f':
		millimeters_feet(a)
	elif b == 'Y' or b == 'y':
		millimeters_yards(a)
	elif b == 'M' or b == 'm':
		millimeters_miles(a)
	elif b == 'q' or b == 'Q':
		print 'Goodbye \n'
		quit()
	else:
		print 'That unit is not available yet'
		both_millimeter()