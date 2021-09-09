from tkinter import *
root=Tk()
root.title("Listbox")
root.geometry('400x250')
i=0
def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1

lbx=Listbox(root)
lbx.pack()
lbx.insert(END,"First item of our listbox")

Button(root,text="Add Item",command=add).pack()




root.mainloop()