from tkinter import *
import tkinter.messagebox as mb
root=Tk()
root.title("GUI")
root.geometry('300x200')

def myfunc():
    print("This is Submenu GUI")

def help():
    print("I will help you")
    #showinfo has not return value
    mb.showinfo("Help","I will help you with this GUI")

def rate():
    print("Rate us")
    #askquestion have return value like yes and no
    value=mb.askquestion("Was you experience good?","Please reply")
    if value=='yes':
        msg="Rate us on app"
    else:
        msg="Tell us what went wrong.we will improve them"
    mb.showinfo("Experience",msg)

def frnd():
    #askrertycancel have return value like true and false
    ans=mb.askretrycancel("Friend","Supportive friend")
    if ans:
        print("Don't retry i m your friend")
    else:
        print("Please retry")
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

m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="Help",command=help)
m3.add_command(label="Rate us",command=rate)
m3.add_command(label="Freind",command=frnd)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Help",menu=m3)


root.mainloop()