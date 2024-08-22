import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from tkinter import END



def reset_info():
    Brand.set("")
    Model.set("")
    Color.set("")
    Glassvar.set(False)
    Memoryvar.set(False)

def get_info(Brand, Model, Color, Glassvar, Memoryvar):
    info = {
        "Brand": Brand,
        "Model": Model,
        "Color": Color,
        "Glass": Glassvar,
        "Memory": Memoryvar
    }
    return info

def results():
        y=get_info(Brand.get(), Model.get(), Color.get(), Glassvar.get(), Memoryvar.get())
        msg.showinfo("Save", f"Information {y} saved")
        reset_info()
        w = tuple(y.values())
        table.insert("",END, values=w, tags=w[4] )


shop = tkinter.Tk()
shop.title(" Mobile information ")
shop.geometry("820x600")

Brand=tkinter.StringVar()
tkinter.Label(shop, text="Brand").place(x=100, y=100)
ttk.Combobox(shop,textvariable= Brand ,values=["Apple","Nokia","Samsung","Xiaomi"],state="readonly").place(x=150,y=100)

Model= tkinter.StringVar()
tkinter.Label(shop,text="Model").place(x=100,y=200)
tkinter.Entry(shop,textvariable=Model,width=22).place(x=150,y=200)

Color=tkinter.StringVar()
tkinter.Label(shop,text="Color").place(x=100,y=300)
ttk.Combobox(shop,text=Color,values=["White","Black","Red","Blue"],state="readonly").place(x=150,y=300)

tkinter.Label(shop,text="Option").place(x=99,y=400)
Glassvar=tkinter.BooleanVar()
Memoryvar=tkinter.BooleanVar()
tkinter.Checkbutton(shop,text="Glass",variable=Glassvar).place(x=150,y=400)
tkinter.Checkbutton(shop,text="Memory",variable=Memoryvar).place(x=150,y=420)

table = ttk.Treeview(shop, columns=(1,2,3,4,5),height=11, show="headings")

table.heading(1, text="Brand")
table.heading(2, text="Model")
table.heading(3, text="Color")
table.heading(4, text="Glass")
table.heading(5, text="Memory")

table.column(1, width=80)
table.column(2, width=80)
table.column(3, width=80)
table.column(4, width=80)
table.column(5, width=80)
table.place(x=400,y=100)

tkinter.Button(shop,text="Save",width=7,height=3,command=results).place(x=250,y=500)
shop.mainloop()
