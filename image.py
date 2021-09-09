from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.geometry('1200x400')
abc=PhotoImage(file="1.png")
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