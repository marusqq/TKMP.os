#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Marius Pozniakovas, Tomas Kučejevas"
__email__ = "pozniak.marius@gmail.com"

import os
import virtual_machine as VM
import memory as me
import interrupts as inte
import sys


class RM:

    def __init__(self):
        '''create all the registers'''

        #also create memory
        self.mem = me.Memory()
        
        #paging
        #ptr
        self.mem.set_register('PTR', '40')
        
        #command reading
        #ic
        self.mem.set_register('IC', '0000')

        #mode user mode by default
        #mode)
        self.mem.set_register('MODE', '0001')

        #interrupts
        #ti
        self.mem.set_register('TI', '0010')

        #si
        self.mem.set_register('SI', '0000')

        #pi
        self.mem.set_register('PI', '0000')
        
        #ioi
        self.mem.set_register('IOI', '0000')

        #channel registers
        #ch1
        self.mem.set_register('CH1', '0000')
        #ch2
        self.mem.set_register('CH2', '0000')
        #ch3
        self.mem.set_register('CH3', '0000')
    
        #random usage registers
        self.mem.set_register('RA', '0020')
        self.mem.set_register('RB', '0030')
        self.mem.set_register('RC', '0000')
        #true/false register
        self.mem.set_register('C', '0000')

        #start by menu
        RM.menu(self)

    def menu(self):
        '''function that takes care of menu and then splits the workflow'''
        last_action = None
        
        while True:
            os.system('cls')

            print('------  Main menu  -------')
            if self.mem.get_register('MODE') == 0:
                print('Mode: Admin')
            else:
                print('Mode: User')
            print('--------------------------')
            print('Command line \t\t 1')
            print('Read from HDD \t\t 2')
            print('Print registers \t 3')
            print('Print memory \t\t 4')
            print('Change mode \t\t 5')
            print('Exit \t\t\t q')
            print("Last action: ", last_action)
            print('--------------------------')

            menu_choice = input('Input your choice: ')

            if menu_choice == '1':
                last_action = 'Command line'
                vm = VM.VM(self)
                vm.start_console()

            elif menu_choice == '2':
                last_action = 'Read from HDD'
                #break

            elif menu_choice == '3':
                os.system('cls')
                last_action = 'Print registers'
                self.mem.print_registers()
                _input = input('Press enter to exit to main menu\n')
                #break

            elif menu_choice == '4':
                self.mem.print_memory()
                last_action = 'Print memory'
                _input = input('Press enter to exit to main menu\n')

            elif menu_choice == '5':
                last_action = 'Change mode'
                if(self.mem.get_register('MODE') == 0):
                    self.mem.set_register('MODE', 1)
                elif(self.mem.get_register('MODE') == 1):
                    pw = input("Please enter the password:\n")
                    if(pw == 'admin'):
                        self.mem.set_register('MODE', 0)
                    
            elif menu_choice == 'q':
                last_action = 'Exiting'
                break

            else:
                last_action = 'Wrong Input' 

    #------------------
    #functions
    def _add(self):
        '''RC = RA + RB'''
        int_value = inte.PI_interrupt(self, modes=['overflow', 'arytmetical'])
        if int_value is None:
            self.mem.set_register('RC', self.mem.get_register('RA') + self.mem.get_register('RB'))    
        return

    def _sub(self):
        '''RC = RA - RB'''
        int_value = inte.PI_interrupt(self, modes=['overflow', 'arytmetical'])
        if int_value is None:
            self.mem.set_register('RC', self.mem.get_register('RA') - self.mem.get_register('RB'))    
        return

    def _cmp(self):
        ''' RA == RB ---> RC = 0
            RA < RB  ---> RC = 1
            RA > RB  ---> RC = 2 '''
        int_value = inte.PI_interrupt(self, modes = 'arytmetical')
        if int_value is None:
            if self.mem.get_register('RA') == self.mem.get_register('RB'):
                self.mem.set_register('RC', 0)

            elif self.mem.get_register('RA') < self.mem.get_register('RB'):
                self.mem.set_register('RC', 1)

            elif self.mem.get_register('RA') > self.mem.get_register('RB'):
                self.mem.set_register('RC', 1)
            
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

    def _stop(self):
        sys.exit('Stopping')
        return

    def _out(self):
        print('[ RC =', self.mem.get_register('RC'), ']')
        return

    def _rdw(self, a, b):
        self.mem.set_register('RA', a)
        self.mem.set_register('RB', b)
        self.mem.set_register('RC', 1)
        return
    
    def _rdi(self, a, b):
        self.mem.set_register('RA', a)
        self.mem.set_register('RB', b)
        self.mem.set_register('RC', 0)
        return

    def _mrw(self, loc_a, loc_b):
        '''TODO'''
        return

    def _mri(self, loc_a, loc_b):
        '''TODO'''
        return
