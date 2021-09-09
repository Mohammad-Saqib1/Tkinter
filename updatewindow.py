from tkinter import *
root = Tk()
root.geometry('400x250')
root.title("Update Window")


def update():
    print("Updating GUI")
    root.geometry(f"{width.get()}x{height.get()}")


width = StringVar()
height = StringVar()
Label(root, text="Width", font="lucida 13 bold").pack()
Entry(root, textvariable=width, relief=SUNKEN).pack(pady=10)
Label(root, text="Height", font="lucida 13 bold").pack()

Entry(root, textvariable=height, relief=SUNKEN).pack(pady=10)
Button(root, text="Apply", command=update,
       font="lucida 13 bold", pady=10, relief=SUNKEN).pack()


root.mainloop()
