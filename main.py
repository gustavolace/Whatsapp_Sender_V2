from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

def import_file():
	file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
	if file_path:
		print("Selected file:", file_path)


ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=import_file).grid(column=1, row=0)
root.mainloop()