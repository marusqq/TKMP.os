#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Marius Pozniakovas, Tomas Kučejevas"
__email__ = "pozniak.marius@gmail.com"

import interrupts as inte
import os

class Memory:

    register_addresses = {
        #system
        'PTR'   :   '0-0',
        'IC'    :   '0-1',
        'MODE'  :   '0-2',
        #interrupts
        'TI'    :   '1-0',
        'SI'    :   '1-1',
        'PI'    :   '1-2',
        'IOI'   :   '1-3',
        #channel registers
        'CH1'   :   '2-0',
        'CH2'   :   '2-1',
        'CH3'   :   '2-2',
        #random usage
        'RA'    :   '3-0',
        'RB'    :   '3-1',
        'RC'    :   '3-2',
        'C'     :   '3-3'
    }

    def __init__(self):
        
        #create all the memory numbers in HEX
        memory_key = []
        for i in range(0, 256):
            for j in range(0, 4):
                index = (str(format(i, 'x')).upper() + '-' + str(j))
                memory_key.append(index)
        
        #create all the 0 
        memory_data = [str(0000).zfill(4)] * len(memory_key)
        
        #add them up
        self.memory = dict(zip(memory_key, memory_data))

    def change_memory(self, loc, new_data):
        '''change memory on loc with new_data'''
        self.memory[loc] = str(new_data)
    
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
        