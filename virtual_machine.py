#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Marius Pozniakovas, Tomas Kučejevas"
__email__ = "pozniak.marius@gmail.com"

import os

class VM:
    
    def __init__(self):
        super().__init__()


    def execute(self, command):
        
        print("\tCommand used: ", command)
        commands = command.split()

        if commands[0] == 'CODE' and len(commands) == 1:
            print('\tCollecting code....')

        
        #3.5.1
            '''data moving'''
        #3.5.1.1
        elif commands[0] == 'RMW':
            print('\t read the word in XY and put it to RA and RB as word')

        #3.5.1.2
        elif commands[0] == 'RMI':
            print('\t read the word in XY and put it in RA and RB as number')

        #3.5.2 
            '''arythmetic commands'''
        #3.5.2.1
        elif commands[0] == 'ADD':
            print('\t adding RA + RB to RC')

        #3.5.2.2
        elif commands[0] == 'SUB':
            print('\t removing RA - RB to RC')

        #3.5.2.3    
        elif commands[0] == 'CMP':
            print('\t compares RA and RB')

        #3.5.3
            '''control commands'''
        #3.5.3.1
        elif commands[0] == 'JP':
            print('\t jumps to xy')
        
        #3.5.3.2
        elif commands[0] == 'JE':
            print('\t jumps to xy. if c == 0')

        #3.5.3.3
        elif commands[0] == 'JG':
            print('\t jumps to xy. if c == 1')
        
        #3.5.3.4
        elif commands[0] == 'HALT':
            print('Halt should be entered after CODE')

        #3.5.4
            '''input / output commands'''
        #3.5.4.1
        elif commands[0] == 'OUT':
            print('\toutputing RC')

        elif commands[0] == 'RDW':
            print('\treading input and putting it in RA, RB as symbols')

        elif commands[0] == 'RDI':
            print('\treading input and putting it in RA, RB as numbers') 
        
        else:
            print('\tWrong input!')

        return command

    def collect_input(self):
        os.system('cls')
        code = []
        coding = False

        print('------     Console      -------')
        while True:
            _input = input()
            if VM.check_functions(self, _input):

                if coding:
                    
                    if _input == 'HALT':
                        coding = False
                        print('----------------------------------')
                        VM.run_code(self, code)
                        print('----------------------------------')
                        print('Press enter to return to main menu')
                        _input = input()
                        break

                    else:
                        code.append(_input)

                elif _input == 'CODE':
                    print('\tStarting to collect CODE')
                    coding = True
                    
                else:
                    VM.run_code(self, _input, single = True)

            else:
                print('Bad input...')

    def run_code(self, code, single = False):
        
        if single:
            print('running single line of code...')
            #print(code)
            VM.execute(self, code)
            return
        else:
            print('running more than a single line of code')
            for line in code:
                print(line)
                VM.execute(self, line)

    def check_functions(self, words_of_code):
        '''function to check input and return true if everything is ok'''
        
        words_of_code = words_of_code.split()
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
        elif words_of_code[0] == 'RDW' and len(words_of_code) == 3:
            return True
        elif words_of_code[0] == 'RDI' and len(words_of_code) == 3:
            return True
        #--------------
        else:
            return False
        
    #def _add(self, ra, rb)


