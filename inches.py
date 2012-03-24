def inches_feet(n):
    a = n / 12
    if a == 1:
        print str(n) + ' inches = ' + str(a) + ' foot.'
    else:
        print str(n) + ' inches = ' + str(a) + ' feet.'

def inches():
        a = input('How many inches would you like to convert: ')
        b = raw_input('What would you like to convert to? [F]eet, [Y]ards, [M]iles: ')
        if b == 'F' or b == 'f':
            inches_feet(a)
