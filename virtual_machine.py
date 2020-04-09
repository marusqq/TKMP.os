#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Marius Pozniakovas, Tomas Kučejevas"
__email__ = "pozniak.marius@gmail.com"

import os
import real_machine as RM
import sys
import interrupts as inte


class VM:
    
    def __init__(self, rm):
        self.rm = rm
        self.codes = []

    def execute(self, command):
        '''execute command depending on what you send'''
        
        commands = command.split()
        
        #3.5.1
        '''data moving'''
        #3.5.1.1
        if commands[0] == 'RMW':
            '''TODO: Pridet XY'''
            self.rm._rmw()
        #3.5.1.2
        elif commands[0] == 'RMI':
            '''TODO: Pridet XY'''
            self.rm._rmi()
            
        #3.5.2 
            '''arythmetic commands'''
        #3.5.2.1
        elif commands[0] == 'ADD':
            self.rm._add()
        #3.5.2.2
        elif commands[0] == 'SUB':
            self.rm._sub()
        #3.5.2.3    
        elif commands[0] == 'CMP':
            self.rm._cmp()

        #3.5.3
            '''control commands'''
        #3.5.3.1
        elif commands[0] == 'JP':
            '''TODO: Implement'''
            #jumps to xy
            self.rm._jp()
        
        #3.5.3.2
        elif commands[0] == 'JE':
            '''TODO: Implement'''
            #jumps to xy. if c == 0
            self.rm._je()

        #3.5.3.3
        elif commands[0] == 'JG':
            '''TODO: Implement'''
            #jumps to xy. if c == 1
            self.rm._jg()

        #3.5.4
            '''input / output commands'''
        #3.5.4.1
        elif commands[0] == 'OUT':
            self.rm._out()

        elif commands[0] == 'RDW':
            '''TODO: to test this'''
            self.rm._rdw(commands[1], commands[2])

        elif commands[0] == 'RDI':
            self.rm._rdi(commands[1], commands[2])

        return command
                    
    def collecting_console_code(self, memory_start, memory_end):
        '''function to wait for HALT and collect code lines'''
        
        code_line = input()
        self.rm.mem.save_code_to_memory(code_line)
        quit("quit")

        while True:
            if code_line != 'HALT':
                self.codes.append(code_line)
                code_line = input()
            else:
                VM.run_code(self, code=self.codes, single=False)
                break

    def console(self, mode = 'quit'):
        '''splits console to modes and continues the workflow'''

        print('------     Console      -------')

        #SINGLE LINE MODE
        if mode == '1':
            while True:
                _input = input()
                
                #exit with HALT
                if _input == 'HALT':
                    print('Press enter to return to main menu')
                    _input = input()
                    break
                elif _input == 'STOP':
                    '''TODO: move this to interrupts.py'''
                    if(self.rm.mem.get_register('MODE') == 0):
                        sys.exit('Stopping the machine')
                    else:
                        print('Insufficient privileges')
                #execute any function if it syntax is ok
                else:
                    VM.run_code(self, _input, single=True)
                    break

        #MULTI LINE MODE
        elif mode == '2':
            while True:
                _input = input()

                #start with CODE
                if _input == 'CODE':
                    VM.collecting_console_code(self, 0000, 8000)
                    break

                #not started with CODE
                else:
                    int_value = inte.PI_interrupt(obj = self.rm, codes = 'NOT_STARTED_WITH_CODE', modes = 'operation')
                    if int_value is not None:
                        break
                
        elif mode == 'quit':
            return

    def start_console(self):
        '''script to start the console, takes no arguments'''

        consoleMode = VM.consoleInfo(self)
        VM.console(self, mode = consoleMode)

    def run_code(self, code, single = False):
        '''runs the code sent, if more than one code line is sent
        single = False, then cycles through code lines and executes them'''
        
        #check for bad functions ant throw an interrupt
        inte.PI_interrupt(self.rm, modes = 'operation', codes = code, single_line=single)

        #single line of code, mode = 1
        if single:
            VM.execute(self, code)

        #multiline code, mode = 2
        else:
            for line in code:
                VM.execute(self, line)
        
        _input = input('Press enter to return to main menu\n')
        return

    def consoleInfo(self):
        '''function to choose console mode'''

        while True:
            os.system('cls')
            print('There is two ways to enter the code:')
            print('1. Just enter command after command and it will be compiled after each line.\nHALT to exit, STOP to stop the machine (supervisor only)\n')
            print('2. Start by entering CODE and then enter commands in each line and finish with HALT.\nThen all block will be executed instantly\n')
        
            _input = input('Enter mode to use: \n')
            if _input == '1' or _input == '2':
                os.system('cls')
                return _input

