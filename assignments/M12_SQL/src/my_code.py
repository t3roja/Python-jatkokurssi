import sqlite3

db_file='my_db.db'
con = sqlite3.connect('my_db.db')
cur = con.cursor()

cur.execute('''CREATE TABLE texttable (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL
);''')
cur.execute('''INSERT INTO texttable (name) VALUES
("Matti"),("Ville"),("Kaisa"),("Mikko");''')
con.commit()
con.close()
"""
Kirjoita ohjelma, joka luo SQLite tietokannan my db.db ja sinne
taulun:
CREATE TABLE texttable (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL
);
Lis¨a¨a tauluun arvot:
INSERT INTO texttable (name) VALUES
("Matti"),("Ville"),("Kaisa"),("Mikko");
"""
