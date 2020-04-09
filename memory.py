#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Marius Pozniakovas, Tomas Kučejevas"
__email__ = "pozniak.marius@gmail.com"

import interrupts as inte
import os

class Memory:

    register_addresses = {
        #system
        'PTR'   :   '00',
        'IC'    :   '01',
        'MODE'  :   '02',
        #interrupts
        'TI'    :   '10',
        'SI'    :   '11',
        'PI'    :   '12',
        'IOI'   :   '13',
        #channel registers
        'CH1'   :   '20',
        'CH2'   :   '21',
        'CH3'   :   '22',
        #random usage
        'RA'    :   '30',
        'RB'    :   '31',
        'RC'    :   '32',
        'C'     :   '33'}

    NO_ARG_FUNCTIONS = ['ADD', 'SUB', 'CMP', 'OUT']
    TWO_ARG_FUNCTIONS = ['JP', 'JE', 'JG', 'RDW', 'RDI', 'RMW', 'RMI', 'MRW', 'MRI']

    

    def __init__(self):
        
        #create all the memory numbers in HEX
        memory_key = []
        for i in range(0, 256):
            for j in range(0, 4):
                index = (str(format(i, 'x')).upper() + str(j))
                memory_key.append(index)
        
        #create all the 0 
        memory_data = [str(0000).zfill(4)] * len(memory_key)
        
        #add them up
        self.memory = dict(zip(memory_key, memory_data))

    def change_memory(self, loc, new_data):
        '''change memory on loc with new_data'''
        self.memory[loc] = str(new_data)
    
    def print_registers(self):
        '''prints registers'''

        os.system('cls')
        print('------   Registers   -------')
        print('----------------------------')
        print('PTR \t\t\t ', self.get_register('PTR'))
        print('MODE \t\t\t ', self.get_register('MODE'))
        print('IC \t\t\t ', self.get_register('IC'))
        print('----------------------------')
        print('TI \t\t\t ', self.get_register('TI'))
        print('SI \t\t\t ', self.get_register('SI'))
        print('PI \t\t\t ', self.get_register('PI'))
        print('IOI \t\t\t ', self.get_register('IOI'))
        print('----------------------------')
        print('RA \t\t\t ', self.get_register('RA'))
        print('RB \t\t\t ', self.get_register('RB'))
        print('RC \t\t\t ', self.get_register('RC'))
        print('C \t\t\t ', self.get_register('C'))
        print('----------------------------')
        print('CH1 \t\t\t ', self.get_register('CH1'))
        print('CH2 \t\t\t ', self.get_register('CH2'))
        print('CH3 \t\t\t ', self.get_register('CH3'))
        print('----------------------------')
        
        return

    def print_memory(self):
        '''prints all the memory in a good way'''
        os.system('cls')
        counter = 1
        print('-------------------------- Memory ---------------------------')
        for key, value in self.register_addresses.items():
            if counter != 2:
                print(key, ' : ', value, end = '\t\t')
                counter = counter + 1
            else:
                print(key, ' : ', value)
                counter = 1
        print('-------------------------------------------------------------')
        counter = 1
        for key, value in self.memory.items():
            if counter != 4:
                print(key, ' : ', value, end = '\t')
                counter = counter + 1
            elif counter == 4:
                print(key, ' : ', value)
                counter = 1

    def get_memory(self, loc):
        return self.memory[loc]

    def get_register(self, name):
        '''returns int value of wanted register'''
        try:
            reg_value = int(self.memory[self.register_addresses[name.upper()]]) 
            return reg_value
        except KeyError:
            return None

    def set_register(self, name, new_value):
        '''changes register value by name'''
        try:
            self.memory[self.register_addresses[name.upper()]] = str(new_value).zfill(4)
            return
        except KeyError:
            return
    
    def save_code_to_memory(self, code):
        '''saves one line of code to registers'''
        
        #get the first word of the code
        code = code.split()
        first_word = code[0]

        #we always encode it
        save_hex = first_word.encode('utf-8').hex()

        #also add numbers if its a two arg function
        if first_word in self.TWO_ARG_FUNCTIONS:
            save_hex = str(format(int(code[1]), 'x')).upper() + str(format(int(code[2]), 'x')).upper() + save_hex

        #add a space
        save_hex = save_hex + '..'

        #take it to memory
        for index in range(0, len(save_hex), 2):
            byte = (save_hex[index] + save_hex[index+1])
            print(byte, 'to', self.get_register('PTR'))
            self.change_memory(str(self.get_register('PTR')), byte.zfill(4))
            self.set_register('PTR', self.get_register('PTR') + 1)
            



        return   
