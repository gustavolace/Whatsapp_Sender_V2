from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import shutil
import os
import openpyxl
from tkinter import messagebox 
from urllib.parse import quote
from sender import *

def copy_and_rename(src_path, dest_path, new_name):
	shutil.copy(src_path, dest_path)
	new_path = f"{dest_path}/{new_name}"
	print(new_path)
	shutil.move(f"{dest_path}/{os.path.basename(src_path)}", new_path) 

def import_file():
	file_path = filedialog.askopenfilename(title="Select a file", filetypes=[('image files', ('.png', '.jpg', 'jpeg')), ("All files", "*.*")])
	if file_path:
		copy_and_rename(file_path, "./assets", "tempIMG.png")
		getimg()
		print("Selected file")

def import_sheet(ttk,root):
	file_path = filedialog.askopenfilename(title="Select a file", filetypes=[('image files', ('.xlsx')), ("All files", "*.*")])
	if file_path:
		copy_and_rename(file_path, "./assets", "sheet.xlsx")
		load_data(ttk,root)
		print("Selected file")

def getimg():
	global img
	global label
	if os.path.isfile("./assets/tempIMG.png"):	
		base_width = 300
		img = Image.open("./assets/tempIMG.png")
		wpercent = (base_width / float(img.size[0]))
		hsize = int((float(img.size[1]) * float(wpercent)))

		img = img.resize((base_width, hsize), Image.Resampling.LANCZOS)
		img = ImageTk.PhotoImage(img)
		label = Label(image=img)
		label.grid(column=0, row=4)

def on_button_toggle(var):
	global after
	if var.get() == 1:
		after = True
		print("Checkbutton is selected")
	else:
		after = False
		print("Checkbutton is deselected")

def on_button_debug(var2):
	global debug
	if var2.get() == 1:
		debug = True
		print("Debug is enable")
	else:
		debug = False
		print("Debug is disable")
        
def delete_image():
	os.remove("./assets/tempIMG.png")
	label.destroy()

def load_data(ttk,root):
	global tree, list_values
	path = "./assets/sheet.xlsx"
	if os.path.isfile(path):
		workbook = openpyxl.load_workbook(path)
		sheet = workbook.active

		list_values = list(sheet.values)
		cols = list_values[0]
		tree = ttk.Treeview(root, columns=cols, show="headings")
		for col_name in cols:
			tree.heading(col_name, text=col_name)
		tree.grid(column=5, row=0, pady=3) 
		for value_tuple in list_values[1:]:
			tree.insert("", END, values=value_tuple)

def gettext(input):
	global debug, after
	inp = input.get(1.0, "end-1c")
	if inp == "":
		messagebox.showwarning("Error","Type something on input")
	else: 
		if 'debug' not in globals():
			debug = False
		if "after" not in globals():
			after = False
		urls = make_url(list_values,inp)
		messagebox.showinfo("Whatsapp Message Sender V2", "Starting...")
		main(urls, debug, after)

def make_url(contacts, text):
	urls = []
	for nome, telefone in contacts :
		if nome == "Nome":
			continue
		client_text = text.replace("$cl", nome)
		url = f"https://web.whatsapp.com/send/?phone={telefone}&text={quote(client_text)}"
		urls.append(url)
	return urls