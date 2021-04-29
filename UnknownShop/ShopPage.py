from logging import disable
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter.ttk import *
from tkinter import messagebox
import pandas
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from UnknownShop import LoginPage
# 
class Shop_main_screen:
    def __init__(self):
        self.shop_window = tk.Tk()
        self.shop_window.title("Unknown Book Store")
        x = (700) - (750/2)
        y = (420) - (500/2)
        self.shop_window.geometry("1280x720+%d+%d" % (x, y))
        # Create Canvas
        self.canvas = Canvas(self.shop_window, width=1280, height=720)

        #USER LOGIN
        self.df = pandas.read_csv('login.csv')
        self.user = self.df.loc[self.df['STATUS']=='T'].values.tolist()
        if self.user == []:
            # messagebox.showerror("Error", "NO USER LOGIN FOUND")
            print("NO USER LOGIN FOUND")
            self.user = [['T', 'NO USER LOGIN FOUND', '', 'You are not logged in', 'You are not logged in', 'You are not logged in', 'You are not logged in', 'You are not logged in']]
        #self.user[0][1] = username
        #self.user[0][2] = password
        #self.user[0][3] = name
        #self.user[0][4] = lastname
        #self.user[0][5] = gender
        #self.user[0][6] = email
        #self.user[0][7] = telphone

        self.infomationPage() # หน้า info 
        self.categoryPage()
        self.paymentPage()
        self.deliveryPage()


        self.create_background()

        self.create_logo()

        self.search_bar()

        self.set_banner()  ## <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        self.count = 0

        self.moveBanner()  ## <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        self.button_state()


        self.shop_window.resizable(0, 0)
        self.shop_window.overrideredirect(0)
        self.shop_window.mainloop()

    def create_background(self):
        bg_path = "Shop_Page\PICTURE\Shop_bg.png"
        self.bg = ImageTk.PhotoImage(Image.open(bg_path).resize((1280, 720)))

        # self.canvas = Canvas(self.shop_window, width=1280, height=720)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg,anchor="nw")

    def create_logo(self):
        
        img_logo_path = "Shop_Page\PICTURE\logo.png"
        self.img_logo = ImageTk.PhotoImage(Image.open(img_logo_path).resize((150, 150)))
        self.canvas.create_image(15, 15, image=self.img_logo, anchor="nw")

    def set_banner(self):
        banner1_path = "Shop_Page\PICTURE\\banner1.jpg"
        banner2_path = "Shop_Page\PICTURE\\banner2.jpg"
        banner3_path = "Shop_Page\PICTURE\\banner3.jpg"
        self.banner1 = ImageTk.PhotoImage(Image.open(banner1_path))
        self.banner2 = ImageTk.PhotoImage(Image.open(banner2_path))
        self.banner3 = ImageTk.PhotoImage(Image.open(banner3_path))

        self.banner_label = tk.Label(self.shop_window,compound='none')
        self.banner_label.pack()

        dot1_path = "Shop_Page\PICTURE\movingdot1.png"
        dot2_path = "Shop_Page\PICTURE\movingdot2.png"
        dot3_path = "Shop_Page\PICTURE\movingdot3.png"
        self.dot1 = ImageTk.PhotoImage(Image.open(dot1_path))
        self.dot2 = ImageTk.PhotoImage(Image.open(dot2_path))
        self.dot3 = ImageTk.PhotoImage(Image.open(dot3_path))

        self.dot_label = tk.Label(self.shop_window)
        self.dot_label.pack()

    def moveBanner(self):
        global after_id
       
        if self.count == 30 :
            self.count = 0

        if self.count == 0 :
            self.banner_label.config(image = self.banner1)
            self.dot_label.config(image = self.dot1)
            self.canvas.create_image(700,250,image=self.banner1)
            self.canvas.create_image(700,425,image=self.dot1)
            self.banner_label.place()
            self.dot_label.place()
        elif self.count == 10 :
            self.banner_label.config(image = self.banner2)
            self.canvas.create_image(700,250,image=self.banner2)
            self.canvas.create_image(700,425,image=self.dot2)
            self.dot_label.config(image = self.dot2)
        elif self.count == 20 :
            self.banner_label.config(image = self.banner3)
            self.canvas.create_image(700,250,image=self.banner3)
            self.canvas.create_image(700,425,image=self.dot3)
            self.dot_label.config(image = self.dot3)

        self.count += 1
        after_id = self.banner_label.after(200, self.moveBanner)
        

    def search_bar(self): 
        self.canvas.create_text(385, 61, text="Search By", font=('TRACK', 12))

        name = tk.StringVar()
        nameEntered = ttk.Entry(self.shop_window, width = 60, textvariable = name)
        nameEntered.place(x=535, y=50)

        drop = ttk.Combobox(self.shop_window, width=10, value=["All", "English Books", "Thai Books"])
        drop.current((0))
        drop.place(x=440, y=50)

        search_button = ttk.Button(self.shop_window, text = "Search")
        search_button.place(x=913, y=47)

        show_all_books_button = ttk.Button(self.shop_window, text = "Show All")
        show_all_books_button.place(x=1000, y=47)
        
        
    def button_state(self):
        button1_path = "UnknownShop\Picture\ShopPage\\button1.png"
        self.img_button1 = ImageTk.PhotoImage(Image.open(button1_path).resize((175, 48)))
        self.canvas.create_image(200,200,image=self.img_button1)
        self.button1 = Button(self.shop_window,image=self.img_button1,command = self.show_infomationPage)
        self.canvas.create_window(0, 200, window=self.button1, anchor="nw")

        button2_path = "UnknownShop\Picture\ShopPage\\button2.png"
        self.img_button2 = ImageTk.PhotoImage(Image.open(button2_path).resize((175, 48)))
        self.canvas.create_image(200,300,image=self.img_button2)
        self.button2 = Button(image=self.img_button2,command= self.show_categoryPage)
        self.canvas.create_window(0, 280, window=self.button2, anchor="nw")

        button3_path = "UnknownShop\Picture\ShopPage\\button3.png"
        self.img_button3 = ImageTk.PhotoImage(Image.open(button3_path).resize((175, 48)))
        self.canvas.create_image(200,400,image=self.img_button3)
        self.button3 = Button(image=self.img_button3,command=self.show_paymentPage)
        self.canvas.create_window(0, 360, window=self.button3, anchor="nw")

        button4_path = "UnknownShop\Picture\ShopPage\\button4.png"
        self.img_button4 = ImageTk.PhotoImage(Image.open(button4_path).resize((175, 48)))
        self.canvas.create_image(200,500,image=self.img_button4)
        self.button4 = Button(image=self.img_button4,command=self.show_deliveryPage)
        self.canvas.create_window(0, 440, window=self.button4, anchor="nw")

        button5_path = "UnknownShop\Picture\ShopPage\\button5.png"
        self.img_button5 = ImageTk.PhotoImage(Image.open(button5_path).resize((175, 48)))
        self.canvas.create_image(200,600,image=self.img_button5)
        self.button5 = Button(self.shop_window, image=self.img_button5, command=self.delete_show_window)
        self.canvas.create_window(0, 520, window=self.button5, anchor="nw")

        button6_path = "UnknownShop\Picture\ShopPage\\button5.png"
        self.img_button6 = ImageTk.PhotoImage(Image.open(button6_path).resize((175, 48)))
        self.button6 = Button(self.shop_window, image=self.img_button6, command=self.delete_show_window)
        self.canvas.create_window(0, 600, window=self.button6, anchor="nw")

    def get_data(self, row, column):
        self.scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name('UnknownShop\minor1981-a976b13f378a.json', self.scope)
        self.gc = gspread.authorize(self.credentials)
        self.data = self.gc.open('รายชื่อหนังสือ').sheet1
        self.row = self.data.row_values(row)[column]
        
        return str(self.row)

    def delete_show_window(self):
        if messagebox.askokcancel("Quit", "Do you want to sign out?"):
            self.df.loc[self.df['USER'] == self.user[0][1], 'STATUS'] = 'F'
            self.df.to_csv("login.csv", index=False)
            self.shop_window.destroy()
            # self.shop_window.after_cancel(after_id)
            # LoginPage.showLoginPage()
    
    def infomationPage(self): # ข้อมูลหน้า info       #1
        self.inner_infomation = Canvas(self.canvas, width=1000, height=550)

        self.username = StringVar()
        self.password = StringVar()
        self.confpassword = StringVar()
        self.name = StringVar()
        self.lastname = StringVar()
        self.email = StringVar()
        self.gender = StringVar()
        self.gender_choice1 = IntVar()
        self.gender_choice2 = IntVar()
        self.telphone = StringVar()
        
        if self.user != []:
            ## NAME
            self.inner_infomation.create_text(150, 100, anchor=NW, text='Name : ')
            self.username_entry = Entry(self.inner_infomation, textvariable=self.username,font=('Verdana',15))
            self.username_entry.insert(0,self.user[0][3])
            self.username_entry.config(state=DISABLED)
            # print(self.username_entry["state"])
            self.inner_infomation.create_window(210,80,window=self.username_entry,anchor = 'nw')
            ##LASTNAME
            self.inner_infomation.create_text(150, 150, anchor=NW, text='Lastname : ')
            self.lname_entry = Entry(self.inner_infomation, textvariable=self.lastname)
            self.lname_entry.insert(0,self.user[0][4])
            self.lname_entry.config(state=DISABLED)
            self.inner_infomation.create_window(275,155,window=self.lname_entry)
            ##GENDER
            self.inner_infomation.create_text(150, 200, anchor=NW, text='Gender : ')
            self.gender_entry = Entry(self.inner_infomation, textvariable=self.gender)
            self.gender_entry.insert(0,self.user[0][5])
            self.gender_entry.config(state=DISABLED)
            self.inner_infomation.create_window(275,205,window=self.gender_entry)
            ##EMAIL
            self.inner_infomation.create_text(150, 250, anchor=NW, text='Email : ')
            self.email_entry = Entry(self.inner_infomation, textvariable=self.email)
            self.email_entry.insert(0,self.user[0][6])
            self.email_entry.config(state=DISABLED)
            self.inner_infomation.create_window(275,255,window=self.email_entry)
            ##PHONE
            self.inner_infomation.create_text(150, 300, anchor=NW, text='Telphone : ')
            self.telphone_entry = Entry(self.inner_infomation, textvariable=self.telphone)
            self.telphone_entry.insert(0,self.user[0][7])
            self.telphone_entry.config(state=DISABLED)
            self.inner_infomation.create_window(275,305,window=self.telphone_entry)

    def categoryPage(self):
        self.inner_category = Canvas(self.canvas, width=1000, height=550)
        self.inner_category.create_text(500, 275, font = 50, anchor=CENTER, text="categoryPage")
    def paymentPage(self):
        self.inner_payment = Canvas(self.canvas, width=1000, height=550)   
        self.inner_payment.create_text(500, 275, font = 50, anchor=CENTER, text="paymentPage")
    def deliveryPage(self):
        self.inner_delivery = Canvas(self.canvas, width=1000, height=550)   
        self.inner_delivery.create_text(500, 275, font = 50, anchor=CENTER, text="deliveryPage")

    def show_infomationPage(self): # ุปุ่ม 1
        self.delete_canvas()
        self.canvas.create_window(250, 150, anchor=NW, window=self.inner_infomation)
    def show_categoryPage(self):
        self.delete_canvas()
        self.canvas.create_window(250, 150, anchor=NW, window=self.inner_category)
    def show_paymentPage(self):
        self.delete_canvas()
        self.canvas.create_window(250,150, anchor=NW, window=self.inner_payment)
    def show_deliveryPage(self):
        self.delete_canvas()
        self.canvas.create_window(250,150, anchor=NW, window=self.inner_delivery)

    def delete_canvas(self): # ปุ่ม 2                #3
        self.canvas.create_window(2000, 700, anchor=NW, window=self.inner_infomation)
        self.canvas.create_window(2200,750, anchor=NW, window=self.inner_category)
        self.canvas.create_window(2400,750, anchor=NW, window=self.inner_payment)
        self.canvas.create_window(2600,750, anchor=NW, window=self.inner_delivery)
        
         # ลบหน้า info
    
    ## 1. def ข้อมูลหน้านั้น -> ใส่ใน init
    ## 2. def แสดงข้อมูลหน้านัั้น -> ใส่ delete ก่อน
    ## 3. ใน def delete เอาหน้านั้นไปใส่


        

def showShopPage():
    run = Shop_main_screen()

if __name__ == '__main__':
    showShopPage()
