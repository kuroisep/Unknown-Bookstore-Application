import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter.ttk import *

shop_window = tk.Tk()
shop_window.title("Unknown Book Store")
x = (700) - (750/2)
y = (420) - (500/2)
shop_window.geometry("1280x720+%d+%d" % (x, y))

bg_path = "PICTURE\Shop_bg.png"
bg = ImageTk.PhotoImage(Image.open(bg_path).resize((1280, 720)))

canvas = Canvas(shop_window, width=1280, height=720)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg,anchor="nw")

logo_path = "PICTURE\logo.png"
logo = ImageTk.PhotoImage(Image.open(logo_path).resize((150, 150)))

name = tk.StringVar()
nameEntered = ttk.Entry(shop_window, width = 70, textvariable = name)
nameEntered.place(x=200,y=50)

combo = Combobox(shop_window)
combo['values']= ("All","English Books","Thai Books")
combo.current(0) #set the selected item
combo.place(x=570,y=50)

button = ttk.Button(shop_window, text = "Search")
button.place(x=713,y=47)

label1 = tk.Label(image=logo)
label1.image = logo
label1.place(x=0, y=0)

shop_window.resizable(0, 0)

shop_window.mainloop()