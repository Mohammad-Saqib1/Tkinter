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