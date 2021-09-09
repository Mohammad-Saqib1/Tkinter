import tkinter.messagebox as mb
from tkinter import *
root=Tk()
root.geometry('300x250')
root.title("Slider")
'''
#verticle slider
myslider=Scale(root,from_=0,to=100)
myslider.pack()
#horizontal slider
myslider1=Scale(root,from_=0,to=100,orient=HORIZONTAL)
myslider1.pack()

myslider2=Scale(root,from_=0,to=100,orient=HORIZONTAL)
#start value with any number
myslider2.set(10)
myslider2.pack()
'''
def func():
    print(f"We have credited {myslider3.get()} dollars to your bank account")
    mb.showinfo("Amount credited!",f"We have credited {myslider3.get()} dollars to your bank account")
Label(root,text="How many dollars do you want?").pack()
#Tickinterval value
myslider3=Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50)
myslider3.pack()
Button(root,text="Get dollars!",command=func).pack()

root.mainloop()