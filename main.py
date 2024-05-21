from tkinter import *
from tkinter import ttk
from functions import *
import openpyxl

def load_data():
    path = "./assets/sheet.xlsx"
    workbook = openpyxl.load_workbook(path)
    sheet = workbook.active

    list_values = list(sheet.values)
    cols = list_values[0]
    tree = ttk.Treeview(root, columns=cols, show="headings")
    for col_name in cols:
        tree.heading(col_name, text=col_name)
    tree.place(x=200, y=200)  # Alterado de pack para grid
    for value_tuple in list_values[1:]:
        tree.insert("", END, values=value_tuple)


root = Tk()
load_data()
root.geometry("800x400")

frm = ttk.Frame(root, padding=10)
frm.grid(sticky=(N, S, E, W))

inputtxt = Text(frm, height=5, width=40)
inputtxt.grid(column=0, row=1, columnspan=1, padx=3, pady=3)

ttk.Label(frm, text="Whatsapp Message Sender V2").grid(column=0, row=0)
ttk.Checkbutton(frm, text='Python', onvalue=1, offvalue=0)
ttk.Button(frm, text="Select a file", command=import_file).grid(column=1, row=0)
ttk.Button(frm, text="Delete Image", command=delete_image).grid(column=2, row=0)
ttk.Button(frm, text="Sheet").grid(column=3, row=0)
ttk.Button(frm, text="Send", command=lambda: gettext(inputtxt)).grid(column=4, row=0)

var = IntVar()
checkbutton = ttk.Checkbutton(root, text="Send after text?", variable=var, onvalue=1, offvalue=0, command= lambda: on_button_toggle(var))
checkbutton.place(x=40, y=150)

getimg()


root.mainloop()