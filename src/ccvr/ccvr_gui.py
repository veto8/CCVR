#!/usr/bin/env python

from tkinter import *
from tkinter import ttk
from ccvr import Ccvr 

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
c = Ccvr()
c.check()

root.mainloop()
