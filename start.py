#!/usr/bin/env python
from inches import *
from feet import *
from yards import *
print 'Welcome to Python Unit converter!'

def __init__():
    c = raw_input('Choose the unit you would to convert: [I]nches, [F]eet, [Y]ards, [M]iles ')
    if c == 'i' or c == 'I':
        inch()
    elif c == 'F' or c == 'f':
        foot()
    elif c == 'Y' or c == 'y':
        yard() 
    else:
        print 'That conversion is not available yet.'
        __init__()
if __name__ == '__main__':
    __init__()
