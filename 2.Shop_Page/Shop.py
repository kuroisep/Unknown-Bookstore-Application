import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image


shop_window = tk.Tk()
shop_window.title("Unknown Book Store")
x = (700) - (750/2)
y = (420) - (500/2)
shop_window.geometry("1280x720+%d+%d" % (x, y))


bg_path = "2.Shop_Page\PICTURE\Shop_bg.png"
bg = ImageTk.PhotoImage(Image.open(bg_path).resize((1280, 720)))

canvas = Canvas(shop_window, width=1280, height=720)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg,anchor="nw")




shop_window.resizable(0, 0)
shop_window.mainloop()