from logging import disable
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter.ttk import *
from tkinter import filedialog, messagebox
import pandas
import os, sys
import re
import cv2
from tkinter.filedialog import SaveFileDialog, askopenfilename
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import mysql.connector

from UnknownShop import LoginPage
import pandas as pd
from time import sleep
import time



class Shop_main_screen:
    def __init__(self):
        self.shop_window = tk.Tk()
        self.shop_window.protocol("WM_DELETE_WINDOW", self.deleteX_show_window)
        self.shop_window.title("Unknown Book Store")
        x = (700) - (750/2)
        y = (420) - (500/2)
        self.shop_window.geometry("1280x720+%d+%d" % (x, y))
        # Create Canvas
        self.canvas = Canvas(self.shop_window, width=1280, height=720, bd=0, highlightthickness=0)


        # Variable Book
        self.No = StringVar()
        self.Name = StringVar()
        self.Author = StringVar()
        self.Category = StringVar()
        self.Language = StringVar()
        self.Price = StringVar()
        self.Code = StringVar()
        self.Rating = StringVar()
        self.Example = StringVar()

        # """ 
        # THEAM
        # """
        # style = ttk.Style(self.shop_window)
        # # Import the tcl file
        # self.shop_window.tk.call('source', 'UnknownShop/azure.tcl')

        # # Set the theme with the theme_use method
        # style.theme_use('azure')
        # style.configure('flat.TButton', borderwidth=0)
        # # style.configure("Treeview", font=('TRACK',13,'bold'))
        # """ 
        # THEAM
        # """

        #USER LOGIN
        self.df = pandas.read_csv('login.csv')
        self.user = self.df.loc[self.df['STATUS']=='T'].values.tolist()
        self.user_imagefile = ''
        self.usercart = []
        if self.user == []:
            # messagebox.showerror("Error", "NO USER LOGIN FOUND")
            print("NO USER LOGIN FOUND")
            self.user = [['T', '\" Login Required \"', '', 
            'You are not logged in', 'You are not logged in', 
            '-','-/-/-', 'You are not logged in', 
            'You are not logged in','account']]
        #self.user[0][1] = username
        #self.user[0][2] = password
        #self.user[0][3] = name
        #self.user[0][4] = lastname
        #self.user[0][5] = gender
        #self.user[0][6] = birthday
        #self.user[0][7] = email
        #self.user[0][8] = telphone
        #self.user[0][9] = picture


        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Load data book >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.loadbookfile = pandas.read_csv('UnknownShop\database\DataBookList.csv')
        self.book_data = self.loadbookfile.values.tolist()

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>





        
        # self.canvas=Canvas(self.shop_window,bg='#7242f5')
        # self.canvas.pack(fill=BOTH, expand=1)
        # text_var=" ______ Welcome to the land of bookS ______"
        # text=self.canvas.create_text(0,-2000,text=text_var,font=('Times New Roman',20,'bold'),fill='white',tags=("marquee",),anchor='w')
        # x1,y1,x2,y2 = self.canvas.bbox("marquee")
        # width = x2-x1
        # height = y2-y1
        # self.canvas['width']=width
        # self.canvas['height']=height
        # fps=40    #Change the fps to make the animation faster/slower



        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.infomationPage() # หน้า info 
        self.categoryPage()
        self.paymentPage()
        self.deliveryPage()
        self.create_background()
        # self.search_bar()
        self.shift()
        self.menuTab()

        ## <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        self.set_banner()
        self.count = 0
        self.moveBanner()
        ## <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 


        self.button_state()

        self.shop_window.resizable(0, 0)
        self.shop_window.overrideredirect(0)
        self.shop_window.mainloop()

    def create_background(self): # <<<<<<<<<<<<<<<<<<<<<<<<<<< BG
        bg_path = "UnknownShop\Picture\Draf BG.png" 
        self.bg = ImageTk.PhotoImage(Image.open(bg_path).resize((1280, 720)))

        # self.canvas = Canvas(self.shop_window, width=1280, height=720)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg,anchor="nw")

    def set_banner(self):
        # BANNER <<<<<<<<<<<<<<<<<<<<<<<<<<
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
                self.canvas.create_image(700,300,image=self.banner1)
                self.canvas.create_image(700,475,image=self.dot1)
                self.banner_label.place()
                self.dot_label.place()
            elif self.count == 10 :
                self.banner_label.config(image = self.banner2)
                self.canvas.create_image(700,300,image=self.banner2)
                self.canvas.create_image(700,475,image=self.dot2)
                self.dot_label.config(image = self.dot2)
            elif self.count == 20 :
                self.banner_label.config(image = self.banner3)
                self.canvas.create_image(700,300,image=self.banner3)
                self.canvas.create_image(700,475,image=self.dot3)
                self.dot_label.config(image = self.dot3)

            self.count += 1
            after_id = self.banner_label.after(200, self.moveBanner)
        

    def search_bar(self): 
        self.canvas.create_text(290, 65, text="Search By", font=('TRACK', 12))

        drop1 = ttk.Combobox(self.shop_window, width=10, value=["Arts / Design / Decoration", "Literature", 
                                                                "Administration / Management", "Humanities / Science", 
                                                                "Children's Books","Career Academic Textbooks", "Psychology"])
        drop1.current((0))
        drop1.place(x=345, y=50)

        drop2 = ttk.Combobox(self.shop_window, width=10, value=["Code", "Name", "Author"])
        drop2.current((0))
        drop2.place(x=440, y=50)

        nameEntered = ttk.Entry(self.shop_window, width = 50, textvariable = self.Name)
        nameEntered.place(x=535, y=50)

        search_button = ttk.Button(self.shop_window, text = "Search")
        search_button.place(x=855, y=50)

        show_all_books_button = ttk.Button(self.shop_window, text = "Clear")
        show_all_books_button.place(x=943, y=50)

    def menuTab(self):

        img_logo_path = "Shop_Page\PICTURE\logo.png"
        self.img_logo = ImageTk.PhotoImage(Image.open(img_logo_path).resize((85, 85)))
        self.canvas.create_image(0, 0, image=self.img_logo, anchor="nw")

        Frame1 = tk.LabelFrame(self.shop_window, borderwidth=0, highlightthickness=0, bg="#1265db")
        Frame1.place(x=100, y=0, height=30, width=1280)
        
        tk.Label(Frame1, text=' Welcome User',background="#1200db", fg="white", borderwidth=0, highlightthickness=0, font=('TRACK', 12)
               ).grid(column=0, row=0)


        Frame2 = tk.LabelFrame(self.shop_window, borderwidth=0, highlightthickness=0, bg="#1200db")
        Frame2.place(x=100, y=30, height=45, width=1280)

        tk.Button(Frame2, text='HOME',background="#1200db",fg="white", width=40, borderwidth=0, highlightthickness=0, font=('TRACK', 12),activebackground="#1200db",command = self.show_HomePage
               ).grid(column=0, row=0, padx=20, pady=10)
        tk.Button(Frame2, text='My Profile', width=10,bg="#1200db",fg="white", borderwidth=0, highlightthickness=0, font=('TRACK', 12),activebackground="#1200db",command = self.show_infomationPage
               ).grid(column=1, row=0, padx=5, pady=10)
        tk.Button(Frame2, text='Shopping', width=10,bg="#1200db",fg="white", borderwidth=0, highlightthickness=0, font=('TRACK', 12),activebackground="#1200db",command= self.show_categoryPage
               ).grid(column=2, row=0, padx=5, pady=10)
        tk.Button(Frame2, text='My Cart', width=10,bg="#1200db",fg="white", borderwidth=0, highlightthickness=0, font=('TRACK', 12),activebackground="#1200db",command=self.show_paymentPage
               ).grid(column=3,row=0, padx=5, pady=10)
        tk.Button(Frame2, text='Delivery Status', width=15,bg="#1200db",fg="white", borderwidth=0, highlightthickness=0, font=('TRACK', 12),activebackground="#1200db",command=self.show_deliveryPage
               ).grid(column=4,row=0, padx=5, pady=10)
        tk.Button(Frame2, text='Contact Us', width=10,fg="white", bg="#1200db", borderwidth=0, highlightthickness=0, font=('TRACK', 12),activebackground="#1200db",command=self.delete_canvas
               ).grid(column=5,row=0, padx=5, pady=10)

        
        

    def value_set_one(self):
        self.value = 1

    def print_value(self):
        print(self.value)
        
    def button_state(self):

        # button1_path = "UnknownShop\Picture\ShopPage\\button1.png"
        # self.img_button1 = ImageTk.PhotoImage(Image.open(button1_path).resize((175, 48)))
        # # self.canvas.create_image(200,200,image=self.img_button1)
        # self.button1 = tk.Button(self.shop_window,image=self.img_button1, command = self.show_infomationPage, borderwidth=0)
        
        # self.canvas.create_window(0, 200, window=self.button1, anchor="nw")

        # button2_path = "UnknownShop\Picture\ShopPage\\button2.png"
        # self.img_button2 = ImageTk.PhotoImage(Image.open(button2_path).resize((175, 48)))
        # # self.canvas.create_image(200,300,image=self.img_button2)
        # self.button2 = tk.Button(image=self.img_button2,command= self.show_categoryPage, borderwidth=0, )
        # self.canvas.create_window(0, 280, window=self.button2, anchor="nw")

        # button3_path = "UnknownShop\Picture\ShopPage\\button3.png"
        # self.img_button3 = ImageTk.PhotoImage(Image.open(button3_path).resize((175, 48)))
        # # self.canvas.create_image(200,400,image=self.img_button3)
        # self.button3 = tk.Button(image=self.img_button3,command=self.show_paymentPage, borderwidth=0)
        # self.canvas.create_window(0, 360, window=self.button3, anchor="nw")

        # button4_path = "UnknownShop\Picture\ShopPage\\button4.png"
        # self.img_button4 = ImageTk.PhotoImage(Image.open(button4_path).resize((175, 48)))
        # # self.canvas.create_image(200,500,image=self.img_button4)
        # self.button4 = tk.Button(image=self.img_button4,command=self.show_deliveryPage, borderwidth=0, 
        #                         relief=FLAT, bg="#856fff",activebackground='#4444ff')
        # self.canvas.create_window(0, 440, window=self.button4, anchor="nw")

        # button5_path = "UnknownShop\Picture\ShopPage\\button5.png"
        # self.img_button5 = ImageTk.PhotoImage(Image.open(button5_path).resize((175, 48)))
        # # self.canvas.create_image(200,600,image=self.img_button5)
        # self.button5 = tk.Button(self.shop_window, image=self.img_button5, command=self.delete_canvas, border=0,
        #                         relief=FLAT, bg="#856fff",activebackground='#4444ff')
        # self.canvas.create_window(0, 520, window=self.button5, anchor="nw")
       

        # button6_path = "UnknownShop\Picture\ShopPage\\button5.png"
        # self.img_button6 = ImageTk.PhotoImage(Image.open(button6_path).resize((175, 48)))
        # # self.canvas.create_image(200,600,image=self.img_button6)
        # self.button6 = tk.Button(self.shop_window, image=self.img_button6, command=self.delete_show_window, border=0,
        #                         relief=FLAT, bg="#856fff",activebackground='#4444ff')
        # self.canvas.create_window(0, 600, window=self.button6, anchor="nw")
        pass
    

    def delete_show_window(self):
        if messagebox.askokcancel("Quit", "Do you want to sign out?"):
            # self.df.loc[self.df['USER'] == self.user[0][1], 'STATUS'] = 'F'
            # self.df.to_csv("login.csv", index=False)
            self.shop_window.destroy()
            # self.shop_window.after_cancel(after_id)
            # LoginPage.showLoginPage()
    def deleteX_show_window(self):
        # self.df.loc[self.df['USER'] == self.user[0][1], 'STATUS'] = 'F'
        # self.df.to_csv("login.csv", index=False)
        self.shop_window.destroy()
        # self.shop_window.after_cancel(after_id)

    def HomePage(self):
        self.inner_HomePage = Canvas(self.canvas, width=1280, height=550)

        self.HomePageFrame1 = tk.LabelFrame(self.inner_HomePage , text="HomePage_BANNER")
        self.HomePageFrame1.place(x=100, y=10, height=350, width=1080)


        HomePageFrame2 = tk.LabelFrame(self.inner_HomePage , text="Selected Menu")
        HomePageFrame2.place(x=100, y=370, height=150, width=1080)

        
        buy_button = tk.Button(HomePageFrame2,text="1", width=10)
        buy_button.grid(row=0,column=0,padx=20, pady=5)
        buy_button = tk.Button(HomePageFrame2,text="2", width=10)
        buy_button.grid(row=1,column=0,padx=20, pady=5)
        # bbuy_button = tk.Button(HomePageFrame2,text="3", width=10)
        # bbuy_button.grid(row=2,column=0,padx=20, pady=5)
    

        buy_button = tk.Button(HomePageFrame2,text="Buy Books", width=15)
        buy_button.grid(row=2,column=2,padx=80, pady=10)

        Status_button = tk.Button(HomePageFrame2,text="Status",width=15)
        Status_button.grid(row=2,column=3,padx=10, pady=10)

        Review_button = tk.Button(HomePageFrame2,text="Review Books",width=15)
        Review_button.grid(row=2,column=4,padx=50, pady=10)

        ContactUs_button = tk.Button(HomePageFrame2,text="Buy Books",width=15)
        ContactUs_button.grid(row=2,column=5,padx=40, pady=10)
       
        

        

    def infomationPage(self): # ข้อมูลหน้า info       #1
        self.inner_infomation = Canvas(self.canvas, width=1280, height=550)
        
        infomationPageFrame1 = tk.LabelFrame(self.inner_infomation , text="INFOMATION")
        infomationPageFrame1.place(x=100, y=0, height=550, width=1080)

        self.infomationPageFrame2 = tk.LabelFrame(self.inner_infomation , text="PICTURE")
        self.infomationPageFrame2.place(x=700, y=0, height=400, width=500)


        if self.user != []:
            ## USERNAME
            username_text = Label(infomationPageFrame1, text="Username".format(self.user[0][1]))
            username1_text = Label(infomationPageFrame1, text=self.user[0][1])
            username_text.grid(row=0, column=0, padx=10, pady=10,sticky="E")
            username1_text.grid(row=0, column=1, padx=10, pady=5,sticky="W")
            ## NAME
            name_text = Label(infomationPageFrame1, text="Name")
            name_text.grid(row=1, column=0, padx=10, pady=5,sticky="E")
            self.name_entry = Entry(infomationPageFrame1)
            self.name_entry.insert(0,self.user[0][3])
            self.name_entry.config(state=DISABLED)
            self.name_entry.grid(row=1, column=1, padx=10, pady=5)
            ##LASTNAME
            lname_text = Label(infomationPageFrame1, text="Lastname")
            lname_text.grid(row=2, column=0, padx=10, pady=5,sticky="E")
            self.lname_entry = Entry(infomationPageFrame1)
            self.lname_entry.insert(0,self.user[0][4])
            self.lname_entry.config(state=DISABLED)
            self.lname_entry.grid(row=2, column=1, padx=10, pady=5)
            ##GENDER
            gender_text = Label(infomationPageFrame1, text="Gender")
            gender_text.grid(row=3, column=0, padx=10, pady=5,sticky="E")
            self.gender_entry = Combobox(infomationPageFrame1, width=8,value=['MALE','FEMALE']) 
            self.gender_entry.insert(0,self.user[0][5])
            self.gender_entry.config(state=DISABLED)
            self.gender_entry.grid(row=3, column=1, padx=10, pady=5,sticky="W")
            ##BIRTHDAY
                    #DATE
            birthday_text = Label(infomationPageFrame1, text="Birthday")
            birthday_text.grid(row=4, column=0, padx=10, pady=5,sticky="E")
            self.birthday_date_entry = Combobox(infomationPageFrame1, width=3,value=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
                                                                             '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', 
                                                                             '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']) 
            self.birthday_date_entry.insert(0,self.user[0][6].split('/')[0])
            self.birthday_date_entry.config(state=DISABLED)
            self.birthday_date_entry.grid(row=4, column=1, padx=10, pady=5,sticky="W")
                    #MONTH
            self.birthday_month_entry = Combobox(infomationPageFrame1, width=5, value=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                                                                                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] )
            self.birthday_month_entry.insert(0,self.user[0][6].split('/')[1])
            self.birthday_month_entry.config(state=DISABLED)
            self.birthday_month_entry.place(x=180,y=165)
                    #YEAR
            year_list = []
            for i in range(1920,2022):
                year_list.append(str(i))
            self.birthday_year_entry = Combobox(infomationPageFrame1, width=5, value=year_list)
            self.birthday_year_entry.insert(0,self.user[0][6].split('/')[2])
            self.birthday_year_entry.config(state=DISABLED)
            self.birthday_year_entry.place(x=260,y=165)
            ##EMAIL
            email_text = Label(infomationPageFrame1, text="Email")
            email_text.grid(row=5, column=0, padx=10, pady=5,sticky="E")
            self.email_entry = Entry(infomationPageFrame1)
            self.email_entry.insert(0,self.user[0][7])
            self.email_entry.config(state=DISABLED)
            self.email_entry.grid(row=5, column=1, padx=10, pady=5)
            ##PHONE
            telphone_text = Label(infomationPageFrame1, text="Phone Number")
            telphone_text.grid(row=6, column=0, padx=10, pady=5,sticky="E")
            self.telphone_entry = Entry(infomationPageFrame1)
            self.telphone_entry.insert(0,self.user[0][8])
            self.telphone_entry.config(state=DISABLED)
            self.telphone_entry.grid(row=6, column=1, padx=10, pady=5)
            ##EDIT BUTTON
            Label(infomationPageFrame1, text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n").grid(row=8, column=0, padx=10, pady=5)
            Label(infomationPageFrame1, text="").grid(row=8, column=1, padx=10, pady=5)
            self.edit_info_button = Button(infomationPageFrame1,text='Edit', command=self.edit_infomation_state)
            self.edit_info_button.grid(row=8, column=2, padx=10, pady=5)
            ##DONE BUTTON
            self.done_info_button = Button(infomationPageFrame1,text='Done',state=DISABLED, command=self.edit_infomation_state)
            self.done_info_button.grid(row=8, column=3, padx=10, pady=5)

            ##PICTURE
            image_path = "UnknownShop/Picture/ShopPage/USER_PIC/{}.png".format(self.user[0][9])
            self.user_img = ImageTk.PhotoImage(Image.open(image_path).resize((300, 300)))
            self.user_imginput = ''

            self.imageselect_info_button = Button(self.infomationPageFrame2,text='select',state=DISABLED, command=self.openimage)
            self.imageselect_info_button.pack(side="bottom")
            self.user_image = Label(self.infomationPageFrame2, image=self.user_img)
            self.user_image.pack()
            
    def openfn(self):
        self.user_imagefile = filedialog.askopenfilename(initialdir='UnknownShop\\Picture\\ShopPage\\USER_PIC',title='open')
        return self.user_imagefile
    def openimage(self):
        self.user_imginput = self.openfn()
        if self.user_imginput != '':
            self.user_img = ImageTk.PhotoImage(Image.open(self.user_imginput).resize((300, 300)))
            self.user_image = Label(self.infomationPageFrame2, image=self.user_img)
            self.user_image.pack()
        

    def edit_infomation_state(self):
        if str(self.name_entry['state']) == 'disabled':
            self.name_entry.config(state=NORMAL)
            self.lname_entry.config(state=NORMAL)
            self.gender_entry.config(state=NORMAL)
            self.birthday_date_entry.config(state=NORMAL)
            self.birthday_month_entry.config(state=NORMAL)
            self.birthday_year_entry.config(state=NORMAL)
            self.email_entry.config(state=NORMAL)
            self.telphone_entry.config(state=NORMAL)
            self.edit_info_button.config(state=DISABLED)
            self.done_info_button.config(state=NORMAL)
            self.imageselect_info_button.config(state=NORMAL)
        else:
            self.edit_infomation_file()

    def edit_infomation_file(self):
        name_info = self.name_entry.get()
        lastname_info = self.lname_entry.get()
        email_info = self.email_entry.get()
        # gender_info = 'MALE'
        tel_info = self.telphone_entry.get()
        birthday_info = str(self.birthday_date_entry.get()) + '/' +  str(self.birthday_month_entry.get()) + '/' + str(self.birthday_year_entry.get())

        email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")

        if (name_info == ''):
            messagebox.showinfo(
                "Info", "Please Enter First Name", parent=self.shop_window)

        elif (lastname_info == ''):
            messagebox.showinfo("Info", "Please Enter Last Name",
                                parent=self.shop_window)

        # elif (self.gender1.get() == 0 and self.gender2.get() == 0):
        #     messagebox.showinfo(
        #         "Error", "Please Select Your Gender", parent=self.register_screen)

        elif (email_info == ''):
            messagebox.showinfo(
                "Info", "Please Enter Your Email", parent=self.shop_window)

        elif (email_regex.match(email_info) == None):
            messagebox.showerror("Error", "Email Invalid", parent=self.shop_window)

        elif (tel_info == ''):
            messagebox.showinfo(
                "Info", "Please Enter Phone Number", parent=self.shop_window)
        
        elif (tel_info.isdigit() == False or len(tel_info) != 10):
            messagebox.showerror("Error", "Phone Number Invalid",parent=self.shop_window)
            self.telphone_entry.delete(0,END)

        else:
            if messagebox.askokcancel("Confirm", "Are you sure?"):
                self.name_entry.config(state=DISABLED)
                self.lname_entry.config(state=DISABLED)
                self.gender_entry.config(state=DISABLED)
                self.birthday_date_entry.config(state=DISABLED)
                self.birthday_month_entry.config(state=DISABLED)
                self.birthday_year_entry.config(state=DISABLED)
                self.email_entry.config(state=DISABLED)
                self.telphone_entry.config(state=DISABLED)
                self.edit_info_button.config(state=NORMAL)
                self.done_info_button.config(state=DISABLED)
                self.imageselect_info_button.config(state=DISABLED)
                self.df.loc[self.df['USER'] == self.user[0][1], 'NAME'] = str(name_info).capitalize()
                self.df.loc[self.df['USER'] == self.user[0][1], 'LNAME'] = str(lastname_info).capitalize()
                self.df.loc[self.df['USER'] == self.user[0][1], 'GENDER'] = str(self.gender_entry.get())
                self.df.loc[self.df['USER'] == self.user[0][1], 'BIRTHDAY'] = str(birthday_info)
                self.df.loc[self.df['USER'] == self.user[0][1], 'EMAIL'] = str(email_info)
                self.df.loc[self.df['USER'] == self.user[0][1], 'TEL'] = str(tel_info)
                self.df.loc[self.df['USER'] == self.user[0][1], 'PICTURE'] = str(self.user[0][1])
                self.df.to_csv("login.csv", index=False)
                if self.user_imginput != '':
                    temp_img = cv2.imread(self.user_imginput)
                    cv2.imwrite('UnknownShop\\Picture\\ShopPage\\USER_PIC\\{}.png'.format(self.user[0][1]), temp_img)
                
    # def selectItem(self,a):
    #     curItem = self.tv1.focus()
    #     self.current_book = self.tv1.item(curItem)['values']
    #     #self.current_book[0] = ลำดับที่
    #     #self.current_book[1] = code
    #     #self.current_book[2] = ชื่อหนังสือ
    #     #self.current_book[3] = ผู้แต่ง
    #     #self.current_book[4] = เรื่องย่อ
    #     #self.current_book[5] = ราคา
    #     #self.current_book[6] = จำนวนหน้า
    #     #self.current_book[7] = หมวด
    #     #self.current_book[8] = ภาษา
    #     #self.current_book[9] = จำนวนสินค้า
    #     #self.current_book[10] = rating

    #     #Update Detail Entry
    #     self.name_detail_book_entry.delete(0,END)
    #     self.author_detail_book_entry.delete(0,END)
    #     self.category_detail_book_entry.delete(0,END)
    #     self.language_detail_book_entry.delete(0,END)
    #     self.price_detail_book_entry.delete(0,END)
    #     self.code_detail_book_entry.delete(0,END)
        
    #     self.name_detail_book_entry.insert(0,self.current_book[2])
    #     self.author_detail_book_entry.insert(0,self.current_book[3])
    #     self.category_detail_book_entry.insert(0,self.current_book[7])
    #     self.language_detail_book_entry.insert(0,self.current_book[8])
    #     self.price_detail_book_entry.insert(0,self.current_book[5])
    #     self.code_detail_book_entry.insert(0,self.current_book[1])
        

        
    def selected_categoryPages(self):
        self.inner_selected_categoryPages = Canvas(self.canvas, width=1000, height=550,bd=0, highlightthickness=0)
        # self.inner_selected_categoryPages.create_text(500, 275, font = 50, anchor=CENTER, text="selected_categoryPages")

    def categoryPage(self):
        self.inner_category = Canvas(self.canvas,width=1280, height=720,bd=0, highlightthickness=0)
        # self.inner_category.create_text(500, 275, font = 50, anchor=CENTER, text="categoryPage")


        ##Frame for book details
        self.detail_frame = ttk.LabelFrame(self.inner_category, text="Book Details")
        self.detail_frame.place(x=20, y=0,height=620, width=650)

        self.picbook_frame = ttk.LabelFrame(self.detail_frame, text="picbook_frame")
        self.picbook_frame.place(x=10, y=0,height=330, width=230)

        self.detail_data = ttk.LabelFrame(self.detail_frame, text="detail_data")
        self.detail_data.place(x=310, y=10,height=300, width=250)

        self.example_frame = ttk.LabelFrame(self.detail_frame, text="example_frame")
        self.example_frame.place(x=10, y=350,height=100, width=600)
        
        self.option_frame = ttk.LabelFrame(self.detail_frame, text="option_frame")
        self.option_frame.place(x=120, y=500,height=60, width=360)



        # Frame for book_TreeView
        frame1 = ttk.LabelFrame(self.inner_category, text="Excel Data")
        frame1.place(x=680, y=0, height=620, width=590)

       

        #Name Of Book
        # self.name_detail_book_entry.bind("<Key>", lambda e: "break")

        # lbl1 = Label(self.detail_frame, text="No")
        # lbl1.grid(row=0, column=0, padx=10, pady=5)
        # self.lbl1_entry = Entry(self.detail_frame, textvariable=self.No)
        # self.lbl1_entry.grid(row=0, column=1, padx=10, pady=5)


        #Author Of Book
        lbl2 = Label(self.detail_data, text="Code")
        lbl2.grid(row=0, column=1, padx=10, pady=5)
        self.lbl2_entry = Entry(self.detail_data, textvariable=self.Code)
        self.lbl2_entry.grid(row=0, column=2, padx=10, pady=5)


        #Category Of Book
        lbl3 = Label(self.detail_data, text="Name")
        lbl3.grid(row=1, column=1, padx=10, pady=5)
        self.lbl3_entry = Entry(self.detail_data, textvariable=self.Name)
        self.lbl3_entry.grid(row=1, column=2, padx=10, pady=5)

        #Language Of Book
        lbl4 = Label(self.detail_data, text="Author")
        lbl4.grid(row=3, column=1, padx=10, pady=5)
        self.lbl4_entry = Entry(self.detail_data, textvariable=self.Author)
        self.lbl4_entry.grid(row=3, column=2, padx=10, pady=5)

        #Price Of Book
        lbl5 = Label(self.detail_data, text="Category")
        lbl5.grid(row=4, column=1, padx=10, pady=5)
        self.lbl5_entry = Entry(self.detail_data, textvariable=self.Category)
        self.lbl5_entry.grid(row=4, column=2, padx=10, pady=5)

        #Code Of Book
        lbl6 = Label(self.detail_data, text="Price")
        lbl6.grid(row=5, column=1, padx=10, pady=5)
        self.lbl6_entry = Entry(self.detail_data, textvariable=self.Price)
        self.lbl6_entry.grid(row=5, column=2, padx=10, pady=5)

        # Rating Of Book
        lbl7 = Label(self.detail_data, text="Rating")
        lbl7.grid(row=6, column=1, padx=10, pady=5)
        self.lbl7_entry = Entry(self.detail_data, textvariable=self.Rating)
        self.lbl7_entry.grid(row=6, column=2, padx=10, pady=5)

        # Example Of Book
        self.commentbox = tk.Entry(self.example_frame, textvariable=self.Example, state="readonly")
        self.commentbox.place(x=10,y=0,width=550,height=70)
       

        ## number of items book
        self.spinboxvar = IntVar(self.option_frame)
        self.spinboxvar.set(1)
        self.items_book_spinbox = Spinbox(self.option_frame, from_=1, to=10,textvariable=self.spinboxvar ,state = 'readonly',width=7)
        Label(self.option_frame, text="").grid(row=7, column=0, padx=10, pady=5)
        self.items_book_spinbox.grid(row=7, column=1, padx=10, pady=5)

        add_favbook_button = Button(self.option_frame,text=' ♥ ', command=self.add_bookcart, width=15)
        add_favbook_button.grid(row=7, column=0, padx=10, pady=5)

        self.add_bookcart_button = Button(self.option_frame,text=' + ', command=self.add_bookcart,state=DISABLED,width=15)
        self.add_bookcart_button.grid(row=7, column=2, padx=10, pady=5)
   

        ##Book Image
        self.book_img_input = 'BookPics\\NOT_FOUND.png'
        self.book_img = ImageTk.PhotoImage(Image.open(self.book_img_input).resize((200, 300)))
        Label(self.picbook_frame, image=self.book_img).grid(row=0, column=0, padx=10, pady=5)
        self.list_img_book = os.listdir('BookPics')


        self.book_treeview = ttk.Treeview(frame1, column=(1,2,3,4,5,6), show="headings", height="20")

        self.book_treeview.place(x= 20, y=15)
        self.book_treeview.column(1, anchor='center', width=40)
        self.book_treeview.column(2, anchor='center', width=80)
        self.book_treeview.column(3, anchor='center', width=140)
        self.book_treeview.column(4, anchor='center', width=100)
        self.book_treeview.column(5, anchor='center', width=100)
        self.book_treeview.column(6, anchor='center', width=50)
        self.book_treeview.heading(1, text="No")
        self.book_treeview.heading(2, text="Code")
        self.book_treeview.heading(3, text="Name")
        self.book_treeview.heading(4, text="Author")
        self.book_treeview.heading(5, text="Category")
        self.book_treeview.heading(6, text="Price")
        

        # Book table
        for i in self.book_data:
            self.book_treeview.insert('', 'end', values = [i][0])
            # print(int(i[0]))



        # Click on table book data
        self.book_treeview.bind("<ButtonRelease-1>", self.lookupCustomer)


        yscrollbar = ttk.Scrollbar(frame1, orient="vertical", command=self.book_treeview.yview)
        xscrollbar = ttk.Scrollbar(frame1, orient="horizontal", command=self.book_treeview.xview)

        self.book_treeview.config(xscrollcommand=xscrollbar.set)
        self.book_treeview.config(yscrollcommand=yscrollbar.set)

        yscrollbar.pack(side="right", fill="y")
        xscrollbar.pack(side="bottom", fill="x")

    
    def lookupCustomer(self, event):
        curItem = self.book_treeview.focus()
        cur = self.book_treeview.item(curItem)['values']
        self.No.set(cur[0])
        self.Code.set(cur[1])
        self.Name.set(cur[2])
        self.Author.set(cur[3])
        self.Category.set(cur[4])
        self.Price.set(cur[5])
        self.Rating.set(cur[9])
        self.Example.set(cur[7])
        
        self.add_bookcart_button.config(state=NORMAL)
        if str(self.Code.get()) +'.png' in self.list_img_book:
            self.book_img_input = 'BookPics\\{}.png'.format(self.Code.get())
            self.book_img = ImageTk.PhotoImage(Image.open(self.book_img_input).resize((200, 300)))
            Label(self.picbook_frame, image=self.book_img).grid(row=0, column=0, padx=10, pady=5)
        else:
            self.book_img_input = 'BookPics\\NOT_FOUND.png'
            self.book_img = ImageTk.PhotoImage(Image.open(self.book_img_input).resize((200, 300)))
            Label(self.picbook_frame, image=self.book_img).grid(row=0, column=0, padx=10, pady=5)

    def add_bookcart(self):
        if self.usercart != []:
            for i in self.usercart:
                if i[0] == self.Code.get():
                    i[2] = str(int(i[2]) + int(self.items_book_spinbox.get()))
                    i[4] = str(float(i[2]) * float(i[3]))
                    print('UserCart :',self.usercart)
                    return
        self.usercart.append([self.Code.get(),self.Name.get(),str(self.items_book_spinbox.get()),self.Price.get(),self.Price.get()])
        print('UserCart :',self.usercart)
        self.spinboxvar.set(1)
    def delete_bookcart(self):
        # print('current :',self.current_bookcart)
        # print('usercart :',self.usercart)
        if self.current_bookcart in self.usercart:
            self.usercart.remove(self.current_bookcart)
        else:
            print('cart is empty')
        self.Del_botton.config(state=DISABLED)
        self.cart_treeview.delete(*self.cart_treeview.get_children())
        index = 1
        for i in self.usercart:
            self.cart_treeview.insert('', 'end', values=[index,i[0],i[1],i[2],i[3],i[4]])
            index += 1
    def lookupCart(self, event):
        curItem = self.cart_treeview.focus()
        cur = self.cart_treeview.item(curItem)['values']
        self.current_bookcart = []
        if cur != '':
            self.Del_botton.config(state=NORMAL)
            for i in cur[1:]:
                self.current_bookcart.append(str(i))

        

    def shift(self):
            x1,y1,x2,y2 = self.inner_payment_slidetext.bbox("marquee")
            if(x2<0 or y1<0): #reset the coordinates
                x1 = self.inner_payment_slidetext.winfo_width()
                y1 = self.inner_payment_slidetext.winfo_height()//2
                self.inner_payment_slidetext.coords("marquee",x1,y1)
            else:
                self.inner_payment_slidetext.move("marquee", -2, 0)
            self.inner_payment_slidetext.after(1000//self.fps,self.shift)
       
    def paymentPage(self):
        self.inner_payment = Canvas(self.canvas, width=1280, height=720)   
        self.inner_payment.create_text(500, 275, font = 50, anchor=CENTER, text="paymentPage")

        paymentPageFrame1 = tk.LabelFrame(self.inner_payment, text="Lo go JA JA")
        paymentPageFrame1.place(x=0, y=0, height=50, width=1280)
        
        ############# Main program ###############
        ##Text Slide
        text_var="______|   Welcome to the land of bookS   |______" 
        self.inner_payment_slidetext = Canvas(paymentPageFrame1, width=1000, height=100)   
        self.inner_payment_slidetext.create_text(0,-2000,text=text_var,font=('Times New Roman',20,'bold'),fill='black',tags=("marquee",),anchor='w')
        x1,y1,x2,y2 = self.inner_payment_slidetext.bbox("marquee")
        
        width = x2-x1
        # height = y2-y1
        self.inner_payment_slidetext['width']=width+500
        self.inner_payment_slidetext['height']=60
        self.fps=40    #Change the fps to make the animation faster/slower
        self.inner_payment_slidetext.pack()
        
        ##cart table
        paymentPageFrame2 = tk.LabelFrame(self.inner_payment, text="Table NA JAJAAJAJ")
        paymentPageFrame2.place(x=50, y=55, height=700, width=1180)

        self.cart_treeview = ttk.Treeview(paymentPageFrame2, column=(1,2,3,4,5,6), show="headings", height="18")
        yscrollbar = ttk.Scrollbar(paymentPageFrame2, orient="vertical", command=self.cart_treeview.yview)
        xscrollbar = ttk.Scrollbar(paymentPageFrame1, orient="horizontal", command=self.cart_treeview.xview)

        self.cart_treeview.config(xscrollcommand=xscrollbar.set)
        self.cart_treeview.config(yscrollcommand=yscrollbar.set)

        yscrollbar.pack(side="right", fill="y")
        xscrollbar.pack(side="bottom", fill="x")
        self.cart_treeview.pack()
        # self.cart_treeview.place(x=500,y=225,anchor=CENTER)
        self.cart_treeview.column(1, anchor='center', width=50)
        self.cart_treeview.column(2, anchor='center', width=100)
        self.cart_treeview.column(3, anchor='w', width=300)
        self.cart_treeview.column(4, anchor='center', width=100)
        self.cart_treeview.column(5, anchor='center', width=100)
        self.cart_treeview.column(6, anchor='center', width=100)
        self.cart_treeview.heading(1, text="no.")
        self.cart_treeview.heading(2, text="Code")
        self.cart_treeview.heading(3, text="Name")
        self.cart_treeview.heading(4, text="Item (s)")
        self.cart_treeview.heading(5, text="Price")
        self.cart_treeview.heading(6, text="Total amount")
        self.cart_treeview.bind("<ButtonRelease-1>", self.lookupCart)
        
        index = 1
        for i in self.usercart:
            self.cart_treeview.insert('', 'end', values=[index,i[0],i[1],i[2],i[3],i[4]])
            index += 1


        Back_bottom = tk.Button(paymentPageFrame2,text="< Back >", command = self.pp)    
        # Back_bottom.pack(side = BOTTOM,anchor='')
        Back_bottom.place(x=300, y=415,anchor="center")

        self.Del_botton = tk.Button(paymentPageFrame2,text="< Del >", command = self.delete_bookcart,state=DISABLED)
        # Del_bottom.pack(side = BOTTOM)    
        self.Del_botton.place(x=400, y=415,anchor="center")

        Next_bottom = tk.Button(paymentPageFrame2,text="< Next >", command = self.pp )
        Next_bottom.place(x=650, y=415,anchor="center")
        # Next_bottom.pack(side = BOTTOM) 

        Seemore_bottom = tk.Button(paymentPageFrame2,text="< See more >", command = self.pp )
        Seemore_bottom.place(x=550, y=415,anchor="center")
        # Seemore_bottom.pack(side = BOTTOM) 

        

        # Back_bottom = tk.Button(paymentPageFrame2,text="< Back >", command = self.pp)    
        # Back_bottom.place(x=500, y=400,anchor="center")

        # Back_bottom = tk.Button(paymentPageFrame2,text="< Back >", command = self.pp)    
        # Back_bottom.place(x=500, y=400,anchor="center")

        # Back_bottom = tk.Button(paymentPageFrame2,text="< Back >", command = self.pp)    
        # Back_bottom.place(x=500, y=400,anchor="center")



    def pp(self):
        print("OOPPPPPPPPPPPPPPPPPPPPPPPPPs")


    def deliveryPage(self):
        self.inner_delivery = Canvas(self.canvas, width=1280, height=720)   

        deliveryPageFrame1 = ttk.LabelFrame(self.inner_delivery, text="Status")
        deliveryPageFrame1.place(x=30, y=20, height=500, width=510)

        deliveryPageFrame2 = ttk.LabelFrame(self.inner_delivery, text="Review Book")
        deliveryPageFrame2.place(x=550, y=20, height=500, width=700)

        deliveryPageFrame2_1 = ttk.LabelFrame(deliveryPageFrame2, text="Picture")
        deliveryPageFrame2_1.place(x=50, y=10, height=200, width=150)

        deliveryPageFrame2_2 = ttk.LabelFrame(deliveryPageFrame2, text="Databook")
        deliveryPageFrame2_2.place(x=400, y=10, height=250, width=250)


        #Author Of Book
        lbl2 = Label(deliveryPageFrame2_2, text="Code")
        lbl2.grid(row=0, column=1, padx=10, pady=5)
        self.lbl2_entry = Entry(deliveryPageFrame2_2, textvariable=self.Code,state= "readonly")
        self.lbl2_entry.grid(row=0, column=2, padx=10, pady=10)


        #Category Of Book
        lbl3 = Label(deliveryPageFrame2_2, text="Name")
        lbl3.grid(row=1, column=1, padx=10, pady=5)
        self.lbl3_entry = Entry(deliveryPageFrame2_2, textvariable=self.Name,state= "readonly")
        self.lbl3_entry.grid(row=1, column=2, padx=10, pady=5)

        #Language Of Book
        lbl4 = Label(deliveryPageFrame2_2, text="Author")
        lbl4.grid(row=3, column=1, padx=10, pady=5)
        self.lbl4_entry = Entry(deliveryPageFrame2_2, textvariable=self.Author,state= "readonly")
        self.lbl4_entry.grid(row=3, column=2, padx=10, pady=5)

        #Price Of Book
        lbl5 = Label(deliveryPageFrame2_2, text="Category")
        lbl5.grid(row=4, column=1, padx=10, pady=5)
        self.lbl5_entry = Entry(deliveryPageFrame2_2, textvariable=self.Category,state= "readonly")
        self.lbl5_entry.grid(row=4, column=2, padx=10, pady=5)

        #Code Of Book
        lbl6 = Label(deliveryPageFrame2_2, text="Price")
        lbl6.grid(row=5, column=1, padx=10, pady=5)
        self.lbl6_entry = Entry(deliveryPageFrame2_2, textvariable=self.Price,state= "readonly")
        self.lbl6_entry.grid(row=5, column=2, padx=10, pady=5)

        # Rating Of Book
        lbl7 = Label(deliveryPageFrame2_2, text="Rating")
        lbl7.grid(row=6, column=1, padx=10, pady=5)
        listofRating = ["1","2","3","4","5"]
        self.Rating_Combobox = ttk.Combobox(deliveryPageFrame2_2,values=listofRating,width=18,state=DISABLED)
        self.Rating_Combobox.current(0)
        self.Rating_Combobox.grid(row=6, column=2, padx=10, pady=5)




        self.review_bottom = ttk.Button(deliveryPageFrame2,text="< Review >", command = self.review_bottomOn, state=DISABLED)    
        # self.review_bottom.place(x=500, y=400,anchor="center")
        self.review_bottom.pack(side = BOTTOM) 

        Back_bottom = ttk.Button(deliveryPageFrame1,text="< Back >", command = self.backk )    
        # Back_bottom.place(x=, y=400,anchor="center")
        Back_bottom.pack(side = LEFT) 

        Next_bottom = ttk.Button(deliveryPageFrame1,text="< Next >", command = self.checkDeliverySuccess)    
        # Next_bottom.place(x=500, y=400,anchor="center")
        Next_bottom.pack(side = RIGHT)



        commenttext = Label(deliveryPageFrame2,text="Comment : ", font=('TRACK', 12))
        commenttext.place(x=50,y=300)
        self.commentbox = tk.Text(deliveryPageFrame2,width=60,height=5, font=('TRACK', 8),state=DISABLED)
        self.commentbox.place(x=200,y=300)
       

        self.Comment_boutton1 = ttk.Button(deliveryPageFrame2,text="< Send >",command = self.printcomment, state=DISABLED)
        self.Comment_boutton1.place(x=300,y=400)
        self.Comment_boutton2 = ttk.Button(deliveryPageFrame2,text="< Clear >",command = self.clearcomment, state=DISABLED)
        self.Comment_boutton2.place(x=450,y=400)

    def printcomment(self):
        # self.commenttext2.config(text=self.commentbox.get(1.0,END))
        print(f"Rating is : {self.Rating_Combobox.get()}")
        print(self.commentbox.get(1.0,END),end ="")
    def clearcomment(self):
        self.commentbox.delete(1.0,END)
        print("<<< delete >>> ")


    def review_bottomOn(self):
        self.commentbox.config(state=NORMAL)
        self.review_bottom.config(state=NORMAL)
        self.Comment_boutton1.config(state=NORMAL)
        self.Comment_boutton2.config(state=NORMAL)
        self.Rating_Combobox.config(state=NORMAL)
        print("Review JAA")

    def backk(self):
        self.commentbox.config(state=DISABLED)
        self.review_bottom.config(state=DISABLED)
        self.Comment_boutton1.config(state=DISABLED)
        self.Comment_boutton2.config(state=DISABLED)
        self.Rating_Combobox.config(state=DISABLED)

    def show_HomePage(self): 
        self.delete_canvas()
        self.HomePage()
        self.canvas.create_window(0, 100, anchor=NW, window=self.inner_HomePage)  

    def checkDeliverySuccess(self):
        print("Checking...")
        print("Success...")
        self.review_bottomOn()

    def show_infomationPage(self): # ุปุ่ม 1
        self.delete_canvas()
        self.infomationPage()
        self.canvas.create_window(0, 100, anchor=NW, window=self.inner_infomation)

    def show_categoryPage(self):
        self.delete_canvas()
        self.canvas.create_window(0, 100, anchor=NW, window=self.inner_category)


    def show_paymentPage(self):
        self.delete_canvas()
        self.paymentPage()
        # self.shift()
        self.canvas.create_window(0,100, anchor=NW, window=self.inner_payment)


    def show_deliveryPage(self):
        self.delete_canvas()
        self.deliveryPage()
        self.canvas.create_window(0,100, anchor=NW, window=self.inner_delivery)
        
                
            

            
    # ลบหน้า info
    def delete_canvas(self): # ปุ่ม 2                #3
        # self.canvas.create_window(2000, 700, anchor=NW, window=self.inner_infomation)
        # self.canvas.create_window(2200,750, anchor=NW, window=self.inner_category)
        # self.canvas.create_window(2400,750, anchor=NW, window=self.inner_payment)
        # self.canvas.create_window(2600,750, anchor=NW, window=self.inner_delivery)
        # pass
        self.canvas.delete(ALL)
        self.create_background()
        # self.create_logo()
        # self.search_bar()
        self.button_state()
        




    ## 1. def ข้อมูลหน้านั้น -> ใส่ใน init
    ## 2. def แสดงข้อมูลหน้านัั้น -> ใส่ delete ก่อน
    ## 3. ใน def delete เอาหน้านั้นไปใส่



def showShopPage():
    run = Shop_main_screen()

if __name__ == '__main__':
    showShopPage()
