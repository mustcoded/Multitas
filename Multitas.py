from tkinter import *
from tkinter import filedialog
from Remove import Remove
import os
from tkinter import messagebox
import webbrowser
from Copy import Copy
import platform
from tkinter import Menu

win = Tk() # Create instance
win.title("Multitas") # Add a title
win.resizable(0, 0) # Disable resizing the GUI
win.configure(background='black') # change background color
win.iconbitmap(('icon.ico'))


#  Create a label
aLabel = Label(win, text="Select tasks from buttons below, if you have any question then read the manual!", anchor="center", padx=13, pady=10, relief=RAISED,)
aLabel.grid(column=0, row=0, sticky=W+E)
aLabel.configure(foreground="white")
aLabel.configure(background="black")
aLabel.configure(wraplength=160)
aLabel.message = ''

# Create a selectFile function to remove the duplicate files
def selectFile():

    fullfilenames = filedialog.askopenfilenames(initialdir="/", title="Select a file") # select multiple files from the hard drive

    if(fullfilenames != ''):

        fullfilenamelist = win.tk.splitlist(fullfilenames)
        directory_path = os.path.dirname(os.path.abspath(fullfilenamelist[0]))

        os.chdir(directory_path)  # change the directory to the selected file directory

        folder = filedialog.askdirectory()  # 7 open a folder then create and start a new remove thread to delete the duplicate file
        folder = folder.replace('/', '\\')  # 8 this is for the windows separator only

        if(folder != '' and folder != os.getcwd()):

            for fullfilename in fullfilenamelist:

                if(fullfilename != ''):
                    filename = fullfilename.split('/')[-1]
                    remove = Remove(folder, filename, fullfilename, directory_path, aLabel)
                    remove.start()
                    remove.join()
                    messagebox.showinfo('Remove the duplicate files', aLabel.message)

        else:
            messagebox.showinfo("Error", "Kindly select one folder and it must be a different one")
            return

    else:
        messagebox.showinfo("Select file", "You need to select a file!")
        return

# Create a copyFile function to move a file from one folder to another
def copyFile():

    fullfilenames = filedialog.askopenfilenames(initialdir="/", title="Select a file") # select multiple files from the hard drive

    if(fullfilenames != ''):

        fullfilenamelist = win.tk.splitlist(fullfilenames)
        directory_path = os.path.dirname(os.path.abspath(fullfilenamelist[0]))

        os.chdir(directory_path)  # change the directory to the selected file directory

        folder = filedialog.askdirectory()  # open a folder then create and start a new Copy thread to move the file from one directory to another one
        folder = folder.replace('/', '\\')  # This is for the windows separator only

        if(folder != '' and folder != os.getcwd()):

            for fullfilename in fullfilenamelist:

                if(fullfilename != ''):
                    filename = fullfilename.split('/')[-1]
                    copy = Copy(folder, filename, fullfilename)
                    copy.start()
                    copy.join()
                    messagebox.showinfo('Move the file ', 'File has been moved to new destination')

        else:
            messagebox.showinfo("Error", "Kindly select one folder and it must be a different one")
            return

    else:
        messagebox.showinfo("Select file", "You need to select a file!")
        return

# Find out a computer system information
def sysInfo():
    sys_text = "OS :- " + platform.platform() + ' ' +  platform.version() + '\n'
    sys_text += "Processor :- " + platform.processor() + '\n'
    sys_text += "Chipset Brand :- " + platform.machine() + '\n'
    sys_text += "Network :- " + platform.node() + '\n'
    aLabel.configure(text=sys_text)

def openLink(): # Start a new link

    webbrowser.open_new("https://islandtropicaman.com/wp/2022/07/06/a-python-application-which-handles-variety-of-tasks/")

# Adding a Button

button_frame = Frame(win, bg='black')
button_frame.grid(column=0, row=1, sticky=E+W)

action = Button(button_frame, text="Remove", command=selectFile, padx=3)
action.grid(column=0, row=0, sticky=E+W)
action.configure(background='black')
action.configure(foreground='white')

action_move = Button(button_frame, text="Move", command=copyFile, padx=3)
action_move.grid(column=1, row=0, sticky=E+W)
action_move.configure(background='black')
action_move.configure(foreground='white')

#action_pic = Button(button_frame, text="SysInfo", command=sysInfo, padx=2)
#action_pic.grid(column=2, row=0, sticky=E+W)
#action_pic.configure(background='black')
#action_pic.configure(foreground='white')

#action_link = Button(button_frame, text="Manual", command=openLink, padx=2)
#action_link.grid(column=3, row=0, sticky=E+W)
#action_link.configure(background='black')
#action_link.configure(foreground='white')

#set menu bar
menuBar = Menu(win)
win.configure(menu=menuBar)
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Manual", command=openLink)
fileMenu.add_separator()
fileMenu.add_command(label="Sys Info", command=sysInfo)
menuBar.add_cascade(label="File", menu=fileMenu)

win.mainloop()  # start GUI