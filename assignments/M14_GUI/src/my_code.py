"""
Example 1

% python3 my_code.py 
Enter mainloop()
>m
"Hello World!" have been printed 1 times!
>m
"Hello World!" have been printed 2 times!
>q
"q" not found from events list!
>x
Exit mainloop()

-----------------------------------------------------------------
Example 2

% python3 my_code.py
Enter mainloop()
>m
"Hello World!" have been printed 1 times!
>r
Number of empty rows:3



>m
"Hello World!" have been printed 2 times!
>r
Number of empty rows:1

>x
Exit mainloop()
"""


######################################
#
# Don't touch the main loop and related variables
events={}
active_mainloop=True
m_presses = 0

def mainloop():
    init_mainloop()

    print('Enter mainloop()')
    while active_mainloop:
        k=input('>')
        if k!='':
            if k in events:
                f=events[k]
                f()
            else:
                print(f'"{k}" not found from events list!')
    print('Exit mainloop()')
######################################

#Event handling function
def event_exit():
    global active_mainloop
    active_mainloop=False

def m_pressed():
    global m_presses
    m_presses = m_presses + 1
    print(f'"Hello World!" have been printed {m_presses} times!')

def r_pressed():
    try:
        rows = int(input("Number of empty rows:"))
    except:
        return
    else:
        for _ in range(rows):
            print()
#Implement functions, variables etc to handle events here.



def init_mainloop():
    global events
    events={}
    events['x']=event_exit
    events['m']=m_pressed
    events['r']=r_pressed
    

    #Add functions to events dict here.


######################################
#
#Don't modify lines below
if __name__ == "__main__":
    mainloop()
