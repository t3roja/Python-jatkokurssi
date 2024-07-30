from tkinter import *
import math

def solve_quadratic():
    try:

        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())


        discriminant = b**2 - 4*a*c
        
        if discriminant < 0:
            # No real roots
            label_root1.config(text='-')
            label_root2.config(text='-')
        else:

            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            

            label_root1.config(text=f'{root1:.2f}')
            label_root2.config(text=f'{root2:.2f}')
            
    except ValueError:

        label_root1.config(text='-')
        label_root2.config(text='-')

root = Tk()
root.title("Quadratic Equation Solver")

Label(root, text="a:").grid(row=0, column=0)
entry_a = Entry(root)
entry_a.grid(row=0, column=1)

Label(root, text="b:").grid(row=1, column=0)
entry_b = Entry(root)
entry_b.grid(row=1, column=1)

Label(root, text="c:").grid(row=2, column=0)
entry_c = Entry(root)
entry_c.grid(row=2, column=1)

btn = Button(root, text="Solve", command=solve_quadratic)
btn.grid(row=3, column=0, columnspan=2)

Label(root, text="Root 1:").grid(row=4, column=0)
label_root1 = Label(root, text="-")
label_root1.grid(row=4, column=1)

Label(root, text="Root 2:").grid(row=5, column=0)
label_root2 = Label(root, text="-")
label_root2.grid(row=5, column=1)

# Start the main loop
if __name__ == "__main__":
    root.mainloop()



"""
Toteuta ohjelma, jonka avulla saat ratkaistua toisen asteen
yht¨al¨on1 ax2 + bx + c = 0. Ohjelma sisältää kolme
Entry-tyyppistä objektia, joiden nimet ovat entry a, entry b ja
entry c, ja joihin kertoimet a, b ja c syötetään2. Painettaessa
nappia btn ohjelma laskee yhtälön juuret ja esittää ne kahden
desimaalin tarkkuudella Label-tyyppisiss¨a objekteissa3
label root1 ja label root2. Jos juuret eivät ole reaalisia4, niin
labeleihin label root1 ja label root2 asetetaan arvo ’-’.
Samoin toimitaan jos jokin arvoista a, b tai c on virheellinen tai
puuttuu.
"""