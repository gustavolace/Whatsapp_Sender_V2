from tkinter import *
from tkinter import ttk
from functions import *





root = Tk()
root.geometry("800x630")
frm = ttk.Frame(root, padding=10)
frm.grid(sticky=(N, S, E, W))

inputtxt = Text(frm, height=5, width=40)
inputtxt.grid(column=0, row=2, columnspan=4, padx=3, pady=3)

ttk.Label(frm, text="Whatsapp Message Sender V2").grid(column=0, row=0, columnspan=4)

ttk.Button(frm, text="Select a file", command=import_file).grid(column=0, row=3)
ttk.Button(frm, text="Delete Image", command=delete_image).grid(column=1, row=3)

ttk.Button(frm, text="Sheet").grid(column=2, row=3)
ttk.Button(frm, text="Send", command=lambda: gettext(inputtxt)).grid(column=3, row=3)

var = IntVar()
checkbutton = ttk.Checkbutton(root, text="Send after text?", variable=var, onvalue=1, offvalue=0, command= lambda: on_button_toggle(var))
checkbutton.grid(column=0, row=1)

load_data(ttk, root)
getimg()


root.mainloop()