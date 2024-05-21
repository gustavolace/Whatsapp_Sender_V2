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
		print("Selected file")

def gettext(input):
	inp = input.get(1.0, "end-1c")
	print(inp) 

