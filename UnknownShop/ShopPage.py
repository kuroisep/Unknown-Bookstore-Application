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

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Minor4810540114.",
    database="world",
    auth_plugin="mysql_native_password"
)
cursor = mydb.cursor()

options = []
# sql = "SELECT Code, Name FROM country"
sql = "SELECT * FROM city"
cursor.execute(sql)
ids = cursor.fetchall()
for i in ids:
    options.append(str(i[0]) + " - " + i[1])



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

        self.Name = StringVar()
        self.Author = StringVar()
        self.Category = StringVar()
        self.Language = StringVar()
        self.Price = StringVar()
        self.Code = StringVar()




        """ 
        THEAM
        """
        style = ttk.Style(self.shop_window)
        # Import the tcl file
        self.shop_window.tk.call('source', 'UnknownShop/azure.tcl')

        # Set the theme with the theme_use method
        style.theme_use('azure')
        style.configure('flat.TButton', borderwidth=0)
        style.configure("Treeview", font=('TRACK',13,'bold'))
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

        # #BOOK Variable
        # self.current_book = ['','','','','','','','','','','','','','','','','','','']
        #self.current_book[0] = ลำดับที่
        #self.current_book[1] = code
        #self.current_book[2] = ชื่อหนังสือ
        #self.current_book[3] = ผู้แต่ง
        #self.current_book[4] = เรื่องย่อ
        #self.current_book[5] = ราคา
        #self.current_book[6] = จำนวนหน้า
        #self.current_book[7] = หมวด
        #self.current_book[8] = ภาษา
        #self.current_book[9] = จำนวนสินค้า
        #self.current_book[10] = rating


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
        
    def shift(self):
        x1,y1,x2,y2 = canvas.bbox("marquee")
        if(x2<0 or y1<0): #reset the coordinates
            x1 = canvas.winfo_width()
            y1 = canvas.winfo_height()//2
            canvas.coords("marquee",x1,y1)
        else:
            canvas.move("marquee", -2, 0)
        canvas.after(1000//fps,shift)    

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
        
        if self.user != []:
            ## USERNAME
            self.inner_infomation.create_text(150, 50, anchor=NW, text='Username : {}'.format(self.user[0][1]))
            ## NAME
            self.inner_infomation.create_text(150, 100, anchor=NW, text='Name : ')
            self.name_entry = Entry(self.inner_infomation,font=('Verdana',15))
            self.name_entry.insert(0,self.user[0][3])
            self.name_entry.config(state=DISABLED)
            self.inner_infomation.create_window(210,80,window=self.name_entry,anchor = 'nw')
            ##LASTNAME
            self.inner_infomation.create_text(150, 150, anchor=NW, text='Lastname : ')
            self.lname_entry = Entry(self.inner_infomation)
            self.lname_entry.insert(0,self.user[0][4])
            self.lname_entry.config(state=DISABLED)
            self.inner_infomation.create_window(280,155,window=self.lname_entry)
            ##GENDER
            self.inner_infomation.create_text(150, 200, anchor=NW, text='Gender : ')
            self.gender_entry = Combobox(self.inner_infomation, width=8,value=['MALE','FEMALE']) 
            self.gender_entry.insert(0,self.user[0][5])
            self.gender_entry.config(state=DISABLED)
            self.inner_infomation.create_window(250,200,window=self.gender_entry)
            ##BIRTHDAY
                    #DATE
            self.inner_infomation.create_text(150, 250, anchor=NW, text='Birthday : ')
            self.birthday_date_entry = Combobox(self.inner_infomation, width=3,value=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
                                                                             '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', 
                                                                             '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']) 
            self.birthday_date_entry.insert(0,self.user[0][6].split('/')[0])
            self.birthday_date_entry.config(state=DISABLED)
            self.inner_infomation.create_window(240,255,window=self.birthday_date_entry)
                    #MONTH
            self.birthday_month_entry = Combobox(self.inner_infomation, width=5, value=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                                                                                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] )
            self.birthday_month_entry.insert(0,self.user[0][6].split('/')[1])
            self.birthday_month_entry.config(state=DISABLED)
            self.inner_infomation.create_window(300,255,window=self.birthday_month_entry)
                    #YEAR
            year_list = []
            for i in range(1920,2022):
                year_list.append(str(i))
            self.birthday_year_entry = Combobox(self.inner_infomation, width=5, value=year_list)
            self.birthday_year_entry.insert(0,self.user[0][6].split('/')[2])
            self.birthday_year_entry.config(state=DISABLED)
            self.inner_infomation.create_window(370,255,window=self.birthday_year_entry)
            ##EMAIL
            self.inner_infomation.create_text(150, 300, anchor=NW, text='Email : ')
            self.email_entry = Entry(self.inner_infomation)
            self.email_entry.insert(0,self.user[0][7])
            self.email_entry.config(state=DISABLED)
            self.inner_infomation.create_window(280,305,window=self.email_entry)
            ##PHONE
            self.inner_infomation.create_text(150, 350, anchor=NW, text='Telphone : ')
            self.telphone_entry = Entry(self.inner_infomation)
            self.telphone_entry.insert(0,self.user[0][8])
            self.telphone_entry.config(state=DISABLED)
            self.inner_infomation.create_window(280,355,window=self.telphone_entry)
            ##EDIT BUTTON
            self.edit_info_button = Button(self.inner_infomation,text='Edit', command=self.edit_infomation_state)
            self.inner_infomation.create_window(275, 450, window=self.edit_info_button, anchor="nw")
            ##DONE BUTTON
            self.done_info_button = Button(self.inner_infomation,text='Done',state=DISABLED, command=self.edit_infomation_state)
            self.inner_infomation.create_window(370, 450, window=self.done_info_button, anchor="nw")

            ##PICTURE
            image_path = "UnknownShop/Picture/ShopPage/USER_PIC/{}.png".format(self.user[0][9])
            self.user_img = ImageTk.PhotoImage(Image.open(image_path).resize((100, 100)))

            self.imageselect_info_button = Button(self.inner_infomation,text='select', command=self.openimage)
            self.inner_infomation.create_window(500, 300, window=self.imageselect_info_button, anchor="nw")
            self.inner_infomation.create_text(550, 180, anchor=NW, text='Picture : ')
            self.inner_infomation.create_image(550,200,image=self.user_img, anchor="nw")
            
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
        

        

    def categoryPage(self):
        self.inner_category = Canvas(self.canvas, width=1000, height=550,bd=0, highlightthickness=0)
        self.inner_category.create_text(500, 275, font = 50, anchor=CENTER, text="categoryPage")

        # Frame for TreeView
        frame1 = tk.LabelFrame(self.inner_category, text="Excel Data")
        frame1.place(x=480, y=20, height=500, width=500)

        ##Frame for book details
        detail_frame = tk.LabelFrame(self.inner_category, text="Book Details")
        detail_frame.place(x=50, y=20,height=500, width=400)

        #Name Of Book
        # name_detail_book = tk.Label(detail_frame,text='Name')
        # name_detail_book.place(x=200,y=20)
        # self.name_detail_book_entry = tk.Entry(detail_frame, textvariable=self.Name)
        # self.name_detail_book_entry.bind("<Key>", lambda e: "break")
        # self.name_detail_book_entry.place(x=200,y=40)

        lbl1 = Label(detail_frame, text="Name")
        lbl1.grid(row=0, column=0, padx=10, pady=5)
        self.lbl1_entry = Entry(detail_frame, textvariable=self.Name)
        self.lbl1_entry.grid(row=0, column=1, padx=10, pady=5)


        #Author Of Book
        lbl2 = Label(detail_frame, text="Author")
        lbl2.grid(row=1, column=0, padx=10, pady=5)
        self.lbl2_entry = Entry(detail_frame, textvariable=self.Author)
        self.lbl2_entry.grid(row=1, column=1, padx=10, pady=5)
        # author_detail_book = tk.Label(detail_frame,text='Author')
        # author_detail_book.place(x=200,y=70)
        # self.author_detail_book_entry = tk.Entry(detail_frame, textvariable=self.Author)
        # self.author_detail_book_entry.bind("<Key>", lambda e: "break")
        # self.author_detail_book_entry.place(x=200,y=90)

        #Category Of Book
        lbl3 = Label(detail_frame, text="Category")
        lbl3.grid(row=2, column=0, padx=10, pady=5)
        self.lbl3_entry = Entry(detail_frame, textvariable=self.Category)
        self.lbl3_entry.grid(row=2, column=1, padx=10, pady=5)
        # category_detail_book = tk.Label(detail_frame,text='Category')
        # category_detail_book.place(x=200,y=120)
        # self.category_detail_book_entry = tk.Entry(detail_frame, textvariable=self.Category)
        # self.category_detail_book_entry.bind("<Key>", lambda e: "break")
        # self.category_detail_book_entry.place(x=200,y=140)

        #Language Of Book
        lbl4 = Label(detail_frame, text="Language")
        lbl4.grid(row=3, column=0, padx=10, pady=5)
        self.lbl4_entry = Entry(detail_frame, textvariable=self.Language)
        self.lbl4_entry.grid(row=3, column=1, padx=10, pady=5)
        # language_detail_book = tk.Label(detail_frame,text='Language')
        # language_detail_book.place(x=200,y=170)
        # self.language_detail_book_entry = tk.Entry(detail_frame, textvariable=self.Language)
        # self.language_detail_book_entry.bind("<Key>", lambda e: "break")
        # self.language_detail_book_entry.place(x=200,y=190)

        #Price Of Book
        lbl5 = Label(detail_frame, text="Price")
        lbl5.grid(row=4, column=0, padx=10, pady=5)
        self.lbl5_entry = Entry(detail_frame, textvariable=self.Price)
        self.lbl5_entry.grid(row=4, column=1, padx=10, pady=5)
        # price_detail_book = tk.Label(detail_frame,text='Price')
        # price_detail_book.place(x=200,y=220)
        # self.price_detail_book_entry = tk.Entry(detail_frame, textvariable=self.Price)
        # self.price_detail_book_entry.bind("<Key>", lambda e: "break")
        # self.price_detail_book_entry.place(x=200,y=240)

        #Code Of Book
        lbl6 = Label(detail_frame, text="Code")
        lbl6.grid(row=5, column=0, padx=10, pady=5)
        self.lbl6_entry = Entry(detail_frame, textvariable=self.Code)
        self.lbl6_entry.grid(row=5, column=1, padx=10, pady=5)
        # code_detail_book = tk.Label(detail_frame,text='Code')
        # code_detail_book.place(x=200,y=270)
        # self.code_detail_book_entry = tk.Entry(detail_frame, textvariable=self.Code)
        # self.code_detail_book_entry.bind("<Key>", lambda e: "break")
        # self.code_detail_book_entry.place(x=200,y=290)

        # button2 = ttk.Button(detail_frame, text="< Load File >", command=lambda: Load_excel_data())
        # button2.place(x=200, y=400)

        self.treeview = ttk.Treeview(frame1, column=(1,2,3,4,5,6), show="headings", height="22")
        self.treeview.pack()

        self.treeview.pack(side=LEFT)
        self.treeview.place(x=0, y=0)
        self.treeview.heading(1, text="Name")
        self.treeview.heading(2, text="Author")
        self.treeview.heading(3, text="Category")
        self.treeview.heading(4, text="Language")
        self.treeview.heading(5, text="Price")
        self.treeview.heading(6, text="Code")


        self.treeview.bind("<ButtonRelease-1>", self.lookupCustomer)


        yscrollbar = ttk.Scrollbar(frame1, orient="vertical", command=self.treeview.yview)
        xscrollbar = ttk.Scrollbar(frame1, orient="horizontal", command=self.treeview.xview)

        self.treeview.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)

        yscrollbar.pack(side="right", fill="y")
        xscrollbar.pack(side="bottom", fill="x")


        self.update(ids)



        # ## Treeview Widget
        # self.tv1 = ttk.Treeview(frame1)
        # # self.tv1 = CustomTreeview(tv)
        # self.tv1.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).
   
        # self.tv1.bind('<ButtonRelease-1>', self.selectItem)



        # treescrolly = tk.Scrollbar(frame1, orient="vertical", command=self.tv1.yview) # command means update the yaxis view of the widget
        # treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=self.tv1.xview) # command means update the xaxis view of the widget
        # self.tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
        # treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
        # treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget


        # def Load_excel_data():
        #     df = pd.read_csv("UnknownShop\DataBookList.csv",engine='python')
        #     # print(df)
        #     # print(str(self.current_book[2]))

        #     clear_data()
        #     self.tv1["column"] = list(df.columns)
        #     self.tv1["show"] = "headings"
        #     for column in self.tv1["columns"]:
        #         self.tv1.heading(column, text=column ) # let the column heading = column name

        #     df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
            
        #     for row in df_rows:
        #         self.tv1.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
        #     return None

            


    #     def clear_data():
    #         self.tv1.delete(*self.tv1.get_children())
    #         return None

    
    def lookupCustomer(self, event):
        curItem = self.treeview.focus()
        cur = self.treeview.item(curItem)['values']
        self.Name.set(cur[0])
        self.Author.set(cur[1])
        self.Category.set(cur[2])
        self.Language.set(cur[3])
        self.Price.set(cur[4])
        # self.Code.set(cur[5])

    def update(self, ids):
        self.treeview.delete(*self.treeview.get_children())
        for i in ids:
            self.treeview.insert('', 'end', values=i)

       
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
