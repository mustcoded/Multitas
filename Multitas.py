from tkinter import *
from tkinter import filedialog
from Remove import Remove
import os
from tkinter import messagebox
import webbrowser

win = Tk() # 1 Create instance
win.title("Multitas") # 2 Add a title
#win.iconbitmap(os.path.abspath('icon.ico'))
win.resizable(0, 0) # 3 Disable resizing the GUI
win.configure(background='white') # 4 change background color
#win.iconbitmap(('icon.ico'))

# 5 Create a label
aLabel = Label(win, text="Select a file to search for it's duplicate files then select another folder which you would like to search and remove those duplicate files from, sit back and enjoy!", anchor="center", padx=13, pady=10, relief=RAISED)
aLabel.grid(column=0, row=1)
aLabel.configure(foreground="white")
aLabel.configure(background="black")
aLabel.configure(wraplength = 240)
aLabel.message = ''

# 6 Create a selectFile function to be used by action button
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


def openLink(): # start a new link

    webbrowser.open_new("http://codingdirectional.info/2018/12/12/remove-duplicate-files-project-is-ready/")

# 9 Adding a Button

action = Button(text="Select File", command=selectFile)
action.grid(column=0, row=2, sticky=W+E)
action.configure(background='black')
action.configure(foreground='white')

action_link = Button(text="Website", command=openLink)
action_link.grid(column=0, row=0, sticky=W+E)
action_link.configure(background='black')
action_link.configure(foreground='white')

win.mainloop()  # 10 start GUI