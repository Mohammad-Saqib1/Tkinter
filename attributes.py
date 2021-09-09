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

saqib.pack(side=BOTTOM, anchor="sw", fill=X, padx=20, pady=50)
root.mainloop()
