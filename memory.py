#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Marius Pozniakovas, Tomas Kučejevas"
__email__ = "pozniak.marius@gmail.com"

import interrupts as inte

class Memory:

    
    def __init__(self, memory_start):
        
        memory_key = []
        for i in range(memory_start, memory_start + 32):
            for j in range(0, 4):
                index = str(i).zfill(2) + '-' + str(j)
                memory_key.append(index)

        memory_data = [str(0000).zfill(4)] * len(memory_key)
        self.memory = dict(zip(memory_key, memory_data))
        
    # def check_size(self, var):
    #     '''checks size'''
    #     if(var > pow(2,32)):
    #         inte.PI_interrupt()
    #         sys.exit("Variable overflow, exiting")
    #     else:
    #         pass

