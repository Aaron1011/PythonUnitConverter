def decimeters_feet(n, api=False):
	a = n * 0.32808

	if api == True:
		return a
	if n == 1:
		print str(n) + ' decimeter = ' + str("{0:.1}".format(a)) + ' feet.'
	else:
		print str(n) + ' decimeters = ' + str("{0:.1}".format(a)) + ' feet.'
	both_decimeter()


def decimeters_yards(n, api=False):
	a = n * 0.10936

	if api == True:
		return a
	if n == 1:
		print str(n) + ' decimeter = ' + str("{0:.1}".format(a)) + ' yards.'
	else:
		print str(n) + ' decimeterss = ' + str("{0:.1}".format(a)) + ' yards.'
	both_decimeter()


def decimeters_miles(n, api=False):
	a = n * 0.000062137

	if api == True:
		return a
	if n == 1:
		print str(n) + ' decimeter = ' + str("{0:.1}".format(a)) + ' miles.'
	else:
		print str(n) + ' decimeters = ' + str("{0:.1}".format(a)) + ' miles.'
	both_decimeter()


def decimeters_inches(n, api=False):
	a = n * 3.9370

	if api == True:
		return a
	if n == 1:
		print str(n) + ' decimeter = ' + str("{0:.1}".format(a)) + ' inches.'
	else:
		print str(n) + ' decimeters = ' + str("{0:.1}".format(a)) + ' inches.'
	both_decimeter()	




def both_decimeter():
    try:
        a = float(raw_input('How many decimeters would you like to convert? '))
    except ValueError:
        print 'You need to enter a number!'
        both_decimeter()

    b = raw_input('What would you like to convert to? [I]nches, [F]eet, [Y]ards or [M]iles [Q]uit  ')
    
    if b == 'F' or b == 'f':
        decimeters_feet(a)
    elif b == 'Y' or b == 'y':
		decimeters_yards(a)
    elif b == 'm' or b == 'M':
        decimeters_miles(a)
    elif b == 'I' or b == 'i':
    	decimeters_inches(a)
	if b == 'Q' or b == 'q':
		print 'Goodbye \n'
		quit()

	else:
		print 'That unit is not available yet'
		both_decimeter()