#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Marius Pozniakovas, Tomas Kučejevas"
__email__ = "pozniak.marius@gmail.com"


class VM:
    
    def __init__(self):
        super().__init__()


    def task(self, command):
        print("Command used: ", command)
        
        if command is None:
            print('None. This is bad.')
        
        elif command == 'CODE':
            print('CODE starting')

        elif command == 'HALT':
            print("code HALTed")

        elif command == 'ADD':
            print('adding')

    