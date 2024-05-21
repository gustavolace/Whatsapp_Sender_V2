from tkinter import *
from tkinter import ttk
from functions import *

root = Tk()
root.geometry("800x400")

frm = ttk.Frame(root, padding=10)
frm.grid(sticky=(N, S, E, W))

inputtxt = Text(frm, height=5, width=40)
inputtxt.grid(column=0, row=1, columnspan=1, padx=3, pady=3)

ttk.Label(frm, text="Whatsapp Message Sender V2").grid(column=0, row=0)
ttk.Checkbutton(frm, text='Python', onvalue=1, offvalue=0)
ttk.Button(frm, text="Select a file", command=import_file).grid(column=1, row=0)
ttk.Button(frm, text="Delete Image", command=delete_image).grid(column=2, row=0)
ttk.Button(frm, text="Enviar", command=lambda: gettext(inputtxt)).grid(column=3, row=0)

var = IntVar()
checkbutton = ttk.Checkbutton(root, text="Send after text?", variable=var, onvalue=1, offvalue=0, command= lambda: on_button_toggle(var))
checkbutton.place(x=40, y=150)


getimg()

root.mainloop()