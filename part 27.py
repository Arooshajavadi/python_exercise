from tkinter import *
import tkinter.messagebox as msg
import tkinter. ttk as ttk
from modules import *

def save_click():
    info=get_info(Product.get(),Count.get(),Price.get(),Invar.get(),Outvar.get())
    test(info,total_count)
    msg.showinfo("Save", f"Information{info}saved!!!")
    reset()
    x=tuple(info.values())
    table.insert("",END,values=x)
    test(info_dict, total_count)


root = tkinter.Tk()
root.geometry("1000x350")
root.title("Inventory")

Product=tkinter.StringVar()
tkinter.Label(root, text="Product").place(x=40, y=40)
tkinter.Entry(root,textvariable=Product).place(x=100, y=40)

Count=tkinter.IntVar()
tkinter.Label(root, text="Count").place(x=40, y=80)
tkinter.Entry(root,textvariable=Count).place(x=100, y=80)

Price=tkinter.IntVar()
tkinter.Label(root, text="Price").place(x=40, y=120)
tkinter.Entry(root,textvariable=Price).place(x=100, y=120)

Person=tkinter.StringVar()
tkinter.Label(root, text="Person").place(x=40, y=160)
tkinter.Entry(root,textvariable=Person).place(x=100, y=160)

Invar=tkinter.BooleanVar()
Outvar=tkinter.BooleanVar()
tkinter.Label(root, text="Type").place(x=40, y=200)
tkinter.Checkbutton(root,text="In",variable=Invar).place(x=100, y=200)
tkinter.Checkbutton(root,text="Out",variable=Outvar).place(x=100, y=230)

table=ttk.Treeview(root,show="headings",columns=(1,2,3,4,5,6))
table.place(x=400, y=40)
table.heading("1", text="Product")
table.heading("2", text="Count")
table.heading("3", text="Price")
table.heading("4", text="Person")
table.heading("5", text="In")
table.heading("6", text="Out")

table.column(1,width="80")
table.column(2,width="80")
table.column(3,width="80")
table.column(4,width="80")
table.column(5,width="80")
table.column(6,width="80")



tkinter.Button(root,text="Save",height=2,width=4,background="lightblue",foreground="white",command=save_click).place(x=100, y=270)
root.mainloop()
