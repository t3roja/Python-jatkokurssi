import sqlite3

db_file = 'my_db.db'
con = sqlite3.connect(db_file)
cur = con.cursor()

res = cur.execute('SELECT name FROM texttable;')

names = res.fetchall()

for name in names:
    print(name) 

con.close()



"""
SQLite tietokannassa my db.db on taulu texttable joka sis¨alt¨a¨a
tuntemattoman m¨a¨ar¨an rivej¨a. Hae taulusta name sarakkeen
kaikki arvot kyselyll¨a
SELECT name FROM texttable;
Tulosta kyselyn palauttamat nimet kukin omalle rivilleen
"""