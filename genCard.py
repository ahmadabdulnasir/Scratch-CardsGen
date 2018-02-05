#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__author__ = 'Ahmad Abdulnasir <dabolinux@gmail.com>'
__copyright__ = 'Copyright (c) 2016, salafi'
__version__ = "0.01t"
"""

import uuid, time
from datetime import datetime
from sys import exit
#from math import pi
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
    print("Welcome to Scrath Card Generator \n\t DaboLinux(c)2017\n\t Contact: www.dabolinux.com dabolinux@gmail.com")
    try:
        amt = int(input("\n\tHow Many cards do you wants to generate?\n\t : "))
    except ValueError:
        print("Error!! Only Numbers are accepted")
        gencard()
    txtfile = open(filetxt, 'a+')
    htmlfile = open(filehtml, 'a+')
    txtfile.write('Serial --------- Pin'+'\n')
    htmlfile.write(head+'\n')
    for i in range(0,amt):
        print("Generating {} of {} Scratch Card(s)".format(i+1, amt))
        pin = genpin()
        serial = genserial()
        card = card = '''<p style="margin-bottom: 0cm"><font color="#ffffff"><font size="4" style="font-size: 14pt"><b><span style="background: #000000">%s &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp Scratch Card </span></b></font></font></p><p style="margin-bottom: 0cm"><i>%s</i> &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp</p><p style="margin-bottom: 0cm"><font size="4" style="font-size: 14pt"><b>Pin:  %s</b></font> </p><p style="margin-bottom: 0.5cm"><font size="3" style="font-size: 10pt">Serial: %s</font> <br/><br/></p>''' %("M & B Training Centers", "Goto www.manbcenter.com/apply",pin, serial)
        txtfile.write(serial +'       '+ pin+'\n')
        htmlfile.write(card+'\n')
    txtfile.close()
    htmlfile.close()
    print("*"*40+' Done ' + "*"*40)


head = '''
        <!DOCTYPE html>
        <head>
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
</html>
       '''



if __name__ == "__main__":
    timestr = time.strftime("%Y-%m-%d-%H.%M.%S") 
    filetxt = timestr + ".txt"
    filehtml = timestr + ".html" # Save the current time and date as writing filename
    gencard()
