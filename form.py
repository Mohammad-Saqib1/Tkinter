from tkinter import *
root=Tk()
#function printf used in submit button
def printf():
    print("The Name of user :",namevalue.get())
    print("The Password of user :",passvalue.get())
    print("The Email of user :",emailvalue.get())
    print("The Gender of user :",gendervalue.get())
    print("The Address of user :",addressvalue.get())
    print("The Age of user :",agevalue.get())
    with open("Answer.txt","a") as f:
        f.write(f"{namevalue.get(),passvalue.get(),emailvalue.get(),gendervalue.get(),agevalue.get(),addressvalue.get()}\n")
        
    
    

root.geometry('600x320')
# Heading
h=Label(root,text="Welcome to our GUI page ",font="camcasius 13 bold",padx=10,bg='orange',borderwidth=5,relief=SUNKEN).grid()
#Input
name=Label(root,text="User Name :",font=20,fg='white',bg='blue',padx=5,borderwidth=5,relief=SUNKEN).grid()
passwd=Label(root,text=" Password :",font=20,fg='white',bg='blue',padx=5,borderwidth=5,relief=SUNKEN).grid()
email=Label(root,text=" Email :",font=20,fg='white',bg='blue',padx=5,borderwidth=5,relief=SUNKEN).grid()
gender=Label(root,text=" Gender :",font=20,fg='white',bg='blue',padx=5,borderwidth=5,relief=SUNKEN).grid()
address=Label(root,text=" Address :",font=20,fg='white',bg='blue',padx=5,borderwidth=5,relief=SUNKEN).grid()
age=Label(root,text=" Age :",font=20,fg='white',bg='blue',padx=5,borderwidth=5,relief=SUNKEN).grid()
#varibles
namevalue=StringVar()
passvalue=StringVar()
emailvalue=StringVar()
gendervalue=StringVar()
agevalue=StringVar()
addressvalue=StringVar()
checkboxvalue=StringVar()
#Entry
nv1=Entry(root,textvariable=namevalue,borderwidth=5,relief=SUNKEN,bg='orange',fg='black',font=6).grid(row=1,column=1)
nv2=Entry(root,textvariable=passvalue,borderwidth=5,relief=SUNKEN,bg='orange',fg='black',font=6).grid(row=2,column=1)
nv3=Entry(root,textvariable=emailvalue,borderwidth=5,relief=SUNKEN,bg='orange',fg='black',font=6).grid(row=3,column=1)
nv4=Entry(root,textvariable=gendervalue,borderwidth=5,relief=SUNKEN,bg='orange',fg='black',font=6).grid(row=4,column=1)
nv5=Entry(root,textvariable=agevalue,borderwidth=5,relief=SUNKEN,bg='orange',fg='black',font=6).grid(row=5,column=1)
nv6=Entry(root,textvariable=addressvalue,borderwidth=5,relief=SUNKEN,bg='orange',fg='black',font=6).grid(row=6,column=1)
#Checkbox
nv8=Label(text="Accept and Agree Licence Agreement !").grid(row=7,column=2)
nv7=Checkbutton(root,textvariable=checkboxvalue).grid(row=7,column=1)

#submit button
nv9=Button(text="Submit",command=printf,bg='skyblue',fg='blue',borderwidth=5,relief=SUNKEN).grid(row=8,column=1,pady=10)





root.mainloop()