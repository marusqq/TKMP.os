#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Marius Pozniakovas, Tomas Kučejevas"
__email__ = "pozniak.marius@gmail.com"

class Memory:

    def __init__(self, name):
        self.name = name
        print(name)

    def check_size(var):
        if(var > pow(2,32)):
            sys.exit("Variable overflow, exiting")
        else:
            pass