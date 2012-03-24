print 'Welcome to Python Unit converter!'

def inches_feet(n):
    a = n / 12
    if a == 1:
        print str(n) + ' inches = ' + str(a) + ' foot.'
    else:
        print str(n) + ' inches = ' + str(a) + ' feet.'


def __init__():
    c = raw_input('Choose the unit you would to convert: [I]nches, [F]eet, [Y]ards, [M]iles ')
    def inches():
        a = input('How many inches would you like to convert: ')
        b = raw_input('What would you like to convert to? [F]eet, [Y]ards, [M]iles: ')
        if b == 'F' or b == 'f':
            inches_feet(a)
    if c == 'i' or c == 'I':
        inches()
    else:
        print 'Goodbye!'
if __name__ == '__main__':
    __init__()


