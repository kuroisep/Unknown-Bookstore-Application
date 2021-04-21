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
        bg_path = "UnknownShop\Picture\ShopPage\Shop_main_page.png"
        bg = ImageTk.PhotoImage(Image.open(bg_path).resize((1280, 720)))

        canvas = Canvas(self.shop_window, width=1280, height=720)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor="nw")

        # logo_path = "UnknownShop\Picture\ShopPage\logo.png"
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

        self.banner1_path = "UnknownShop\Picture\ShopPage\\banner1.jpg"
        self.banner2_path = "UnknownShop\Picture\ShopPage\\banner2.jpg"
        self.banner3_path = "UnknownShop\Picture\ShopPage\\banner3.jpg"
        self.banner1 = ImageTk.PhotoImage(Image.open(self.banner1_path))
        self.banner2 = ImageTk.PhotoImage(Image.open(self.banner2_path))
        self.banner3 = ImageTk.PhotoImage(Image.open(self.banner3_path))

        self.banner_label = tk.Label(self.shop_window)
        self.banner_label.pack()

        self.dot1_path = "UnknownShop\Picture\ShopPage\movingdot1.png"
        self.dot2_path = "UnknownShop\Picture\ShopPage\movingdot2.png"
        self.dot3_path = "UnknownShop\Picture\ShopPage\movingdot3.png"
        self.dot1 = ImageTk.PhotoImage(Image.open(self.dot1_path))
        self.dot2 = ImageTk.PhotoImage(Image.open(self.dot2_path))
        self.dot3 = ImageTk.PhotoImage(Image.open(self.dot3_path))

        self.dot_label = tk.Label(self.shop_window)
        self.dot_label.pack()

        button1_path = "UnknownShop\Picture\ShopPage\\button1.png"
        img_button1 = ImageTk.PhotoImage(Image.open(button1_path).resize((175, 48)))
        self.button1 = Button(image=img_button1)
        canvas.create_window(0, 222, window=self.button1,anchor = "nw")

        button2_path = "UnknownShop\Picture\ShopPage\\button2.png"
        img_button2 = ImageTk.PhotoImage(Image.open(button2_path).resize((175, 48)))
        self.button2 = Button(image=img_button2)
        canvas.create_window(0, 307, window=self.button2,anchor = "nw")

        button3_path = "UnknownShop\Picture\ShopPage\\button3.png"
        img_button3 = ImageTk.PhotoImage(Image.open(button3_path).resize((175, 48)))
        self.button3 = Button(image=img_button3)
        canvas.create_window(0, 393, window=self.button3,anchor = "nw")

        button4_path = "UnknownShop\Picture\ShopPage\\button4.png"
        img_button4 = ImageTk.PhotoImage(Image.open(button4_path).resize((175, 48)))
        self.button4 = Button(image=img_button4)
        canvas.create_window(0, 477, window=self.button4,anchor = "nw")

        button5_path = "UnknownShop\Picture\ShopPage\\button5.png"
        img_button5 = ImageTk.PhotoImage(Image.open(button5_path).resize((175, 48)))
        self.button5 = Button(image=img_button5)
        canvas.create_window(0, 563, window=self.button5,anchor = "nw")

        self.count = 0
        self.movebanner()
        self.shop_window.resizable(0, 0)
        self.shop_window.mainloop()

    def movebanner(self):
        if self.count == 30:
            self.count = 0
        if self.count == 0:
            self.banner_label.config(image=self.banner1)
            self.dot_label.config(image=self.dot1)
            self.banner_label.place(x=330, y=100)
            self.dot_label.place(x=630, y=405)
        elif self.count == 10:
            self.banner_label.config(image=self.banner2)
            self.dot_label.config(image=self.dot2)
        elif self.count == 20:
            self.banner_label.config(image=self.banner3)
            self.dot_label.config(image=self.dot3)
        self.count += 1
        self.banner_label.after(200, self.movebanner)


def showShopPage():
    Shop_main_screen()
# RunMain = Shop_main_screen()
