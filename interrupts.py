#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Marius Pozniakovas, Tomas Kučejevas"
__email__ = "pozniak.marius@gmail.com"
'''script used to call different interrupts'''

ONE_BYTE    = int(255)
TWO_BYTES   = int(255) * int(255)
THREE_BYTES = int(255) * int(255) * int(255)
FOUR_BYTES  = int(255) * int(255) * int(255) * int(255)


def PI_interrupt(obj, modes, codes = None, single_line = False):
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
        
        #check singleline
        if single_line:
            if not check_functions(codes):
                obj.mem.set_register('PI', 1)
                input("INTERRUPT PI " + str(obj.mem.get_register('PI')) + '\n')
                return obj.mem.get_register('PI')


        #check multiline
        else:
            for code in codes:
                if not check_functions(code):
                    obj.mem.set_register('PI', 1)
                    input("INTERRUPT PI " + str(obj.mem.get_register('PI')) + '\n')
                    return obj.mem.get_register('PI')


    #4. check for overflow
    if 'overflow' in modes:
        if obj.mem.get_register('PTR')      > FOUR_BYTES   or + \
            obj.mem.get_register('IC')      > TWO_BYTES    or + \
            obj.mem.get_register('MODE')    > ONE_BYTE     or + \
            obj.mem.get_register('TI')      > ONE_BYTE     or + \
            obj.mem.get_register('SI')      > ONE_BYTE     or + \
            obj.mem.get_register('PI')      > ONE_BYTE     or + \
            obj.mem.get_register('IOI')     > ONE_BYTE     or + \
            obj.mem.get_register('RA')      > FOUR_BYTES   or + \
            obj.mem.get_register('RB')      > FOUR_BYTES   or + \
            obj.mem.get_register('RC')      > FOUR_BYTES   or + \
            obj.mem.get_register('CH1')     > int(1)       or + \
            obj.mem.get_register('CH2')     > int(1)       or + \
            obj.mem.get_register('CH3')     > int(1)       or + \
            obj.mem.get_register('C')       > 1:

                obj.mem.set_register('PI', 4)
                input("INTERRUPT PI " + str(obj.mem.get_register('PI')) + '\n')
                return obj.mem.get_register('PI')   
    
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