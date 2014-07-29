#!/usr/bin/env python

from modules import *
import platform
print 'Welcome to Python Unit converter!'
if platform.architecture()[0] == '64bit':
    print "Congratulations! You're using a 64-bit OS!" 
print 'Currently, only units of length can be converted.'

def __init__():
    a = raw_input('What measurement system would you like to convert?\n[E]nglish to english, [M]etric to metric, or [B]oth: ')
    if platform.system() == 'Windows':
    
        if a == 'E' or a == 'e':
            __english__()
            raw_input('Please press enter to exit: ')
        elif a == 'M' or a == 'm':
            __metric__()
            raw_input('Please press enter to exit: ')
        elif a == 'B' or a == 'b':
            __both__()
            raw_input('Please press enter to exit: ')
    else:
        if a == 'E' or a == 'e':
            __english__()
            
        elif a == 'M' or a == 'm':
            __metric__()
            
        elif a == 'B' or a == 'b':
            __both__()

        else:
            print("Please enter a valid option \n\n")
            __init__()

def __english__():
    c = raw_input('Choose the unit you would like to convert: [I]nches, [F]eet, [Y]ards, [M]iles ')
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
    c = raw_input('Choose the unit you would like to convert: [M]ilimeters, [C]entimeters, [D]ecimeters, [Me]ter, [K]ilometer: ')
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

def both_english():
    c = raw_input('Choose the unit you would like to convert: [I]nches, [F]eet, [Y]ards, [M]iles ')
    if c == 'I' or c == 'i':
        both_inch()
    if c == 'f' or c == 'F':
        pass #both_feet()
    else:
        print 'That unit is not available yet!'

def both_metric():
    #print 'both metric unit'

    c2 = raw_input('Choose the unit you would like to convert: [M]illimeters, [C]entimeters, [D]ecimeters, [Me]ters, [K]ilometers ')

    if c2 == 'C' or c2 == 'c':
        both_centimeter()
        
    elif c2 == 'D' or c2 == 'd':
        both_decimeter()

    elif c2 == 'Me' or c2 == 'me':
        both_meter()

    elif c2 == 'K' or c2 == 'k':
        both_kilometer()

    elif c2 == 'M' or 'm':
        both_millimeter()

    else:
        print 'Please enter a valid option\n\n'
        both_metric()


def __both__():
    
    c1 = raw_input('Would you like to convert [E]nglish to Metric, or [M]etric to English? ')
    if c1 == 'E' or c1 =='e':
        both_english()
    elif c1 == 'M' or c1 == 'm':
        both_metric()


if __name__ == '__main__':
    __init__()
