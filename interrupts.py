#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Marius Pozniakovas, Tomas Kučejevas"
__email__ = "pozniak.marius@gmail.com"
'''script used to call different interrupts'''

ONE_BYTE = int(255)


def PI_interrupt(obj, codes, modes):
    '''returns a number of interrupt to PI register
    input:
    modes = operation, address, HDD, overflow, arythmetical
    returns:
    1       => inputted operation doesnt exist
    2       => inputted address doesnt exist
    3       => no memory in HDD
    4       => register overflow
    5       => arythmetical command used and C != 1

    None    => No interrupt
    '''
    #1. check for wrong operation
    if 'operation' in modes:
        
        print(len(codes))

        for code in codes:
            if not check_functions(code):
                obj._pi = 1
                input("INTERRUPT PI " + str(obj._pi) + '\n')
                return obj._pi


    #4. check for overflow
    if 'overflow' in modes:
        if int(obj._ptr)      > ONE_BYTE * 4 or + \
            int(obj._ic)      > ONE_BYTE * 2 or + \
            int(obj._mode)    > ONE_BYTE * 1 or + \
            int(obj._ti)      > ONE_BYTE * 1 or + \
            int(obj._si)      > ONE_BYTE * 1 or + \
            int(obj._pi)      > ONE_BYTE * 1 or + \
            int(obj._ioi)     > ONE_BYTE * 1 or + \
            int(obj._ch1)     > int(1)       or + \
            int(obj._ch2)     > int(1)       or + \
            int(obj._ch3)     > int(1)       or + \
            int(obj._ra)      > ONE_BYTE * 4 or + \
            int(obj._rb)      > ONE_BYTE * 4 or + \
            int(obj._rc)      > ONE_BYTE * 4 or + \
            int(obj._c)      > 1:
                obj._pi = 4
                input("INTERRUPT PI " + str(obj._pi) + '\n')
                return obj._pi   
    
    return None

def SI_interrupt(obj):
    '''returns a number of interrupt to SI register
    possible interrupts:
    1       => user uses supervisor command

    None    => No interrupt
    '''

    return None

def IOI_interrupt(obj):
    '''returns a number of interrupt to IOI register
    possible interrupts:
    0       => problem in 3 channel (input)
    1       => problem in 3 channel (output)
    2       => problem in 2 channel (output)
    3       => problem in 1 channel (input)

    None    => No interrupt
    '''

    return None

def TI_interrupt(obj):
    '''returns a number of interrupt to TI register
    possible interrupts:
    0       => time is over

    None    => No interrupt
    '''
    

    return None

def check_functions(words_of_code):
    '''function to check input and return true if everything is ok'''
        
    words_of_code = words_of_code.split()
    print

    if words_of_code is None or len(words_of_code) == 0:
        return False
    #--------------
    elif words_of_code[0] == 'CODE' and len(words_of_code) == 1:
        return True
    #--------------
    elif words_of_code[0] == 'RMW' and len(words_of_code) == 3:
        return True
    elif words_of_code[0] == 'RMI' and len(words_of_code) == 3:
        return True
    #--------------
    elif words_of_code[0] == 'ADD' and len(words_of_code) == 1:
        return True
    elif words_of_code[0] == 'SUB' and len(words_of_code) == 1:
        return True
    elif words_of_code[0] == 'CMP' and len(words_of_code) == 1:
        return True
    #--------------
    elif words_of_code[0] == 'JP' and len(words_of_code) == 3:
        return True
    elif words_of_code[0] == 'JE' and len(words_of_code) == 3:
        return True
    elif words_of_code[0] == 'JG' and len(words_of_code) == 3:
        return True
    elif words_of_code[0] == 'HALT' and len(words_of_code) == 1:
        return True
    #--------------
    elif words_of_code[0] == 'OUT' and len(words_of_code) == 1:
        return True
    elif words_of_code[0] == 'RDW' and len(words_of_code) == 3: #and isinstance(words_of_code[1], int) and isinstance(words_of_code[2], int):
        return True
    elif words_of_code[0] == 'RDI' and len(words_of_code) == 3: #and isinstance(words_of_code[1], int) and isinstance(words_of_code[2], int):
        return True
    #--------------
    else:
        return False