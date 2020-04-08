#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Marius Pozniakovas, Tomas Kučejevas"
__email__ = "pozniak.marius@gmail.com"

import os
import real_machine as RM
import memory as mem
import interrupts as inte

DEBUG = False

class VM:
    
    def __init__(self, rm):
        self.rm = rm
        self.codes = None

    def execute(self, command):
        '''execute command depending on what you send'''
        
        commands = command.split()
        
        if DEBUG:
            print("\tCommands used: ", commands)
        
        #3.5.1
            '''data moving'''
        #3.5.1.1
        elif commands[0] == 'RMW':
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
        
        else:
            print('\tWrong input!')

        return command
                    
    def collecting_console_code(self, memory_start, memory_end):
        '''function to wait for HALT and collect code lines'''
        
        code_line = input()
        
        while True:
            if code_line != 'HALT':
                self.codes.append(code_line)
                code_line = input()
            else:
                VM.run_code(self, code=codes, single=False)
                print('Press enter to return to main menu')
                _input = input()
                break

    def console(self, mode = 'quit'):
        '''splits console to modes and continues the workflow'''

        print('------     Console      -------')

        #SINGLE LINE MODE
        if mode == '1':
            while True:
                _input = input()
                
                #check for syntax errors
                int_value = inte.PI_interrupt(obj = self.rm, codes = _input, modes = 'operation')
                if int_value is not None:
                    break
                
                #exit with HALT
                elif _input == 'HALT':
                    print('Press enter to return to main menu')
                    _input = input()
                    break

                #execute any function if it syntax is ok
                else:
                    VM.run_code(self, _input, single=True)

        #MULTI LINE MODE
        elif mode == '2':
            while True:
                _input = input()

                #start with CODE
                if _input == 'CODE':
                    #VM.collecting_console_code(memory_start, memory_end)
                    VM.collecting_console_code(self, 0000, 8000)
                    break

                #not started with CODE
                else: 
                    print('You must start with CODE')
                    #PI = 1
        
        elif mode == 'quit':
            return

    def start_console(self):
        '''script to start the console, takes no arguments'''

        consoleMode = VM.consoleInfo(self)
        VM.console(self, mode = consoleMode)

    def run_code(self, code, single = False):
        '''runs the code sent, if more than one code line is sent
        single = False, then cycles through code lines and executes them'''
        
        if single:
            if DEBUG:
                print('running single line of code...')
            VM.execute(self, code)
            return
        else:
            if DEBUG:
                print('running more than a single line of code')
            for line in code:
                VM.execute(self, line)
            return

    def consoleInfo(self):
        '''function to choose console mode'''

        while True:
            os.system('cls')
            print('There is two ways to enter the code:')
            print('1. Just enter command after command and it will be compiled after each line.\nHALT to exit\n')
            print('2. Start by entering CODE and then enter commands in each line and finish with HALT.\nThen all block will be executed instantly\n')
        
            _input = input('Enter mode to use: \n')
            if _input == '1' or _input == '2':
                os.system('cls')
                return _input

