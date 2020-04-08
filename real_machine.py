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
        self.mem.change_memory('0-0', '0000')
        
        #command reading
        #ic
        self.mem.change_memory('0-1', '0000')

        #mode user mode by default
        #mode
        self.mem.change_memory('0-2', '0001')

        #interrupts
        #ti
        self.mem.change_memory('1-0', '0010')

        #si
        self.mem.change_memory('1-1', '0000')

        #pi
        self.mem.change_memory('1-2', '0000')
        
        #ioi
        self.mem.change_memory('1-3', '0000')

        #channel registers
        #ch1
        self.mem.change_memory('2-0', '0000')
        #ch2
        self.mem.change_memory('2-1', '0000')
        #ch3
        self.mem.change_memory('2-2', '0000')
    
        #random usage registers
        self.mem.change_memory('3-0', '0000')
        self.mem.change_memory('3-1', '0000')
        self.mem.change_memory('3-2', '0000')
        #true/false register
        self.mem.change_memory('3-3', '0000')

        #start by menu
        RM.menu(self)

    def menu(self):
        '''function that takes care of menu and then splits the workflow'''
        last_action = None
        
        while True:
            os.system('cls')

            print('------  Main menu  -------')
            print('MODE:', self.mem.get_register('MODE'))
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
                print('------   Registers   -------')
                print('Paging')
                print('---')
                print('PTR \t\t\t ', self.mem.get_register('PTR'))
                print('----------------------------')
                print('Mode')
                print('---')
                print('MODE \t\t\t ', self.mem.get_register('MODE'))
                print('----------------------------')
                print('Command Reading')
                print('---')
                print('IC \t\t\t ', self.mem.get_register('IC'))
                print('----------------------------')
                print('Interrupts')
                print('---')
                print('TI \t\t\t ', self.mem.get_register('TI'))
                print('SI \t\t\t ', self.mem.get_register('SI'))
                print('PI \t\t\t ', self.mem.get_register('PI'))
                print('IOI \t\t\t ', self.mem.get_register('IOI'))
                print('----------------------------')
                print('Random Usage')
                print('---')
                print('RA \t\t\t ', self.mem.get_register('RA'))
                print('RB \t\t\t ', self.mem.get_register('RB'))
                print('RC \t\t\t ', self.mem.get_register('RC'))
                print('C \t\t\t ', self.mem.get_register('C'))
                print('----------------------------')
                print('Channel Usage')
                print('---')
                print('CH1 \t\t\t ', self.mem.get_register('CH1'))
                print('CH2 \t\t\t ', self.mem.get_register('CH2'))
                print('CH3 \t\t\t ', self.mem.get_register('CH3'))
                print('----------------------------')
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

    def _stop(self):
        sys.exit('Stopping')
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
