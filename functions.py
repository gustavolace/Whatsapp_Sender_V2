from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import shutil
import os

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

def gettext(input):
	inp = input.get(1.0, "end-1c")
	print(inp) 

def getimg():
	global img
	global label
	if os.path.isfile("./assets/tempIMG.png"):	
		print("carregetimg")
		img = Image.open("./assets/tempIMG.png")
		img = img.resize((250, 250))
		img = ImageTk.PhotoImage(img)
		label = Label(image=img)
		label.place(x=40, y=180)

def on_button_toggle(var):
    if var.get() == 1:
        print("Checkbutton is selected")
    else:
        print("Checkbutton is deselected")
        
def delete_image():
	os.remove("./assets/tempIMG.png")
	label.destroy()
