#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__author__ = 'Ahmad Abdulnasir <dabolinux@gmail.com>'
__copyright__ = 'Copyright (c) 2016, salafi'
__version__ = "0.01t"
"""

from datetime import datetime
from sys import exit
from math import pi
from random import randint as ran

def genPin():
    dpin = ''
#    sp = '-'
    now = datetime.now()
    dpin = str(now.microsecond)
    dpin += str(now.minute)
    salt = ran(1995,2018)
    dpin += str(now.hour+salt)
    #dpin += str(in))
    pin = dpin[::-1]
    return pin


def genSerial():
    dserial = ''
    now = datetime.now()
    dserial += str(now.day)
    dserial += str(now.year)
    dserial += str(now.month)
    dserial += str(now.second)
    serial = int(dserial[::-1])+ran(1995,2018)
    return str(serial)
 
def genCard():
    talatu = open('output.html', 'a+')
    head = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html>
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8"/>
	<title></title>
	<meta name="generator" content="LibreOffice 5.1.4.2 (Linux)"/>
	<meta name="created" content="Ahmad Abdulnasir (salafi)"/>
	<meta name="changedby" content="Ahmad Abdulnasir"/>
	<meta name="changed" content=" "/>
	<style type="text/css">
		@page { size: 21cm 29.7cm }
	</style>
</head>
<body lang="en-US" dir="ltr"> ''' 
    tail= ''' </body>
</html>'''
    print("Welcome to Scrath Card Generator \n\t DaboLinux(c)2017\n\t www.dabolinux.com")
    try:
        amt = int(input("How Many cards do you wants to generate?\n\t :"))
        cards = ''
    except ValueError:
        print("Error!! Only Numbers are accepted")
        genCard()
        
    for i in range(0,amt):
        pin = genPin()
        serial = genSerial()
        
        card = '''<p style="margin-bottom: 0cm"><font color="#ffffff"><font size="4" style="font-size: 14pt"><b><span style="background: #000000">%s &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp Scrath Card </span></b></font></font></p><p style="margin-bottom: 0cm"><i>%s</i> &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp</p><p style="margin-bottom: 0cm"><font size="4" style="font-size: 14pt"><b>%s</b></font> </p><p style="margin-bottom: 0.5cm"><font size="3" style="font-size: 10pt">%s</font> <br/><br/></p>''' %("M & B Training Centers", "Goto www.manbcenter.com/apply",pin, serial)   
          
        cards += card
          
    talatu.write(cards)
    talatu.close()
    print("*"*45+' Done  '+"*"*45)

    
if __name__ == "__main__":
    genCard()
