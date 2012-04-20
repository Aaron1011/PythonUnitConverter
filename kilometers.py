def kilometer():
    try:
        a = float(raw_input('How many kilometers would you like to convert? '))
    except ValueError:
        print 'You need to enter a number!'
        foot()
    b = raw_input('What you you like to convert to? [M]illimeters, [C]entimeters, [D]ecimeters, [Me]ters: ')
    #if b == 'M' or b == 'm':
    #    centimeters_millimeters(a)
    #if b == 'D' or b == 'd':
    #    centimeters_decimeters(a)
    #if b == 'Me' or b == 'me' or b == 'mE':
    #    centimeters_meters(a)
    #if b == 'K' or b == 'k':
    #    centimeters_kilometers(a)
