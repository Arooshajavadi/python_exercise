import tkinter
from tkinter import *


def get_info():
    pass

def reset(event):
    pass

def save_click():
    pass





root = tkinter.Tk()
root.geometry("500x350")
root.title("Inventory")

Product=tkinter.StringVar
tkinter.Label(root, text="Product",textvariable=Product).place(x=40, y=40)
tkinter.Entry(root).place(x=100, y=40)

Count=tkinter.IntVar()
tkinter.Label(root, text="Count",textvariable=Count).place(x=40, y=80)
tkinter.Entry(root).place(x=100, y=80)

Price=tkinter.IntVar()
tkinter.Label(root, text="Price",textvariable=Price).place(x=40, y=120)
tkinter.Entry(root).place(x=100, y=120)

Person=tkinter.StringVar()
tkinter.Label(root, text="Person",textvariable=Person).place(x=40, y=160)
tkinter.Entry(root).place(x=100, y=160)

Invar=tkinter.BooleanVar()
Outvar=tkinter.BooleanVar()
tkinter.Label(root, text="Type").place(x=40, y=200)
tkinter.Checkbutton(root,text="In",variable=Invar).place(x=100, y=200)
tkinter.Checkbutton(root,text="Out",variable=Outvar).place(x=100, y=230)











tkinter.Button(root,text="Save",height=2,width=4,background="lightblue",foreground="white").place(x=100, y=270)

root.mainloop()
