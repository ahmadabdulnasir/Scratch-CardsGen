#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__author__ = 'Ahmad Abdulnasir <dabolinux@gmail.com>'
__copyright__ = 'Copyright (c) 2016, salafi'
__version__ = "0.01t"
"""

import uuid
from datetime import datetime
from sys import exit
from math import pi
from random import randint as ran

def genpin():
    '''
    Generate Random alphanumeric Pin
    '''
    hot = uuid.uuid4()
    lpin = str(hot)
    pin = lpin[9:23]
    return pin

def genserial():
    '''
    Generate a numeric Serial numbers
    '''
    dserial = ''
    now = datetime.now()
    dserial += str(now.day)
    dserial += str(now.year)
    dserial += str(now.month)
    dserial += str(now.second)
    serial = int(dserial[::-1])+ran(1995,2018)
    return str(serial)
def gencard():
    '''
    Generate the card
    '''
    for i in range(0,10):
        print(genpin(), genserial())


if __name__ == "__main__":
    gencard()