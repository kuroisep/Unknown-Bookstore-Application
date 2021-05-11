from tkinter import PhotoImage
import tkinter as tk
from PIL import ImageTk
from IPython.core.display import Image

# dictionary of colors:
color = {"nero": "#252726", "orange": "#D78BDC", "darkorange": "#D710FF"}

# setting root window:
root = tk.Tk()
root.title("Tkinter Navbar")
root.config(bg="gray17")
root.geometry("1280x720+850+50")

# setting switch state:
btnState = False

# loading Navbar icon image:
navIcon = PhotoImage(file="UnknownShop\\Picture\\ShopPage\ICON\\account.png",height = 100, width = 100)
closeIcon = PhotoImage(file="Ref\\coffee.png",height = 50, width = 50)


# setting switch function:
def switch():
    global btnState
    if btnState is True:
        # create animated Navbar closing:
        for x in range(301):
            navRoot.place(x=-x, y=0)
            topFrame.update()

        # resetting widget colors:
        brandLabel.config(bg="gray17", fg="green")
        homeLabel.config(bg=color["orange"])
        topFrame.config(bg=color["orange"])
        root.config(bg="gray17")

        # turning button OFF:
        btnState = False
    else:
        # make root dim:
        brandLabel.config(bg=color["nero"], fg="#5F5A33")
        homeLabel.config(bg=color["nero"])
        topFrame.config(bg=color["nero"])
        root.config(bg=color["nero"])

        # created animated Navbar opening:
        for x in range(-300, 0):
            navRoot.place(x=x, y=0)
            topFrame.update()

        # turing button ON:
        btnState = True

# top Navigation bar:
topFrame = tk.Frame(root, bg=color["orange"])
topFrame.pack(side="top", fill=tk.X)

# Header label text:
homeLabel = tk.Label(topFrame, text="PE", font="Bahnschrift 15", bg=color["orange"], fg="gray17", height=2, padx=20)
homeLabel.pack(side="right")

# Main label text:
brandLabel = tk.Label(root, text="Pythonista\nEmpire", font="System 30", bg="gray17", fg="green")
brandLabel.place(x=640, y=250)

# Navbar button:
navbarBtn = tk.Button(topFrame, image=navIcon, bg=color["nero"], activebackground=color["orange"], bd=0, padx=20, command=switch, height = 150, width = 150)
navbarBtn.place(x=10, y=10)

# setting Navbar frame:
navRoot = tk.Frame(root, bg="gray17", height=1000, width=300)
navRoot.place(x=-300, y=0)
tk.Label(navRoot, font="Bahnschrift 15", bg=color["orange"], fg="black", height=2, width=300, padx=20).place(x=0, y=0)

# set y-coordinate of Navbar widgets:
y = 80
# option in the navbar:
options = ["Profile", "Settings", "Help", "About", "Feedback", "Contact Us"]
# Navbar Option Buttons:
for i in range(6):
    tk.Button(navRoot, text=options[i], font="BahnschriftLight 15", bg="gray17", fg=color["orange"], activebackground="gray17", activeforeground="green", bd=0).place(x=25, y=y)
    y += 40

# Navbar Close Button:
closeBtn = tk.Button(navRoot, image=closeIcon, bg=color["orange"], activebackground=color["orange"], bd=0, command=switch, height = 50, width = 50)
closeBtn.place(x=250, y=0)

# window in mainloop:
root.mainloop()