#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__author__ = 'Ahmad Abdulnasir <dabolinux@gmail.com>'
__copyright__ = 'Copyright (c) 2018, salafi'
__version__ = "0.01t"
"""
import sqlite3
import time, os, sys


j = sys.argv
k = j[0].split('/')
go = k[1:-1]
moo = '/'.join(go)
#wsp = '/'+moo #droid only
#os.chdir(wsp) #droid only

mbdb ='tee.db'
wsp = os.getcwd()
print(wsp)
timestr = time.strftime("%Y-%m-%d-%H.%M.%S") 
filehtml = timestr + ".html" # Save the current time and date as writing filename
filetxt = timestr + 'txt'
def fileinfo():
    global con, db
    if os.path.isfile(mbdb):
        con = sqlite3.connect(mbdb)
        db = con.cursor()
        print('Green')
        sqlcmd = '''CREATE TABLE IF NOT EXISTS `cards` (
	`sn`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`pin`	TEXT NOT NULL,
	`serial`	TEXT NOT NULL,
	`email`	TEXT NOT NULL DEFAULT 'students@mandbcenter.com',
	`used`	INTEGER NOT NULL DEFAULT 'No'
) '''
        db.execute(sqlcmd)
    else:
        print("Error Unknown Database. Ko Kayi formating din wayar ka ne?")
        ans = input("1. Eh nayi formating/restore\n2. A'a Banyi komai ba\v : ")
        if ans in ['1', 'eh', 'yes', 'y']:
            print("Ka nemi Developer din a dabolinux@gmail.com")
        else:
            print("Kayi reboot na wayar ka sake gwadawa")
            sys.exit(1)
def delete(card):
    db.execute("DELETE FROM cards WHERE pin=?", (card))
    con.commit()

def update(card):
    sqlcmdU = "UPDATE cards SET used='Yes' WHERE serial='"+ card+"'" #.format(card)
    #print(sqlcmdU)
    #db.execute("UPDATE cards SET used='Yes' WHERE serial=?",(card))
    db.execute(sqlcmdU)
    con.commit()
    
def getcard():
    card = db.execute("SELECT sn,pin,serial FROM cards where used='No'").fetchone()
    return card
goma = 'zxcvbnm45'
def gencard():
    '''
    Generate the card
    '''
    os.system('clear')
    print("Welcome to Scrath Card Generator \n\t DaboLinux(c)2017\n\t Contact: www.dabolinux.com")
    tam = input("Password : ")
    if tam == goma:
        os.system('clear')
        pass
    else:
        print("Wrong Password!!!")
        time.sleep(2)
        sys.exit(1)
    #try:
        amt = int(input("\n\tScracth Card guda nawa zan hada?\n\t : "))
    #except ValueError:
    #    print("Error!! Namba kawai zaka rubuta na gane")
    #    time.sleep(1.5)
        gencard()
    txtfile = open(filetxt, 'w')
    htmlfile = open(filehtml, 'a+')
    txtfile.write('Serial --------- Pin'+'\n')
    htmlfile.write(head+'\n')
    kirga = 0
    for i in range(0,100):
        print("Generating {} of {} Scratch Card(s)".format(i+1, 100))
        card = getcard()
        sn = card[0]
        pin = card[1]
        serial = card[2]
        yanzu = time.strftime("%Y-%m-%d %H:%M")
        cardone = '''
        <div>
        <h3><span style="background: #000000 color=#ffffff">M & B Training Centers &nbsp &nbsp  &nbsp Online</span></h3>
        <span><i>Goto www.mandbcenter.com/apply</i></span> &nbsp &nbsp  &nbsp <span> %s </span>
        <h3> <b>Pin:  %s </b></h3>
        <h6> <span> Serial: %s </span> <span>Date:  %s </span> </h6> 
        </div> <br /> 
        ''' %( sn,pin, serial,yanzu)
        htmlfile.write(cardone+'\n')
        kirga = kirga + 1
        if kirga in [5,15,25,35,45,55,65,75,85,95]:
            htmlfile.write(leftseg)
        elif kirga in [10,20,30,40,50,60,70,80,90,100]:
            htmlfile.write(righseg)
        update(serial)  # Mark the Card as Used
    txtfile.write(serial +'           '+ pin+' last fetch: '+str(sn)+'\n')
    txtfile.close()
    htmlfile.close()
    print("*"*20+' Done ' + "*"*20)
    print("Saved in " + filehtml)
    con.commit()
    db.close()
    con.close()
leftseg = '''
    </div> <br />
    
    <div class="right">'''
righseg = '''
</div> <br />

<hr />
<div class="left">
<br />
'''

head = '''
<!DOCTYPE html>
<head>
<html lang="en">
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8"/>
<title></title>
<style type="text/css">
@page { size: 21cm 29.7cm }
    .right {
        float: right;
        margin-left: auto;
        margin-right: auto;
        width: 50%;
    }
    .left {
        float: left;
        margin-left: auto;
        margin-right: auto;
        width: 50%;
    }
    </style>
</head>

<body>

<div class="left">
<br />
 ''' 

tail= ''' </body>
</html>
       '''
if __name__ == "__main__":
    fileinfo()
    gencard()
