from tkinter import *
root=Tk()
root.geometry('500x500')
root.minsize(400,200)
root.maxsize(800,400)
# after creating label must be packed
saqib=Label(text="This s basic GUI Tutorial",bg='grey',font=20)
saqib.pack()



root.mainloop()