#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Marius Pozniakovas, Tomas Kučejevas"
__email__ = "pozniak.marius@gmail.com"
'''script used to call different interrupts'''

def PI_interrupt(rm):
    '''returns a number of interrupt to PI register
    returns:
    1       => inputted operation doesnt exist
    2       => inputted address doesnt exist
    3       => no memory in HDD
    4       => overflow
    5       => arythmetical command used and C != 1

    None    => No interrupt
    '''

    return None

def SI_interrupt(rm):
    '''returns a number of interrupt to SI register
    possible interrupts:
    1       => user uses supervisor command

    None    => No interrupt
    '''

    return None

def IOI_interrupt(rm):
    '''returns a number of interrupt to IOI register
    possible interrupts:
    0       => problem in 3 channel (input)
    1       => problem in 3 channel (output)
    2       => problem in 2 channel (output)
    3       => problem in 1 channel (input)

    None    => No interrupt
    '''

    return None

def TI_interrupt(rm):
    '''returns a number of interrupt to TI register
    possible interrupts:
    0       => time is over

    None    => No interrupt
    '''
    

    return None

