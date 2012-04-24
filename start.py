#!/usr/bin/env python
from imports import *
import platform
print 'Welcome to Python Unit converter!'
if platform.architecture()[0] == '64bit':
    print "Congratulations! You're using a 64-bit OS!" 
print 'Currently, only units of length can be converted.'
def __init__():
    a = raw_input('What measurement system would you like to convert?\n[E]nglish to english, [M]etric to metric, or [B]oth: ')
    if a == 'E' or a == 'e':
        __english__()
    elif a == 'M' or a == 'm':
        __metric__()
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



def __metric__():
    c = raw_input('Choose the unit you would to convert: [M]ilimeters, [C]entimeters, [D]ecimeters, [Me]ter, [K]ilometer: ')
    if c == 'c' or c == 'C':
        centimeter()
    elif c == 'M' or c == 'm':
        millimeter()
    elif c == 'D' or c == 'd':
        decimeter()
    elif c == 'Me' or c == 'me':
        meter()
    elif c == 'K' or c == 'k':
        kilometer()
    else:
        print 'That unit is not available!'
        __metric__()


if __name__ == '__main__':
    __init__()
