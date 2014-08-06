def kilometers_feet(n, api=False):
	a = n * 3280.8

	if api == True:
		return a
	if n == 1:
		print str(n) + ' kilometer = ' + str("{0:.1}".format(a)) + ' feet.'
	else:
		print str(n) + ' kilometers = ' + str("{0:.1}".format(a)) + ' feet.'
	both_kilometer()


def kilometers_yards(n, api=False):
	a = n * 1093.6

	if api == True:
		return a
	if n == 1:
		print str(n) + ' kilometer = ' + str("{0:.1}".format(a)) + ' yards.'
	else:
		print str(n) + ' kilometerss = ' + str("{0:.1}".format(a)) + ' yards.'
	both_kilometers()


def kilometers_miles(n, api=False):
	a = n * 0.62137

	if api == True:
		return a
	if n == 1:
		print str(n) + ' kilometer = ' + str("{0:.1}".format(a)) + ' miles.'
	else:
		print str(n) + ' kilometers = ' + str("{0:.1}".format(a)) + ' miles.'
	both_kilometer()


def kilometers_inches(n, api=False):
	a = n * 39.370

	if api == True:
		return a
	if n == 1:
		print str(n) + ' kilometer = ' + str("{0:.1}".format(a)) + ' inches.'
	else:
		print str(n) + ' kilometers = ' + str("{0:.1}".format(a)) + ' inches.'
	both_kilometer()	




def both_kilometer():
    try:
        a = float(raw_input('How many kilometers would you like to convert? '))
    except ValueError:
        print 'You need to enter a number!'
        both_kilometer()

    b = raw_input('What would you like to convert to? [I]nches, [F]eet, [Y]ards or [M]iles [Q]uit  ')
    
    if b == 'F' or b == 'f':
        kilometers_feet(a)
    elif b == 'Y' or b == 'y':
		kilometers_yards(a)
    elif b == 'm' or b == 'M':
        kilometers_miles(a)
    elif b == 'I' or b == 'i':
    	kilometers_inches(a)
	if b == 'Q' or b == 'q':
		print 'Goodbye \n'
		quit()

	else:
		print 'That unit is not available yet'
		both_kilometer()