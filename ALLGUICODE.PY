1:-BASIC WINDOW
from tkinter import *
basicwindow=Tk()
basicwindow.mainloop()

2:-MIN AND MAX SIZE
from tkinter import *
root=Tk()
root.geometry('500x500')
root.minsize(300,100)
root.maxsize(800,400)
root.mainloop()

3:-LABEL
from tkinter import *
root=Tk()
root.geometry('500x500')
root.minsize(400,200)
root.maxsize(800,400)
# after creating label must be packed
saqib=Label(text="This s basic GUI Tutorial",bg='grey',font=20)
saqib.pack()
root.mainloop()

4:-PHOTO
from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.geometry('1200x400')
abc=PhotoImage(file="lg.png")
saqib=Label(image=abc)

saqib.pack()
'''
for jpg
saqib=Image.open("p2.jpg")
rakib=ImageTk.PhotoImage(saqib)
ahsan=Label(image=rakib)
ahsan.pack()
'''
root.mainloop()

5:-ATTRIBUTES
from tkinter import *
root = Tk()

root.geometry('300x200')
root.title(" ATTRIBUTES TUTORIAL ")
# start attributes
'''
important label attributes
text-adds the text
bg-backgroung 
fg-foreground
font-set the font
padx-x padding
pady-y padding
relief-borderstyling-SUNKEN,RAISED,GROOVE,RIDGE


important pack attributes
anchor=nw,ew,es,sw,etc
side=top,bottom,left,right
fill x & Y
padding- x & y 
'''
saqib = Label(text='''“Dream is not that which 
you see while sleeping it is
 something that does not let you sleep.”
― A P J Abdul Kalam''', bg='orange', fg='blue', padx=15, pady=50, font="comicsansms 19 bold", borderwidth=5, relief=SUNKEN)

saqib.pack(side=BOTTOM, anchor="sw", fill=X,padx=20,pady=50)
root.mainloop()

6:-FRAME
from tkinter import *
root=Tk()
root.geometry('500x500')
f1=Frame(root,bg='orange',relief=SUNKEN)
f1.pack(side=LEFT,fill="y")
f2=Frame(root,bg='orange',relief=SUNKEN)
f2.pack(side=TOP,fill="x")
l=Label(f1,text="VISUAL STUDIO",borderwidth=6,relief=SUNKEN)
l.pack(pady=142)
l=Label(f2,text="Welcome to our vs code",borderwidth=8,relief=SUNKEN)
l.pack()
root.mainloop()

7:-BUTTON
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


8:- PACKING METHODS
from tkinter import *
root=Tk()

def hello():
    print(f"This is the name of user : {uservalue.get()}")
    print(f"This is the password of user : {passvalue.get()}")
    print(f"This is the gender of user : {gendervalue.get()}")
    print(f"This is the age of user: {agevalue.get()}")
root.geometry('600x600')
user=Label(root,text="Username",font=25,fg='red').grid()
passwd=Label(root,text="Password",font=25,fg='red').grid()
ml=Label(root,text="Gender",font=25,fg='red').grid()
ag=Label(root,text="Age",font=25,fg='red').grid()

uservalue=StringVar()
passvalue=StringVar()
gendervalue=StringVar()
agevalue=StringVar()
uservalue1=Entry(root,textvariable=uservalue).grid(row=0,column=1)
passvalue1=Entry(root,textvariable=passvalue).grid(row=1,column=1)
gendervalue1=Entry(root,textvariable=gendervalue).grid(row=2,column=1)
agevalue1=Entry(root,textvariable=agevalue).grid(row=3,column=1)
btn=Button(root,text="Submit",command=hello,font=20,fg='green').grid(padx=50)
root.mainloop()



9:-EVENTS

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

