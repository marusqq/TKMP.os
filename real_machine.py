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
        self._ti = 0
        self._si = 0
        self._pi = 0
        self._ioi = 0

        #channel registers
        self._ch1 = 0
        self._ch2 = 0
        self._ch3 = 0

        #true/false register
        self._c = 0

        print('RM created.')
        RM.menu(self)

    def menu(self):
        err = None
        
        while True:
            os.system('cls')

            print('------  Main menu  -------')
            print('Command line \t\t 1')
            print('Read from HDD \t\t 2')
            print('Print all the memory \t 3')
            print('Exit \t\t\t 4')
            print("Last input: ", err)
            print('--------------------------')

            menu_choice = input('Input your choice: ')

            if menu_choice == '1':
                print('command line opened')
                err = 'command line'
                vm = VM.VM()
                vm.collect_input()
                
                #break

            elif menu_choice == '2':
                print('read from hdd')
                err = 'hdd'
                #break

            elif menu_choice == '3':
                print('printing memory')
                err = 'memory'
                #break

            elif menu_choice == '4':
                print('exiting')
                err = 'exiting'
                break

            else:
                err = 'Wrong input.' 


    
        



