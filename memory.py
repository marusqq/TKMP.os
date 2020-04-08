#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Marius Pozniakovas, Tomas Kučejevas"
__email__ = "pozniak.marius@gmail.com"

import interrupts as inte

class Memory:

    def __init__(self):
        super().__init__()

    def check_size(self, var):
        '''checks size'''
        if(var > pow(2,32)):
            inte.PI_interrupt()
            sys.exit("Variable overflow, exiting")
        else:
            pass