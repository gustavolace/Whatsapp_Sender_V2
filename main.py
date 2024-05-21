from tkinter import *
from tkinter import ttk
from functions import *

root = Tk()
root.geometry("800x400")

frm = ttk.Frame(root, padding=10)
frm.grid(sticky=(N, S, E, W))

inputtxt = Text(frm, height=5, width=40)
inputtxt.grid(column=0, row=1, columnspan=1, padx=3, pady=3)

ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Select a file", command=import_file).grid(column=1, row=0)
ttk.Button(frm, text="Texto", command=lambda: gettext(inputtxt)).grid(column=2, row=0)
getimg()

root.mainloop()