#importing required packages and libraries
import re
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import filedialog, simpledialog
from tkinter.scrolledtext import ScrolledText
from datetime import datetime

root = Tk()

root.title("AziPad")
#root.geometry("300x300")
root.resizable(0, 0)

my_pad = ScrolledText(root, width = 90, height = 40)
file_name = ' '

#All Command Functions Start

def new_file():
    global fileName
    if len(my_pad.get('1.0', END+'-1c')) > 0:
        if messagebox.askyesno("Notepad", "Do you want to save changes?"):
            save()
        else:
            my_pad.delete(0.0, END)
    root.title("Notepad")

def open_file():
    fd = filedialog.askopenfile(parent = root, mode = 'r')
    t = fd.read()
    my_pad.delete(0.0, END)
    my_pad.insert(0.0, t)

def save():
    fd = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt')
    if fd!= None:
        data = my_pad.get('1.0', END)
    try:
        fd.write(data)
    except:
        messagebox.showerror(title="Error", message = "Not able to save file!")

def save_as():
    fd = filedialog.asksaveasfile(mode='w', defaultextension = '.txt')
    t = my_pad.get(0.0, END)     #t stands for the text gotten from notepad
    try:
        fd.write(t.rstrip())
    except:
        messagebox.showerror(title="Error", message = "Not able to save file!")

def exit_pad():
    if messagebox.askyesno(title="Alert", message="Do you want to exit..?"):
        root.destroy()

def date_time():
    time_now = datetime.now()
    dt_formate = time_now.strftime("%d/%m/%Y - %H:%M:%S")
    label = messagebox.showinfo("Date/Time ", dt_formate)

def about_pad():
    label = messagebox.showinfo("About Notepad", "This Notepad is developed by Muhamad Azeem")

def cut():
    my_pad.event_generate("<<Cut>>")

def copy():
    my_pad.event_generate("<<Copy>>")

def paste():
    my_pad.event_generate("<<Paste>>")

def select_all():
    my_pad.event_generate("<<SelectAll>>")

def delete_all():
    my_pad.event_generate("<<Clear>>")

def find_text():
    my_pad.tag_remove("Found", '1.0', END)
    find = simpledialog.askstring("Find", "Find what: ")
    if find:
        idx = '1.0'
    while 1:
        idx = my_pad.search(find, idx, nocase = 1, stopindex = END)
        if not idx:
            break
        last_index = '%s+%dc' %(idx, len(find))
        my_pad.tag_add("Found", idx, last_index)
        idx = last_index
    my_pad.tag_config("Found", foreground = 'white', background = 'blue')
    my_pad.bind("<1>", click_event)

def click_event(event):
    my_pad.tag_config("Found", background = 'white', foreground = 'black')

#All Command Functions Close

#Initialize Menu
my_pad_menu = Menu(root)
root.configure(menu = my_pad_menu)

#file menu
file_menu = Menu(my_pad_menu, tearoff = False)
my_pad_menu.add_cascade(label = "File", menu = file_menu)

#Add item to file
file_menu.add_command(label = "New", comman = new_file)
file_menu.add_command(label = "Open", command = open_file)
file_menu.add_command(label = "Save", command = save)
file_menu.add_command(label = "Save As", command = save_as)
file_menu.add_separator()
file_menu.add_command(label = "Exit",  command = exit_pad)

#Edit Menu
edit_menu = Menu(my_pad_menu, tearoff = False)
my_pad_menu.add_cascade(label = "Edit", menu = edit_menu)

#Add Edit Items
edit_menu.add_command(label = "Cut", command = cut)
edit_menu.add_command(label = "Copy", command = copy)
edit_menu.add_command(label = "Paste", command = paste)
edit_menu.add_command(label = "Delete", command = delete_all)
edit_menu.add_separator()
edit_menu.add_command(label = "Find", command = find_text)
edit_menu.add_separator()
edit_menu.add_command(label = "Select All", command = select_all)
edit_menu.add_command(label = "Date and Time", command = date_time)

#Help Menu
help_menu = Menu(my_pad_menu, tearoff = False)
my_pad_menu.add_cascade(label = "Help", menu = help_menu)

#Add Help Items
help_menu.add_command(label = "About Notepad", command = about_pad)

#Satus Bar
#status_frame = Frame(root)
#status_bar = Label(root, text = "Status Bar",  relief = SUNKEN, anchor = W)
#status_bar.pack()

my_pad.pack()
root.mainloop()