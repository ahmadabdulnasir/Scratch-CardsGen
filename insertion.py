import sqlite3

con = sqlite3.connect('mandbcenter.db')
db = con.cursor()

fo = open('dododo.txt')

for i in fo.readlines():
    spam = i.split()
    pin = spam[1]#.replace('','\n')
    serial = spam[0]
    db.execute("INSERT INTO cards(pin,serial) VALUES(?,?)", (pin,serial) )


con.commit()
db.close()
con.close()
fo.close()