from tkinter import *
root=Tk()
root.title(" My GUI ")
cwidth=800
cheight=400
root.geometry(f"{cwidth}x{cheight}")
can_widget=Canvas(root,width=cwidth,height=cheight)
can_widget.pack()
can_widget.create_line(0,0,800,400)
can_widget.create_line(0,400,800,0)

root.mainloop()