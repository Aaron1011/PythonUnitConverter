#!/usr/bin/env python
from inches import *
from feet import *
from yards import *
from miles import *
print 'Welcome to Python Unit converter!'
print 'Currently, only units of length can be converted.'
def __init__():
    a = raw_input('What measurement system would you like to convert?\n[E]nglish to english, [Metric to metric, or [B]oth: ')
    if a == 'E' or a == 'e':
        __english__()
    else:
         print 'Sorry! That is not available yet!'
         __init__()  

def __english__():
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
        __english__()
if __name__ == '__main__':
    __init__()
