from tkinter import *

#Your code here!
root = Tk()

lbl = Label(root, text="Button not pressed!")
lbl.pack()

def click():
    lbl.config(text="Button pressed!")

btn = Button(root, text="btn", command=click)
btn.pack()


#Don't modify lines below
if __name__ == "__main__":
    root.mainloop()


"""
Toteuta ohjelma, joka nappia (btn) painettaessa tulostaa viestin
’Button pressed!’ Label-tyyppiseen objektiin lbl.
Alkutilanteessa lbl sis¨alt¨a¨a tekstin ’Button not pressed!’
"""