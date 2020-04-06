#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Marius Pozniakovas, Tomas Kučejevas"
__email__ = "pozniak.marius@gmail.com"

import os
import real_machine as RM

DEBUG = False

class VM:
    
    def __init__(self, rm):
        self.rm = rm


    def execute(self, command):
        
        commands = command.split()
        
        if DEBUG:
            print("\tCommands used: ", commands)

        if commands[0] == 'CODE' and len(commands) == 1:
            print('DONT DELETE THIS IF WE GET HERE code IN VIRTUAL_MACHINE.EXECUTE')
        
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
        
        #3.5.3.4
        elif commands[0] == 'HALT':
            print('DONT DELETE THIS IF WE GET HERE halt IN VIRTUAL_MACHINE.EXECUTE')

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

    def collect_input(self):

        VM.consoleInfo(self)
        code = []
        coding = False
        os.system('cls')

        print('------     Console      -------')
        #listen to all commands
        while True:
            _input = input()

            #check if the functions are legit
            if VM.check_functions(self, _input):

                #if we started collecting code snippet
                if coding:
                    
                    #finishing code snippet
                    if _input == 'HALT':
                        coding = False
                        print('----------------------------------')
                        VM.run_code(self, code)
                        print('----------------------------------')
                        print('Press enter to return to main menu')
                        _input = input()
                        break
                    
                    #adding code to code snippet
                    else:
                        code.append(_input)

                #if we were not collecting code snippet, but we will start now
                elif _input == 'CODE':
                    
                    print("(Now enter your code and enter HALT to finish)")
                    if DEBUG:
                        print('\tStarting to collect CODE')
                    
                    coding = True

                #if we were not collecting code snippet, but we want to exit the console
                elif _input == 'HALT':
                    print('Press enter to return to main menu')
                    _input = input()
                    break
                
                #if we were not collecting code snippet and there is no special command, just execute it
                else:
                    VM.run_code(self, _input, single = True)

            #bad syntax of function
            else:
                print('Bad function input...')

    def run_code(self, code, single = False):
        
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

    def check_functions(self, words_of_code):
        '''function to check input and return true if everything is ok'''
        
        words_of_code = words_of_code.split()
        if DEBUG:
            print('\tChecking this =>', words_of_code, len(words_of_code))
        
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

    def consoleInfo(self):
        os.system('cls')
        print('There is two ways to enter the code:')
        print('1. Just enter command after command and it will be compiled after each line.\nHALT to exit\n')
        print('2. Start by entering CODE and then enter commands in each line and finish with HALT.\nThen all block will be executed instantly\n')
        _input = input('Press enter to continue\n')

        return

