from tkinter import *
root=Tk()
def hello():
    print("Hello Bhai")
def hell():
    print("Khush Raho Bhai")
def hel():
    print("Sada Awad Raho Bhai")
def he():
    print("Tension Mat Liya Karo Bhai")
root.geometry('600x400')
f1=Frame(root,bg="orange",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,anchor='nw',padx=23)
btn=Button(f1,fg='grey',text="Print Now",command=hello)
btn.pack()
f4=Frame(root,bg="orange",borderwidth=6,relief=SUNKEN)
f4.pack(side=LEFT,anchor='nw',padx=23)
btn3=Button(f4,fg='grey',text="Click Now",command=hell)
btn3.pack()
f2=Frame(root,bg="orange",borderwidth=6,relief=SUNKEN)
f2.pack(side=LEFT,anchor='nw',padx=23)
btn1=Button(f2,fg='grey',text="Submit Now",command=hel)
btn1.pack()

f3=Frame(root,bg="orange",borderwidth=6,relief=SUNKEN)
f3.pack(side=LEFT,anchor='nw',padx=23)
btn2=Button(f3,fg='grey',text="Search Now",command=he)
btn2.pack()
root.mainloop()