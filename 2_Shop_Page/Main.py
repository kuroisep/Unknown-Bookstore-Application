import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter.ttk import *

class Shop_main_screen:
    def __init__(self):
        self.shop_window = tk.Tk()
        self.shop_window.title("Unknown Book Store")
        x = (700) - (750/2)
        y = (420) - (500/2)
        self.shop_window.geometry("1280x720+%d+%d" % (x, y))
        bg_path = "2_Shop_Page\PICTURE\Shop_main_page.png"
        bg = ImageTk.PhotoImage(Image.open(bg_path).resize((1280, 720)))

        canvas = Canvas(self.shop_window, width=1280, height=720)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor="nw")

        # logo_path = "2_Shop_Page\PICTURE\logo.png"
        # logo = ImageTk.PhotoImage(Image.open(logo_path).resize((150, 150)))

        name = tk.StringVar()
        nameEntered = ttk.Entry(self.shop_window, width=70, textvariable=name)
        nameEntered.place(x=400, y=50)

        combo = Combobox(self.shop_window)
        combo['values'] = ("All", "English Books", "Thai Books")
        combo.current(0)  # set the selected item
        combo.place(x=770, y=50)

        button = ttk.Button(self.shop_window, text="Search")
        button.place(x=913, y=47)

        # label1 = tk.Label(image=logo)
        # label1.image = logo
        # label1.place(x=0, y=0)

        banner1_path = "2_Shop_Page\PICTURE\\banner1.jpg"
        banner2_path = "2_Shop_Page\PICTURE\\banner2.jpg"
        banner3_path = "2_Shop_Page\PICTURE\\banner3.jpg"
        banner1 = ImageTk.PhotoImage(Image.open(banner1_path))
        banner2 = ImageTk.PhotoImage(Image.open(banner2_path))
        banner3 = ImageTk.PhotoImage(Image.open(banner3_path))

        banner_label = tk.Label(self.shop_window)
        banner_label.pack()

        dot1_path = "2_Shop_Page\PICTURE\movingdot1.png"
        dot2_path = "2_Shop_Page\PICTURE\movingdot2.png"
        dot3_path = "2_Shop_Page\PICTURE\movingdot3.png"
        dot1 = ImageTk.PhotoImage(Image.open(dot1_path))
        dot2 = ImageTk.PhotoImage(Image.open(dot2_path))
        dot3 = ImageTk.PhotoImage(Image.open(dot3_path))

        dot_label = tk.Label(self.shop_window)
        dot_label.pack()
        global x
        x = 0

        def moveBanner(self):
                if x == 30:
                    x = 0

                if x == 0:
                    banner_label.config(image=banner1)
                    dot_label.config(image=dot1)
                    banner_label.place(x=330, y=100)
                    dot_label.place(x=630, y=405)
                elif x == 10:
                    banner_label.config(image=banner2)
                    dot_label.config(image=dot2)
                elif x == 20:
                    banner_label.config(image=banner3)
                    dot_label.config(image=dot3)

                x += 1
                banner_label.after(200, moveBanner)

        moveBanner(self)

        self.shop_window.resizable(0, 0)
        self.shop_window.mainloop()
RunMain = Shop_main_screen()