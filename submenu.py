from tkinter import *
root=Tk()
root.title("GUI")
root.geometry('300x200')

def myfunc():
    print("This is Submenu GUI")
mainmenu=Menu(root)
#tearoff reduce ---- line
m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="Save",command=myfunc)
m1.add_command(label="New",command=myfunc)
m1.add_command(label="Open File",command=myfunc)
m1.add_command(label="Exit",command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m1)

m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="Cut",command=myfunc)
m2.add_command(label="Copy",command=myfunc)
m2.add_command(label="Paste",command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)

root.mainloop()