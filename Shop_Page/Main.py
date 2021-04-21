import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter.ttk import *
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class shoppage():

    def __init__(self):
        self.shop_window = tk.Tk()
        self.shop_window.title("Unknown Book Store")
        x = (700) - (750/2)
        y = (420) - (500/2)
        self.shop_window.geometry("1280x720+%d+%d" % (x, y))

        self.create_background()

        self.create_logo()

        self.search()

        self.set_banner()
        self.count = 0
        self.moveBanner()

        # self.test_search()
        self.shop_window.resizable(0, 0)
        self.shop_window.mainloop()

    def create_background(self):
        bg_path = "Shop_Page\PICTURE\Shop_bg.png"
        self.bg = ImageTk.PhotoImage(Image.open(bg_path).resize((1280, 720)))

        self.canvas = Canvas(self.shop_window, width=1280, height=720)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg,anchor="nw")

    def create_logo(self):
        logo_path = "Shop_Page\PICTURE\logo.png"
        logo = ImageTk.PhotoImage(Image.open(logo_path).resize((150, 150)))

        label1 = tk.Label(image=logo)
        label1.image = logo
        label1.place(x=0, y=0)

    def set_banner(self):
        banner1_path = "Shop_Page\PICTURE\\banner1.jpg"
        banner2_path = "Shop_Page\PICTURE\\banner2.jpg"
        banner3_path = "Shop_Page\PICTURE\\banner3.jpg"
        self.banner1 = ImageTk.PhotoImage(Image.open(banner1_path))
        self.banner2 = ImageTk.PhotoImage(Image.open(banner2_path))
        self.banner3 = ImageTk.PhotoImage(Image.open(banner3_path))

        self.banner_label = tk.Label(self.shop_window)
        self.banner_label.pack()

        dot1_path = "Shop_Page\PICTURE\movingdot1.png"
        dot2_path = "Shop_Page\PICTURE\movingdot2.png"
        dot3_path = "Shop_Page\PICTURE\movingdot3.png"
        self.dot1 = ImageTk.PhotoImage(Image.open(dot1_path))
        self.dot2 = ImageTk.PhotoImage(Image.open(dot2_path))
        self.dot3 = ImageTk.PhotoImage(Image.open(dot3_path))

        self.dot_label = tk.Label(self.shop_window)
        self.dot_label.pack()

    def moveBanner(self) :
        if self.count == 30 :
            self.count = 0

        if self.count == 0 :
            self.banner_label.config(image = self.banner1)
            self.dot_label.config(image = self.dot1)
            self.banner_label.place(x=330,y=100)
            self.dot_label.place(x=630,y=405)
        elif self.count == 10 :
            self.banner_label.config(image = self.banner2)
            self.dot_label.config(image = self.dot2)
        elif self.count == 20 :
            self.banner_label.config(image = self.banner3)
            self.dot_label.config(image = self.dot3)

        self.count += 1
        self.banner_label.after(200, self.moveBanner)

    def search(self):
    
        name = tk.StringVar()
        nameEntered = ttk.Entry(self.shop_window, width = 70, textvariable = name)
        nameEntered.place(x=400,y=50)

        drop = ttk.Combobox(self.shop_window, value=["All", "English Books", "Thai Books"])
        drop.current((0))
        drop.place(x=770, y=50)

        search_button = ttk.Button(self.shop_window, text = "Search")
        search_button.place(x=913,y=47)

def test_search():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('Minor\minor1981-a976b13f378a.json', scope)

    gc = gspread.authorize(credentials)

    data = gc.open('Table').sheet1

    row = data.get_all_records()


    print(row)
        
        
Run = shoppage()