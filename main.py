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
ttk.Button(frm, text="Texto", command=gettext(inputtxt)).grid(column=2, row=0)

img = Image.open("./assets/tempIMG.png")
img = img.resize((250, 250))
img = ImageTk.PhotoImage(img)
label1 = Label(image=img)
label1.place(x=400, y=50)

root.mainloop()