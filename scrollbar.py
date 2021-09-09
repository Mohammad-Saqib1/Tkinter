from tkinter import *
root = Tk()
root.geometry('400x250')
root.title("Scroll Bar")
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

"""
# integer scrollbar

lbx=Listbox(root,yscrollcommand=scrollbar.set)
scrollbar.config(command=lbx.yview)
for i in range(200):
    lbx.insert(END,f"Item {i}")
lbx.pack()
"""

# text scrollbar
text = Text(root, yscrollcommand=scrollbar.set)
text.pack()
scrollbar.config(command=text.yview)


root.mainloop()
