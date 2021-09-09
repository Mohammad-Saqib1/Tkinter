from tkinter import *
root=Tk()
def harry(event):
    print(f"hello\n{event.x},{event.y}\n")
root.geometry('400x400')
root.title("EVENTS")
a=Button(root,text="CLICK ME")
a.pack()
a.bind('<Button-1>',harry)
a.bind('<Double-1>',quit)

root.mainloop()