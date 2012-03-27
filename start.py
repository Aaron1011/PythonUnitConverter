#!/usr/bin/env python
from inches import *
from feet import *
from yards import *
from miles import *
print 'Welcome to Python Unit converter!'

def __init__():
    c = raw_input('Choose the unit you would to convert: [I]nches, [F]eet, [Y]ards, [M]iles ')
    if c == 'i' or c == 'I':
        inch()
    elif c == 'F' or c == 'f':
        foot()
    elif c == 'Y' or c == 'y':
        yard() 
    elif c == 'M' or c == 'm':
        mile()
    else:
        print 'That is not a unit!'
        __init__()
if __name__ == '__main__':
    __init__()
