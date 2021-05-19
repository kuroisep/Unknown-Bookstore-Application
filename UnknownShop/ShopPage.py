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

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Minor4810540114.",
    database="new_book",
    auth_plugin="mysql_native_password"
)
cursor = mydb.cursor()

options = []
# sql = "SELECT Code, Name FROM country"
sql = "SELECT * FROM books"
cursor.execute(sql)
ids = cursor.fetchall()
for i in ids:
    options.append(str(i[0]) + " - " + i[1])


print(ids)


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


        # Variable User
        self.No = StringVar()
        self.Name = StringVar()
        self.Author = StringVar()
        self.Category = StringVar()
        self.Language = StringVar()
        self.Price = StringVar()
        self.Code = StringVar()
        self.Rating = StringVar()

        """ 
        THEAM
        """
        style = ttk.Style(self.shop_window)
        # Import the tcl file
        self.shop_window.tk.call('source', 'UnknownShop/azure.tcl')

        # Set the theme with the theme_use method
        style.theme_use('azure')
        style.configure('flat.TButton', borderwidth=0)
        # style.configure("Treeview", font=('TRACK',13,'bold'))
        """ 
        THEAM
        """

        #USER LOGIN
        self.df = pandas.read_csv('login.csv')
        self.user = self.df.loc[self.df['STATUS']=='T'].values.tolist()
        self.imagefile = ''
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
        self.create_logo()
        self.search_bar()
        # self.shift()
        self.set_banner()  ## <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        self.count = 0
        self.shift()

        self.moveBanner()  ## <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        self.button_state()

        self.shop_window.resizable(0, 0)
        self.shop_window.overrideredirect(0)
        self.shop_window.mainloop()

    def create_background(self):
        bg_path = "UnknownShop\Picture\Draf BG.png" 
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
        

    def search(self):
        q2 = self.Name.get()
        query = "SELECT id, name, countrycode, district, population FROM city WHERE name LIKE '%"+q2+"%'"
        cursor.execute(query)
        rows = cursor.fetchall()
        self.update(rows)


    def clear(self):
        query = "SELECT id, name, countrycode, district, population FROM city"
        cursor.execute(query)
        rows = cursor.fetchall()
        self.update(rows)


    def search_bar(self): 
        self.canvas.create_text(385, 65, text="Search By", font=('TRACK', 12))

        # name = tk.StringVar()
        nameEntered = ttk.Entry(self.shop_window, width = 60, textvariable = self.Name)
        nameEntered.place(x=440, y=50)

        # drop = ttk.Combobox(self.shop_window, width=10, value=["All", "English Books", "Thai Books"])
        # drop.current((0))
        # drop.place(x=440, y=50)

        search_button = ttk.Button(self.shop_window, text = "Search", command=self.search)
        search_button.place(x=820, y=50)

        show_all_books_button = ttk.Button(self.shop_window, text = "Clear", command=self.clear)
        show_all_books_button.place(x=908, y=50)
        

    def value_set_one(self):
        self.value = 1

    def print_value(self):
        print(self.value)
        
    def button_state(self):

        button1_path = "UnknownShop\Picture\ShopPage\\button1.png"
        self.img_button1 = ImageTk.PhotoImage(Image.open(button1_path).resize((175, 48)))
        # self.canvas.create_image(200,200,image=self.img_button1)
        self.button1 = tk.Button(self.shop_window,image=self.img_button1, command = self.show_infomationPage, borderwidth=0)
        
        self.canvas.create_window(0, 200, window=self.button1, anchor="nw")

        button2_path = "UnknownShop\Picture\ShopPage\\button2.png"
        self.img_button2 = ImageTk.PhotoImage(Image.open(button2_path).resize((175, 48)))
        # self.canvas.create_image(200,300,image=self.img_button2)
        self.button2 = tk.Button(image=self.img_button2,command= self.show_categoryPage, borderwidth=0, )
        self.canvas.create_window(0, 280, window=self.button2, anchor="nw")

        button3_path = "UnknownShop\Picture\ShopPage\\button3.png"
        self.img_button3 = ImageTk.PhotoImage(Image.open(button3_path).resize((175, 48)))
        # self.canvas.create_image(200,400,image=self.img_button3)
        self.button3 = tk.Button(image=self.img_button3,command=self.show_paymentPage, borderwidth=0)
        self.canvas.create_window(0, 360, window=self.button3, anchor="nw")

        button4_path = "UnknownShop\Picture\ShopPage\\button4.png"
        self.img_button4 = ImageTk.PhotoImage(Image.open(button4_path).resize((175, 48)))
        # self.canvas.create_image(200,500,image=self.img_button4)
        self.button4 = tk.Button(image=self.img_button4,command=self.show_deliveryPage, borderwidth=0, 
                                relief=FLAT, bg="#856fff",activebackground='#4444ff')
        self.canvas.create_window(0, 440, window=self.button4, anchor="nw")

        button5_path = "UnknownShop\Picture\ShopPage\\button5.png"
        self.img_button5 = ImageTk.PhotoImage(Image.open(button5_path).resize((175, 48)))
        # self.canvas.create_image(200,600,image=self.img_button5)
        self.button5 = tk.Button(self.shop_window, image=self.img_button5, command=self.delete_canvas, border=0,
                                relief=FLAT, bg="#856fff",activebackground='#4444ff')
        self.canvas.create_window(0, 520, window=self.button5, anchor="nw")
       

        button6_path = "UnknownShop\Picture\ShopPage\\button5.png"
        self.img_button6 = ImageTk.PhotoImage(Image.open(button6_path).resize((175, 48)))
        # self.canvas.create_image(200,600,image=self.img_button6)
        self.button6 = tk.Button(self.shop_window, image=self.img_button6, command=self.delete_show_window, border=0,
                                relief=FLAT, bg="#856fff",activebackground='#4444ff')
        self.canvas.create_window(0, 600, window=self.button6, anchor="nw")
    

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

    
    def infomationPage(self): # ข้อมูลหน้า info       #1
        self.inner_infomation = Canvas(self.canvas, width=1000, height=550)
        
        infomationPageFrame1 = tk.LabelFrame(self.inner_infomation , text="INFOMATION")
        infomationPageFrame1.place(x=0, y=0, height=550, width=500)

        infomationPageFrame2 = tk.LabelFrame(self.inner_infomation , text="PICTURE")
        infomationPageFrame2.place(x=500, y=0, height=400, width=500)


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

            self.imageselect_info_button = Button(infomationPageFrame2,text='select',state=DISABLED, command=self.openimage)
            self.imageselect_info_button.pack(side="bottom")
            user_image = Label(infomationPageFrame2, image=self.user_img)
            user_image.pack()
            
    def openfn(self):
        self.imagefile = filedialog.askopenfilename(initialdir='UnknownShop\\Picture\\ShopPage\\USER_PIC',title='open')
        return self.imagefile
    def openimage(self):
        self.x = self.openfn()
        self.user_img = ImageTk.PhotoImage(Image.open(self.x).resize((100, 100)))
        self.inner_infomation.create_image(550,200,image=self.user_img, anchor="nw")
        # self.user_img = self.user_img.resize((100, 150), Image.ANTIALIAS)
        # self.user_img = ImageTk.PhotoImage(self.user_img)
        

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
                temp_img = cv2.imread(self.x)
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
        self.inner_selected_categoryPages.create_text(500, 275, font = 50, anchor=CENTER, text="selected_categoryPages")

    def categoryPage(self):
        self.inner_category = Canvas(self.canvas, width=1000, height=550,bd=0, highlightthickness=0)
        self.inner_category.create_text(500, 275, font = 50, anchor=CENTER, text="categoryPage")


        ##Frame for book details
        detail_frame = ttk.LabelFrame(self.inner_category, text="Book Details")
        detail_frame.place(x=0, y=20,height=500, width=400)

        # Frame for book_TreeView
        frame1 = ttk.LabelFrame(self.inner_category, text="Excel Data")
        frame1.place(x=410, y=20, height=500, width=590)

       

        #Name Of Book
        # self.name_detail_book_entry.bind("<Key>", lambda e: "break")

        lbl1 = Label(detail_frame, text="No")
        lbl1.grid(row=0, column=0, padx=10, pady=5)
        self.lbl1_entry = Entry(detail_frame, textvariable=self.No)
        self.lbl1_entry.grid(row=0, column=1, padx=10, pady=5)


        #Author Of Book
        lbl2 = Label(detail_frame, text="Code")
        lbl2.grid(row=1, column=0, padx=10, pady=5)
        self.lbl2_entry = Entry(detail_frame, textvariable=self.Code)
        self.lbl2_entry.grid(row=1, column=1, padx=10, pady=5)


        #Category Of Book
        lbl3 = Label(detail_frame, text="Name")
        lbl3.grid(row=2, column=0, padx=10, pady=5)
        self.lbl3_entry = Entry(detail_frame, textvariable=self.Name)
        self.lbl3_entry.grid(row=2, column=1, padx=10, pady=5)

        #Language Of Book
        lbl4 = Label(detail_frame, text="Author")
        lbl4.grid(row=3, column=0, padx=10, pady=5)
        self.lbl4_entry = Entry(detail_frame, textvariable=self.Author)
        self.lbl4_entry.grid(row=3, column=1, padx=10, pady=5)

        #Price Of Book
        lbl5 = Label(detail_frame, text="Category")
        lbl5.grid(row=4, column=0, padx=10, pady=5)
        self.lbl5_entry = Entry(detail_frame, textvariable=self.Category)
        self.lbl5_entry.grid(row=4, column=1, padx=10, pady=5)

        #Code Of Book
        lbl6 = Label(detail_frame, text="Price")
        lbl6.grid(row=5, column=0, padx=10, pady=5)
        self.lbl6_entry = Entry(detail_frame, textvariable=self.Price)
        self.lbl6_entry.grid(row=5, column=1, padx=10, pady=5)


        # Rating Of Book
        lbl7 = Label(detail_frame, text="Rating")
        lbl7.grid(row=6, column=0, padx=10, pady=5)
        self.lbl7_entry = Entry(detail_frame, textvariable=self.Rating)
        self.lbl7_entry.grid(row=6, column=1, padx=10, pady=5)

        self.book_treeview = ttk.Treeview(frame1, column=(1,2,3,4,5,6), show="headings", height="20")

        self.book_treeview.place(x= 80, y=15)
        self.book_treeview.column(1, anchor='w', width=50)
        self.book_treeview.column(2, anchor='w', width=100)
        self.book_treeview.column(3, anchor='w', width=50)
        self.book_treeview.column(4, anchor='w', width=50)
        self.book_treeview.column(5, anchor='w', width=50)
        self.book_treeview.column(6, anchor='w', width=100)
        self.book_treeview.heading(1, text="No")
        self.book_treeview.heading(2, text="Code")
        self.book_treeview.heading(3, text="Name")
        self.book_treeview.heading(4, text="Author")
        self.book_treeview.heading(5, text="Category")
        self.book_treeview.heading(6, text="Price")
        

        # Click on table book data
        self.book_treeview.bind("<ButtonRelease-1>", self.lookupCustomer)


        yscrollbar = ttk.Scrollbar(frame1, orient="vertical", command=self.book_treeview.yview)
        xscrollbar = ttk.Scrollbar(frame1, orient="horizontal", command=self.book_treeview.xview)

        self.book_treeview.config(xscrollcommand=xscrollbar.set)
        self.book_treeview.config(yscrollcommand=yscrollbar.set)

        yscrollbar.pack(side="right", fill="y")
        xscrollbar.pack(side="bottom", fill="x")




        self.update(ids)
    
    def lookupCustomer(self, event):
        curItem = self.book_treeview.focus()
        cur = self.book_treeview.item(curItem)['values']
        self.No.set(cur[0])
        self.Code.set(cur[1])
        self.Name.set(cur[3])
        self.Author.set(cur[4])
        self.Category.set(cur[8])
        self.Price.set(cur[6])

    def update(self, ids):
        self.book_treeview.delete(*self.book_treeview.get_children())
        for i in ids:
            self.book_treeview.insert('', 'end', values=i)

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
        self.inner_payment = Canvas(self.canvas, width=1000, height=550)   
        self.inner_payment.create_text(500, 275, font = 50, anchor=CENTER, text="paymentPage")

        paymentPageFrame1 = tk.LabelFrame(self.inner_payment, text="Lo go JA JA")
        paymentPageFrame1.place(x=0, y=0, height=100, width=1000)
        
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
        paymentPageFrame2.place(x=0, y=100, height=450, width=1000)

        self.cart_treeview = ttk.Treeview(paymentPageFrame2, column=(1,2,3,4,5), show="headings", height="18")
        yscrollbar = ttk.Scrollbar(paymentPageFrame2, orient="vertical", command=self.cart_treeview.yview)
        xscrollbar = ttk.Scrollbar(paymentPageFrame1, orient="horizontal", command=self.cart_treeview.xview)

        self.cart_treeview.config(xscrollcommand=xscrollbar.set)
        self.cart_treeview.config(yscrollcommand=yscrollbar.set)

        yscrollbar.pack(side="right", fill="y")
        xscrollbar.pack(side="bottom", fill="x")
        self.cart_treeview.pack()
        # self.cart_treeview.place(x=500,y=225,anchor=CENTER)
        self.cart_treeview.column(1, anchor='w', width=50)
        self.cart_treeview.column(2, anchor='w', width=50)
        self.cart_treeview.column(3, anchor='w', width=200)
        self.cart_treeview.column(4, anchor='w', width=100)
        self.cart_treeview.column(5, anchor='w', width=100)
        self.cart_treeview.heading(1, text="no.")
        self.cart_treeview.heading(2, text="Code")
        self.cart_treeview.heading(3, text="Name")
        self.cart_treeview.heading(4, text="Item (s)")
        self.cart_treeview.heading(5, text="Price")
        for i in range(0,100):
            self.cart_treeview.insert('', 'end', values=[i,'code','SAASASAS_ '+ str(i) ,"55555","159.50"])



        Back_bottom = tk.Button(paymentPageFrame2,text="< Back >", command = self.pp)    
        # Back_bottom.pack(side = BOTTOM,anchor='')
        Back_bottom.place(x=300, y=415,anchor="center")

        Del_bottom = tk.Button(paymentPageFrame2,text="< Del >", command = self.pp )
        # Del_bottom.pack(side = BOTTOM)    
        Del_bottom.place(x=400, y=415,anchor="center")

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
        self.inner_delivery = Canvas(self.canvas, width=1000, height=550)   
        self.inner_delivery.create_text(500, 275, font = 50, anchor=CENTER, text="deliveryPage")

        deliveryPageFrame1 = ttk.LabelFrame(self.inner_delivery, text="Status")
        deliveryPageFrame1.place(x=0, y=0, height=500, width=300)

        deliveryPageFrame2 = ttk.LabelFrame(self.inner_delivery, text="Review Book")
        deliveryPageFrame2.place(x=300, y=0, height=500, width=700)

        deliveryPageFrame2_1 = ttk.LabelFrame(deliveryPageFrame2, text="Picture")
        deliveryPageFrame2_1.place(x=275, y=10, height=150, width=150)


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
        commenttext.place(x=50,y=200)
        self.commentbox = tk.Text(deliveryPageFrame2,width=60,height=5, font=('TRACK', 8),state=DISABLED)
        self.commentbox.place(x=200,y=200)
       
        Comboboxtext = Label(deliveryPageFrame2,text="Rating : ", font=('TRACK', 12))
        Comboboxtext.place(x=50,y=300)
        listofRating = ["1","2","3","4","5"]
        self.Rating_Combobox = ttk.Combobox(deliveryPageFrame2,values=listofRating,width=10,state=DISABLED)
        self.Rating_Combobox.current(0)
        self.Rating_Combobox.place(x=200,y=300)

        self.Comment_boutton1 = ttk.Button(deliveryPageFrame2,text="< Send >",command = self.printcomment, state=DISABLED)
        self.Comment_boutton1.place(x=300,y=370)
        self.Comment_boutton2 = ttk.Button(deliveryPageFrame2,text="< Clear >",command = self.clearcomment, state=DISABLED)
        self.Comment_boutton2.place(x=450,y=370)

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
        
    def checkDeliverySuccess(self):
        print("Checking...")
        print("Success...")
        self.review_bottomOn()

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
