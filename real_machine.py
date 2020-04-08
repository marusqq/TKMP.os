#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Marius Pozniakovas, Tomas Kučejevas"
__email__ = "pozniak.marius@gmail.com"

import os
import virtual_machine as VM
import memory as me

class RM:

    def __init__(self):
        '''create all the registers'''
        
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
        
        #also create memory
        self.mem = me.Memory()

        #start by menu
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
            print('Exit \t\t\t q')
            print("Last input: ", err)
            print('--------------------------')

            menu_choice = input('Input your choice: ')

            if menu_choice == '1':
                err = 'Input'
                vm = VM.VM(self)
                vm.start_console()

            elif menu_choice == '2':
                print('read from hdd')
                err = 'HDD'
                #break

            elif menu_choice == '3':
                os.system('cls')
                err = 'Memory'
                print('------   Registers   -------')
                print('Paging')
                print('---')
                print('PTR \t\t\t ', self._ptr)
                print('----------------------------')
                print('Mode')
                print('---')
                print('MODE \t\t\t ', self._mode)
                print('----------------------------')
                print('Command Reading')
                print('---')
                print('IC \t\t\t ', self._ic)
                print('----------------------------')
                print('Interrupts')
                print('---')
                print('TI \t\t\t ', self._ti)
                print('SI \t\t\t ', self._si)
                print('PI \t\t\t ', self._pi)
                print('IOI \t\t\t ', self._ioi)
                print('----------------------------')
                print('Random Usage')
                print('---')
                print('RA \t\t\t ', self._ra)
                print('RB \t\t\t ', self._rb)
                print('RC \t\t\t ', self._rc)
                print('C \t\t\t ', self._c)
                print('----------------------------')
                print('Channel Usage')
                print('---')
                print('CH1 \t\t\t ', self._ch1)
                print('CH2 \t\t\t ', self._ch2)
                print('CH3 \t\t\t ', self._ch3)
                print('----------------------------')
                _input = input('Press enter to exit to main menu\n')
                #break

            elif menu_choice == 'q':
                err = 'exiting'
                break

            else:
                err = 'Wrong Input' 

    #------------------
    #functions
    def _add(self):
        '''RC = RA + RB'''
        if(self._c == 0):
            self._rc = int(self._ra) + int(self._rb)
            self.mem.check_size(self._rc)
        else:
            print("C != 0, aborting operation")
        return

    def _sub(self):
        '''RC = RA - RB'''
        if(self._c == 0):
            self._rc = int(self._ra) - int(self._rb)
            self.mem.check_size(self._rc)
        else:
            print("C != 0, aborting operation")
        return

    def _cmp(self):
        ''' RA == RB ---> RC = 0
            RA < RB  ---> RC = 1
            RA > RB  ---> RC = 2 '''
        if self._ra == self._rb:
            self._rc = 0

        elif self._ra < self._rb:
            self._rc = 1

        elif self._ra > self._rb:
            self._rc = 2
        
        return
    
    def _rmw(self):
        '''TODO'''
        return

    def _rmi(self):
        '''TODO'''
        return

    def _jp(self):
        '''TODO'''
        return

    def _je(self):
        '''TODO'''
        return
    
    def _jg(self):
        '''TODO'''
        return

    def _halt(self):
        print('Halting')
        return

    def _out(self):
        print('RC =', self._rc)
        return

    def _rdw(self, a, b):
        self._ra = a
        self._rb = b
        self._c = 1
        return
    
    def _rdi(self, a, b):
        self._ra = a
        self._rb = b
        self._c = 0
        return
