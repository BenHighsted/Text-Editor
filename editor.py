"""
Text editor project by Ben Highsted
Started 02/04/2020

"""

#I used this tutorial: https://www.codespeedy.com/create-a-text-editor-in-python/ as a base for this project

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class TextEditor:

	def __init__(self, root):
		self.root = root
		self.root.title("Text Editor") #edit the title here when you have a name
		self.root.geometry("1200x700+200+150") #size of window

		#Initialises/creates variables
		self.filename = None
		self.title = StringVar()
		self.status = StringVar()

		#Creates and packs title
		self.titlebar = Label(self.root, textvariable = self.title, font = ("times new roman", 15, "bold"), bd = 2, relief = GROOVE)
		self.titlebar.pack(side = TOP, fill = BOTH)
		self.settitle()

		#Creates, packs and sets status bar
		self.statusbar = Label(self.root, textvariable = self.status, font = ("times new roman", 15, "bold"), bd = 2, relief = GROOVE)
		self.statusbar.pack(side = BOTTOM, fill = BOTH)
		self.status.set("Welcome to Ben's Text Editor")

		#Creates and Configures the menu bar
		self.menubar = Menu(self.root, font = ("times new roman", 15, "bold"), activebackground = "skyblue")
		self.root.config(menu = self.menubar)
		
		#Creates the file dropdown menu
		self.filemenu = Menu(self.menubar, font = ("times new roman", 12, "bold"), activebackground = "skyblue", tearoff = 0)

		#Creates a set of commands for the file menu
		self.filemenu.add_command(label = "New", accelerator = "Ctrl+N", command = self.newfile)
		self.filemenu.add_command(label = "Open", accelerator = "Ctrl+O", command = self.openfile)
		self.filemenu.add_command(label = "Save", accelerator = "Ctrl+S", command = self.savefile)
		self.filemenu.add_command(label = "Save As", accelerator = "Ctrl+A", command = self.saveasfile)
		self.filemenu.add_separator()
		self.filemenu.add_command(label = "Exit", accelerator = "Ctrl+L", command = self.exitfile)
		self.menubar.add_cascade(label = "File", menu = self.filemenu)

		#Creates the edit dropdown menu
		self.editmenu = Menu(self.menubar, font = ("times new roman", 12, "bold"), activebackground = "skyblue", tearoff = 0)
		
		#Creates a set of commands for the edit menu
		self.editmenu.add_command(label = "Cut", accelerator = "Ctrl+X", command = self.cut)
		self.editmenu.add_command(label = "Copy", accelerator = "Ctrl+C", command = self.copy)
		self.editmenu.add_command(label = "Paste", accelerator = "Ctrl+V", command = self.paste)
		self.editmenu.add_separator()
		self.editmenu.add_command(label = "Undo", accelerator = "Ctrl+Z", command = self.undo)
		self.menubar.add_cascade(label = "Edit", menu = self.editmenu)

		#Creates the help dropdown menu
		self.helpmenu = Menu(self.menubar, font = ("times new roman", 12, "bold"), activebackground = "skyblue", tearoff = 0)

		#Creates a set of commands for the help menu
		self.helpmenu.add_command(label = "About", command = self.infoabout)
		self.menubar.add_cascade(label = "Help", menu = self.helpmenu)

		#Change this to an about drop down instead? Or the name of the editor drops down, then you can select about?

		#Creates the text area and a scroll bar for it
		scrollbar = Scrollbar(self.root, orient = VERTICAL)
		self.textarea = Text(self.root, yscrollcommand = scrollbar.set, font = ("times new roman", 15, "bold"), state = "normal", relief = GROOVE)
		scrollbar.pack(side = RIGHT, fill = Y)
		scrollbar.config(command = self.textarea.yview)
		self.textarea.pack(fill = BOTH, expand = 1)

		self.shortcuts()

	#Function definitions
	def settitle(self):
		if self.filename:
			self.title.set(self.filename)
		else:
			self.title.set("Untitled")

	def newfile(self, *args):
		self.textarea.delete("1.0", END)
		self.filename = None
		self.settitle()
		self.status.set("New File Created")

	def openfile(self, *args):
		try:
			self.filename = filedialog.askopenfilename(title = "Select file", filetypes = (("All Files", "*.*"), ("Text Files", "*.txt"), ("Python Files", "*.py")))
			if self.filename:
				infile = open(self.filename, "r")
				self.textarea.delete("1.0", END)
				for line in infile:
					self.textarea.insert(END, line)
				infile.close()
				self.settitle()
				self.status.set("Opened Successfully")
		except Exception as e:
			messagebox.showerror("Error: Exception ", e)

	def savefile(self, *args):
		try:
			if self.filename:
				data = self.textarea.get("1.0", END)
				outfile = open(self.filename, "w")
				outfile.write(data)
				outfile.close()
				self.settitle()
				self.status.set("Saved Successfully")
			else:
				self.saveasfile()
		except Exception as e:
			messagebox.showerror("Error: Exception ", e)

	def saveasfile(self, *args):
		try:
			untitledfile = filedialog.asksaveasfilename(title = "Safe file As", defualtextension = ".txt", initialfile = "Untitled.txt", filetypes = (("All Files", "*,*"), ("Text Files", "*.txt"), ("Python Files", "*.py")))
			data = self.textarea.get("1.0", END)
			outfile = open(untitledfile, "w")
			outfile.write(data)
			outfile.close()
			self.filename = untitledfile
			self.settitle()
			self.status.set("Saved Successfully")
		except Exception as e:
			messagebox.showerror("Error: Exception ", e)

	def exitfile(self, *args):
		message = messagebox.query("Warning:", "Your unsaved data may be lost.")
		if message > 0:
			self.root.destroy()
		else:
			return

	def cut(self, *args):
		self.textarea.event_generate("<<Cut>>")

	def copy(self, *args):
		self.textarea.event_generate("<<Copy>>")
	
	def paste(self, *args):
		self.textarea.event_generate("<<Paste>>")

	def undo(self, *args):
		try:
			if self.filename:
				self.textarea.delete("1.0", END)
				infile = open(self.filename, "r")
				for line in infile:
					self.textarea.insert(END, line)
				infile.close()
				self.settitle()
				self.status.set("Undone Successfully")
			else:
				self.textarea.delete("1.0", END)
				self.filename = None
				self.settitle()
				self.status.set("Undone Successfully")
		except Exception as e:
			messagebox.showerror("Error: Exception ", e)

	def infoabout(self):
		messagebox.showinfo("About Text Editor", "Version 1.0: The base editor\nCreated using Python3.")

	def shortcuts(self):
		#Binds shortcuts to inputs
		self.textarea.bind("<Control-n>", self.newfile)
		self.textarea.bind("<Control-o>", self.openfile)
		self.textarea.bind("<Control-s>", self.savefile)
		self.textarea.bind("<Control-a>", self.saveasfile)
		self.textarea.bind("<Control-l>", self.exitfile)
		self.textarea.bind("<Control-x>", self.cut)
		self.textarea.bind("<Control-c>", self.copy)
		self.textarea.bind("<Control-v>", self.paste)
		self.textarea.bind("<Control-z>", self.undo)

root = Tk()
TextEditor(root)
root.mainloop()