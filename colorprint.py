#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from colorama import init
init()
from colorama import Fore, Back, Style

class ColorPrint:
    
    def __getattr__(self, name):
        pass

    @staticmethod
    def printRed(*string, sep=' ', end='\n', file=sys.stdout):
        print(Fore.RED, sep='', end='')
        print(*string, sep=sep, end=end, file=file, flush=True)
        print(Style.RESET_ALL, end='', flush=True)

    @staticmethod
    def printGreen(*string, sep=' ', end='\n', file=sys.stdout):
        print(Fore.GREEN, sep='', end='')
        print(*string, sep=sep, end=end, file=file, flush=True)
        print(Style.RESET_ALL, end='', flush=True)

    @staticmethod
    def printBlue(*string, sep=' ', end='\n', file=sys.stdout):
        print(Fore.BLUE, sep='', end='')
        print(*string, sep=sep, end=end, file=file, flush=True)
        print(Style.RESET_ALL, end='', flush=True)

if __name__ == '__main__':
    ColorPrint.printRed('This is red.')
    ColorPrint.printGreen('This is green.')
    ColorPrint.printBlue('This is blue.')
