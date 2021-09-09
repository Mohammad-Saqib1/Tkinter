from tkinter import *
import tkinter.messagebox as mb
root = Tk()
root.geometry('400x250')
root.title("Radio Button")


def order():
    mb.showinfo("Order Received!",
                f"We have received your order {var.get()}. Thanks for ordering")


var = StringVar()
var.set("Radio")
radio = Radiobutton(root, text="Doas", variable=var,
                    value="Dosa", padx=20, font="lucida 13 bold").pack(anchor="w")
radio = Radiobutton(root, text="Idly", variable=var,
                    value="Idly", padx=20, font="lucida 13 bold").pack(anchor="w")
radio = Radiobutton(root, text="Paratha", variable=var,
                    value="Paratha", padx=20, font="lucida 13 bold").pack(anchor="w")
radio = Radiobutton(root, text="Samosa", variable=var,
                    value="Samosa", padx=20, font="lucida 13 bold").pack(anchor="w")

Button(root, text="Order Now", command=order,
       font="lucida 13 bold", padx=20, fg='white', bg='blue').pack()
root.mainloop()
