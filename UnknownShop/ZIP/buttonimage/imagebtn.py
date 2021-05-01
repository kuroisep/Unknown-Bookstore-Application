import tkinter
from tkinter import *
from tkinter import messagebox

def btnclick():
    messagebox.showinfo("Message","Button is clicked")

root = tkinter.Tk()
root.geometry("800x800")
root.configure(bg="#856fff")

photo = PhotoImage(file="UnknownShop/ZIP/buttonimage/group.png")
photo2 = PhotoImage(file="UnknownShop/ZIP/buttonimage/group.png")
btn = Button(
    root,
    image=photo,
    command=btnclick,
    border=0,
)
btn.pack(pady=50)

btn2 = Button(
    root,
    image=photo2,
    command=btnclick,
    border=20,
)
btn2.pack()
root.mainloop()