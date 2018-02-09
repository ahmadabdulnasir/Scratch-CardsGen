import sqlite3


con = sqlite3.connect('mandbcenter.db') 
db = con.cursor() 
sqlcmdint = '''CREATE TABLE IF NOT EXISTS `cards` (
	`sn`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`pin`	TEXT NOT NULL,
	`serial`	TEXT NOT NULL,
	`email`	TEXT NOT NULL DEFAULT 'students@mandbcenter.com',
	`used`	INTEGER NOT NULL DEFAULT 'No'
) '''
db.execute(sqlcmdint)
j = db.execute('SELECT * FROM cards').fetchall()
con.commit()
db.close()
con.close()
#commit
print(j)