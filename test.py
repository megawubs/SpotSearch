# File: toolbar1.py

from Tkinter import *

root = Tk()

Lb1 = Listbox(root)
Lb1.insert(1, 'Python')
Lb1.insert(2, 'PHP')
Lb1.insert(3, 'JavaScript')
Lb1.insert(4, 'Objective-c')


Lb1.pack()
root.mainloop()