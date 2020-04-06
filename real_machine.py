#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Marius Pozniakovas, Tomas Kučejevas"
__email__ = "pozniak.marius@gmail.com"

import os
import virtual_machine as VM

class RM:

    def __init__(self):
        
        #paging
        self._ptr = 0
        
        #command reading
        self._ic = 0

        #mode
        self._mode = 0
        
        #interrupts
        self._ti = 10
        self._si = 0
        self._pi = 0
        self._ioi = 0

        #channel registers
        self._ch1 = 0
        self._ch2 = 0
        self._ch3 = 0

        #random usage registers
        self._ra = 0
        self._rb = 0
        self._rc = 0

        #true/false register
        self._c = 0

        print('RM created.')
        RM.menu(self)

    def menu(self):
        '''function that takes care of menu and then splits the workflow'''
        err = None
        
        while True:
            os.system('cls')

            print('------  Main menu  -------')
            print('Command line \t\t 1')
            print('Read from HDD \t\t 2')
            print('Print registers \t 3')
            print('Exit \t\t\t 4')
            print("Last input: ", err)
            print('--------------------------')

            menu_choice = input('Input your choice: ')

            if menu_choice == '1':
                err = 'Input'
                vm = VM.VM()
                vm.collect_input()

            elif menu_choice == '2':
                print('read from hdd')
                err = 'HDD'
                #break

            elif menu_choice == '3':
                os.system('cls')
                err = 'Memory'
                print('------   Registers   -------')
                print('---------- Paging -----------')
                print('PTR \t\t\t ', self._ptr)
                print('----------- Mode ------------')
                print('Mode \t\t\t ', self._mode)
                print('- Command Reading Registry -')
                print('IC \t\t\t ', self._ic)
                print('-------- Interrupts ---------')
                print('TI \t\t\t ', self._ti)
                print('SI \t\t\t ', self._si)
                print('PI \t\t\t ', self._pi)
                print('IOI \t\t\t ', self._ioi)
                print('-- Random Usage Registers --')
                print('RA \t\t\t ', self._ra)
                print('RB \t\t\t ', self._rb)
                print('RC \t\t\t ', self._rc)
                print('C \t\t\t ', self._c)
                print('----- Channel Registers -----')
                print('CH1 \t\t\t ', self._ch1)
                print('CH2 \t\t\t ', self._ch2)
                print('CH3 \t\t\t ', self._ch3)
                print('-----------------------------')
                _input = input('Press enter to exit to main menu\n')
                #break

            elif menu_choice == '4':
                print('Exit')
                err = 'exiting'
                break

            else:
                err = 'Wrong Input' 

    def add(self, ra, rb):
        self._rc = self._ra + self._rb
        return
    
        



