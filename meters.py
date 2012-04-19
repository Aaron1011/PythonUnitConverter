def meter():
    try:
        a = float(raw_input('How many meters would you like to convert? '))
    except ValueError:
        print 'You need to enter a number!'
        meter()
    b = raw_input('What you you like to convert to? [M]illimeters, [C]entimeters, [D]ecimeters, [K]ilometers: ')
    quit()
