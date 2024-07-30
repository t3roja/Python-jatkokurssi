from tkinter import *
import sqlite3
db_file='my_db.db'
con = sqlite3.connect(db_file)
cur = con.cursor()
count = 0
res = cur.execute('SELECT data FROM textdata')
res = res.fetchall()
max = len(res)

root = Tk()

lbl = Label(root, text="")
lbl.pack()

def click():
    global count
    txt = res
    if count == max:
        count = 0

        lbl.config(text=txt[count])
        count += 1
    else:

        lbl.config(text=txt[count])
        count += 1

btn = Button(root, text="Button", command=click)
btn.pack()

#Don't modify lines below
if __name__ == "__main__":
    root.mainloop()


"""
Toteuta ohjelma, joka lukee SQLite-tietokannasta my db.db
taulusta textdata tietoja kyselyllä
SELECT data FROM textdata;
Ohjelman käyttöliittymässä on Label-tyyppinen objekti lbl ja
nappi btn. Painettaessa nappia labeliin haetaan kyselyst¨a
seuraavalla rivillä oleva arvo123. Viimeisen arvon jälkeen
aloitetaan taas ensimmäisestä arvosta. Ohjelman käynnistyessä
lbl on tyhjä.
"""