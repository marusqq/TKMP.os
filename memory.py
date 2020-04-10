#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Marius Pozniakovas, Tomas Kučejevas"
__email__ = "pozniak.marius@gmail.com"

import interrupts as inte
import os

class Memory:

    register_addresses = {
        #system
        'PTR'   :   '0000',
        'IC'    :   '0001',
        'MODE'  :   '0002',
        #interrupts
        'TI'    :   '0010',
        'SI'    :   '0011',
        'PI'    :   '0012',
        'IOI'   :   '0013',
        #channel registers
        'CH1'   :   '0020',
        'CH2'   :   '0021',
        'CH3'   :   '0022',
        #random usage
        'RA'    :   '0030',
        'RB'    :   '0031',
        'RC'    :   '0032',
        'C'     :   '0033'}

    NO_ARG_FUNCTIONS = ['ADD', 'SUB', 'CMP', 'OUT']
    TWO_ARG_FUNCTIONS = ['JP', 'JE', 'JG', 'RDW', 'RDI', 'RMW', 'RMI', 'MRW', 'MRI']

    

    def __init__(self):
        
        #create all the memory numbers in HEX
        memory_key = []
        for i in range(0, 256):
            for j in range(0, 4):
                index = (str(format(i, 'x')).upper() + str(j)).zfill(4)
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
        print('------------------------ Registers --------------------------')
        counter = 1
        for key, value in self.memory.items():
            if counter != 4:
                print(key, ' : ', value, end = '\t')
                counter = counter + 1
            elif counter == 4:
                print(key, ' : ', value)
                counter = 1
            
            if key == '0033':
                print('----------------------- Code Memory Below -------------------')
            elif key == '09F3':
                print('----------------------- Usable memory -----------------------')

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
        save_hex = first_word.encode('utf-8').hex().upper()

        #also add numbers if its a two arg function
        if first_word in self.TWO_ARG_FUNCTIONS:
            save_hex = save_hex + str(format(int(code[1]), 'x')).upper() + str(format(int(code[2]), 'x')).upper()

        #add a space
        save_hex = save_hex + '..'

        times_added = 0

        #take it to memory
        for index in range(0, len(save_hex), 2):
            
            #take hexed chars
            byte = save_hex[index] + save_hex[index+1]
                
            if times_added == 0:
                full_byte = byte
                times_added = times_added + 1

            elif times_added == 1:
                full_byte = full_byte + byte
                times_added = 0
                self.change_memory(str(self.get_memory(self.register_addresses['PTR'])), full_byte)
                self.move_to_another_memory_cell()

        return

    def move_to_another_memory_cell(self):
        '''checks if the next memory cell is ok'''

        current_ptr = (self.get_memory(self.register_addresses['PTR']))
        #current_ptr = 'E52'
        #for example if we have E52
        front = current_ptr[:-1] #this will be E5
        end_last = current_ptr[-1] #this will be 2
        
        #check if end is 0,1,2, if yes add one more
        #if end is 3, we can't add one more, so we add in the first part
        
        if end_last in ('0','1','2'):
            number = front + str(int(end_last) + 1)
            self.set_register('PTR', number)
            
        else:
            hex_value = (int(front, base = 16)) + 1
            number = (str(format(hex_value, 'x')).upper()) + '0'
            self.set_register('PTR', number)
  
    def read_memory_for_code(self):
        '''reads memory and finds a code part'''
        #(str(self.get_memory(self.register_addresses['PTR'])))
        word = ''

        while True:
            
            #get two letters
            command = self.get_memory((str(self.get_memory(self.register_addresses['PTR']))))

            #i think we found no code
            if command == '0000':
                return None
            
            first_part, second_part = command[:int(len(command)//2)], command[int(len(command)//2):]

            #this is a space after code
            if first_part != '..':
                first_word = chr(int(first_part, 16))
                word = word + first_word
            
            else:
                self.move_to_another_memory_cell()
                break
            
            if second_part != '..':
                second_word = chr(int(second_part, 16))
                word = word + second_word
            
            else:
                self.move_to_another_memory_cell()
                break

            self.move_to_another_memory_cell()

        return word