import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import font as tkFont
import pandas
from PIL import ImageTk, Image
import re
import os
import csv

import tkinter as tk
# from tkinter import ttk
# from tkinter.ttk import *


class main_account_screen:

    def __init__(self):
        self.main_screen = Tk()
        self.myfont = 'TRACK'

        icon_path = "MAIN\Picture\LoginPage\open-book.png"
        icon = PhotoImage(file=icon_path)
        self.main_screen.iconphoto(False, icon)

        x = (960) - (1280/2)
        y = (540) - (720/2)
        self.main_screen.geometry("1280x720+%d+%d" % (x, y))
        self.main_screen.title("Account Login")

        bg_path = "MAIN\Picture\LoginPage\LOGIN.png"
        bg = ImageTk.PhotoImage(Image.open(bg_path).resize((1280, 720)))

        # Create Canvas
        canvas = Canvas(self.main_screen, width=1280, height=720)

        canvas.pack(fill="both", expand=True)

        # Display image
        canvas.create_image(0, 0, image=bg,
                            anchor="nw")

        global username_verify
        global password_verify

        username_verify = StringVar()
        password_verify = StringVar()

        global username_login_entry
        global password_login_entry

        img_logo_path = "MAIN\Picture\LoginPage\logo.png"
        img_logo = ImageTk.PhotoImage(Image.open(img_logo_path).resize((200, 200)))
        canvas.create_image(200, 150, image=img_logo, anchor="nw")

        canvas.create_text(280, 350, text="Welcome", font=(self.myfont, 60), anchor="n")
        canvas.create_text(320, 430, text="To the land of books",
                        font=(self.myfont, 20), anchor="n")

        canvas.create_text(1000, 170, text="Signin", font=(self.myfont, 40))

        canvas.create_text(875, 250, text="Username", font=(self.myfont))
        username_login_entry = Entry(
            textvariable=username_verify, width=30, font=20)
        # username_login_entry.config(fg = 'blue')
        canvas.create_window(1000, 290, window=username_login_entry)

        canvas.create_text(875, 340, text="Password", font=self.myfont)
        password_login_entry = Entry(
            textvariable=password_verify, show='●', width=30, font=20)
        canvas.create_window(1000, 380, window=password_login_entry)

        img_login_path = "MAIN\Picture\LoginPage\login-button1.png"
        img_login_button = ImageTk.PhotoImage(
            Image.open(img_login_path).resize((200, 300)))
        login_button = Button(image=img_login_button, command=self.login_verify,
                            bd=0, highlightthickness=0, width=140, height=60)
        canvas.create_window(900, 450, window=login_button)

        img_regis_path = "MAIN\Picture\LoginPage\\regis-button.png"
        img_regis_button = ImageTk.PhotoImage(
            Image.open(img_regis_path).resize((170, 80)))
        regis_button = Button(image=img_regis_button, width=140, height=60,
                            command=self.register, highlightthickness=0, borderwidth=0)
        canvas.create_window(1100, 450, window=regis_button)

        canvas.create_text(1230, 700, text="V.1.0.0", font=self.myfont)

        exit_button = Button(text="EXIT", command=self.delete_main_screen,
                            bd=0, highlightthickness=0, width=20, height=3)
        canvas.create_window(1100, 600, window=exit_button)


        self.main_screen.resizable(0, 0)
        self.main_screen.overrideredirect(0)
        self.main_screen.mainloop()

    def login_verify(self):
        self.username1 = username_verify.get()
        self.password1 = password_verify.get()
        df = pandas.read_csv('login.csv')
        data = df.set_index('USER').T.to_dict('list')
        if data.get(self.username1) != None:
            if str(data.get(self.username1)[0]) == str(self.password1):
                self.info_NAME = data.get(self.username1)[1]
                self.info_LNAME = data.get(self.username1)[2]
                self.info_GENDER = data.get(self.username1)[3]
                self.info_EMAIL = data.get(self.username1)[4]
                self.info_telphone = data.get(self.username1)[5]
                username_login_entry.delete(0, END)
                password_login_entry.delete(0, END)
                self.login_sucess()
            else:
                self.password_not_recognised()
                password_login_entry.delete(0, END)
        else:
            self.user_not_found()
            username_login_entry.delete(0, END)
            password_login_entry.delete(0, END)


    def login_sucess(self):
        self.login_success_screen = Toplevel(self.main_screen)
        self.login_success_screen.title("Login Success")
        x = (960) - (400/2)
        y = (540) - (300/2)
        self.login_success_screen.geometry("400x300+%d+%d" % (x, y))
        canvas = Canvas(self.login_success_screen, width=400, height=300)
        canvas.pack(fill="both", expand=True)

        if self.info_GENDER == 'MALE':
            sex = 'Mr.'
        else:
            sex = 'Mrs.'

        canvas.create_text(200, 100, text="WELCOME  {} {}  {}".format(
            sex, self.info_NAME, self.info_LNAME))
        canvas.create_text(200, 130, text="Email : {}   Phone Number : {} ".format(
            self.info_EMAIL, self.info_telphone))
        ok_button = Button(self.login_success_screen, text="OK",
                        command=self.delete_login_success)
        canvas.create_window(200, 200, window=ok_button)

    def delete_login_success(self):
        self.login_success_screen.destroy()
        self.delete_main_screen()

    def delete_password_not_recognised(self):
        self.password_not_recog_screen.destroy()

    def delete_user_not_found_screen(self):
        self.user_not_found_screen.destroy()

    def delete_register_screen(self):
        self.register_screen.destroy()

    def delete_main_screen(self):
        self.main_screen.destroy()


    def password_not_recognised(self):
        self.password_not_recog_screen = Toplevel(self.main_screen)
        self.password_not_recog_screen.title("Error")
        x = (960) - (400/2)
        y = (540) - (300/2)
        self.password_not_recog_screen.geometry("400x300+%d+%d" % (x, y))
        canvas = Canvas(self.password_not_recog_screen, width=400, height=300)
        canvas.pack(fill="both", expand=True)

        canvas.create_text(200, 100, text="Incorrect Password")
        ok_button = Button(self.password_not_recog_screen, text="OK",
                        command=self.delete_password_not_recognised)
        canvas.create_window(200, 150, window=ok_button)

    
    def user_not_found(self):
        self.user_not_found_screen = Toplevel(self.main_screen)
        self.user_not_found_screen.title("Error")
        x = (960) - (400/2)
        y = (540) - (300/2)
        self.user_not_found_screen.geometry("400x300+%d+%d" % (x, y))
        canvas = Canvas(self.user_not_found_screen, width=400, height=300)
        canvas.pack(fill="both", expand=True)

        canvas.create_text(200, 100, text="User Not Found")
        ok_button = Button(self.user_not_found_screen, text="OK",
                        command=self.delete_user_not_found_screen)
        canvas.create_window(200, 150, window=ok_button)


    def register(self):
        self.register_screen = Toplevel(self.main_screen)
        self.register_screen.title("Register")
        self.register_screen.focus_set()
        self.register_screen.grab_set()
        self.register_screen.resizable(0, 0)

        x = (960) - (750/2)
        y = (540) - (650/2)
        self.register_screen.geometry("750x600+%d+%d" % (x, y))

        regis_bg_path = "MAIN\Picture\LoginPage\REGISTER.png"
        self.regis_bg = ImageTk.PhotoImage(Image.open(regis_bg_path).resize((750, 600)))

        canvas = Canvas(self.register_screen, width=750, height=600)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.regis_bg, anchor="nw")

        self.username = StringVar()
        self.password = StringVar()
        self.confpassword = StringVar()
        self.name = StringVar()
        self.lastname = StringVar()
        self.email = StringVar()
        self.gender1 = IntVar()
        self.gender2 = IntVar()
        self.gender_choice1 = IntVar(self.register_screen)
        self.gender_choice2 = IntVar(self.register_screen)
        self.telphone = StringVar()

        canvas.create_text(375, 60, text="Please enter details below", font=self.myfont)

        canvas.create_text(65, 150, text="Username *", font=self.myfont)
        self.username_entry = Entry(self.register_screen, textvariable=self.username)
        canvas.create_window(115, 175, window=self.username_entry, width=180)

        self.password_entry = Entry(self.register_screen, textvariable=self.password, show='●')
        canvas.create_text(290, 150, text="Password *", font=self.myfont)
        canvas.create_window(400, 175, window=self.password_entry, width=180)

        self.confpassword_entry = Entry(self.register_screen, textvariable=self.confpassword, show='●')
        canvas.create_text(580, 150, text="Confirm Password *", font=self.myfont)
        canvas.create_window(610, 175, window=self.confpassword_entry, width=180)

        self.name_entry = Entry(self.register_screen, textvariable=self.name)
        canvas.create_text(50, 225, text="Name *", font=self.myfont)
        canvas.create_window(115, 250, window=self.name_entry, width=180)

        self.lastname_entry = Entry(self.register_screen, textvariable=self.lastname)
        canvas.create_text(292, 225, text="Last Name *", font=self.myfont)
        canvas.create_window(340, 250, window=self.lastname_entry, width=180)

        canvas.create_text(600, 225, text="Gender *", font=self.myfont)

        self.gender_choice1 = Checkbutton(self.register_screen, text="Male", font=(
            self.myfont, 12), command=self.my_upd, variable=self.gender1)
        self.gender_choice2 = Checkbutton(self.register_screen, text="Female", font=(
            self.myfont, 12), command=self.my_upd, variable=self.gender2)

        canvas.create_window(550, 250, window=self.gender_choice1)
        canvas.create_window(650, 250, window=self.gender_choice2)

        canvas.create_text(85, 310, text="Email Address * ", font=self.myfont)
        self.email_entry = Entry(self.register_screen, textvariable=self.email)
        canvas.create_window(150, 335, window=self.email_entry, width=250)

        canvas.create_text(410, 310, text="Phone Number * ", font=self.myfont)
        self.telphone_entry = Entry(self.register_screen, textvariable=self.telphone)
        canvas.create_window(470, 335, window=self.telphone_entry, width=250)

        helv20 = tkFont.Font(family='Helvetica', size=20, weight=tkFont.BOLD)
        regis_button = Button(self.register_screen, text="Register",
                            font=helv20, bg="blue", fg="white", command=self.register_user)
        canvas.create_window(400, 420, window=regis_button)
        clear_button = Button(self.register_screen, text="Clear",
                            font=helv20, bg="blue", fg="white", command=self.clear_user)
        canvas.create_window(600, 420, window=clear_button)

        cancel_button = Button(self.register_screen, text="CANCEL", command=self.delete_register_screen,
                            bd=0, highlightthickness=0, width=20, height=3)
        canvas.create_window(600, 500, window=cancel_button)


    def my_upd(self):
        i = 0
        if(self.gender1.get() == 1):
            i = i+1
        if(self.gender2.get() == 1):
            i = i+1
        if(i >= 1):
            if(self.gender1.get() != 1):
                self.gender_choice1.config(state='disabled')
            if(self.gender2.get() != 1):
                self.gender_choice2.config(state='disabled')
        else:
            self.gender_choice1.config(state='normal')
            self.gender_choice2.config(state='normal')


    def clear_user(self):
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.confpassword_entry.delete(0, END)
        self.gender_choice1.deselect()
        self.gender_choice2.deselect()
        self.email_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.lastname_entry.delete(0, END)
        self.telphone_entry.delete(0, END)
        self.gender_choice1.config(state='normal')
        self.gender_choice2.config(state='normal')


    def register_user(self):
        username_info = self.username.get()
        password_info = self.password.get()
        confpassword_info = self.confpassword.get()
        name_info = self.name.get()
        lastname_info = self.lastname.get()
        email_info = self.email.get()
        gender_info = 'MALE'
        tel_info = self.telphone.get()

        email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")

        df = pandas.read_csv('login.csv')
        checkuser = df['USER'].tolist()
        if username_info in checkuser:
            messagebox.showinfo("Info", "This Username Already Exists",
                                parent=self.register_screen)

        elif (username_info == ''):
            messagebox.showinfo("Info", "Please Enter Username",
                                parent=self.register_screen)

        elif (password_info == ''):
            messagebox.showinfo("Info", "Please Enter Password",
                                parent=self.register_screen)

        elif (confpassword_info == ''):
            messagebox.showinfo(
                "Info", "Please Enter Confirm Password", parent=self.register_screen)

        elif (password_info != confpassword_info):
            messagebox.showerror("Error", "Password Not Match",
                                parent=self.register_screen)
            self.password_entry.delete(0, END)
            self.confpassword_entry.delete(0, END)

        elif (name_info == ''):
            messagebox.showinfo(
                "Info", "Please Enter First Name", parent=self.register_screen)

        elif (lastname_info == ''):
            messagebox.showinfo("Info", "Please Enter Last Name",
                                parent=self.register_screen)

        elif (self.gender1.get() == 0 and self.gender2.get() == 0):
            messagebox.showinfo(
                "Error", "Please Select Your Gender", parent=self.register_screen)

        elif (email_info == ''):
            messagebox.showinfo(
                "Info", "Please Enter Your Email", parent=self.register_screen)

        elif (email_regex.match(email_info) == None):
            messagebox.showerror("Error", "Email Invalid", parent=self.register_screen)

        elif (tel_info == ''):
            messagebox.showinfo(
                "Info", "Please Enter Phone Number", parent=self.register_screen)
        
        elif (tel_info.isdigit() == False or len(tel_info) != 10):
            messagebox.showerror("Error", "Phone Number Invalid",parent=self.register_screen)
            self.telphone_entry.delete(0,END)
            
        else:
            if self.gender1.get() == 0:
                gender_info = 'FEMALE'
            # Write File
            if (messagebox.askokcancel("Confirmation", "Are you sure?", parent=self.register_screen)) == True:

                with open('login.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([username_info, password_info,
                                    name_info.capitalize(), lastname_info.capitalize(), gender_info, email_info, str(tel_info)])
                self.clear_user()
                self.register_screen.destroy()
                messagebox.showinfo("Alert", "Register Sucessfully!!")
            else:
                pass

class Shop_main_screen:
    def __init__(self):
        self.shop_window = tk.Tk()
        self.shop_window.title("Unknown Book Store")
        x = (700) - (750/2)
        y = (420) - (500/2)
        self.shop_window.geometry("1280x720+%d+%d" % (x, y))
        bg_path = "MAIN\Picture\ShopPage\Shop_main_page.png"
        bg = ImageTk.PhotoImage(Image.open(bg_path).resize((1280, 720)))

        canvas = Canvas(self.shop_window, width=1280, height=720)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor="nw")

        # logo_path = "MAIN\Picture\ShopPage\logo.png"
        # logo = ImageTk.PhotoImage(Image.open(logo_path).resize((150, 150)))

        name = tk.StringVar()
        nameEntered = Entry(self.shop_window, width=70, textvariable=name)
        nameEntered.place(x=400, y=50)

        combo = Combobox(self.shop_window)
        combo['values'] = ("All", "English Books", "Thai Books")
        combo.current(0)  # set the selected item
        combo.place(x=770, y=50)

        button = Button(self.shop_window, text="Search")
        button.place(x=913, y=47)

        # label1 = tk.Label(image=logo)
        # label1.image = logo
        # label1.place(x=0, y=0)

        self.banner1_path = "MAIN\Picture\ShopPage\\banner1.jpg"
        self.banner2_path = "MAIN\Picture\ShopPage\\banner2.jpg"
        self.banner3_path = "MAIN\Picture\ShopPage\\banner3.jpg"
        self.banner1 = ImageTk.PhotoImage(Image.open(self.banner1_path))
        self.banner2 = ImageTk.PhotoImage(Image.open(self.banner2_path))
        self.banner3 = ImageTk.PhotoImage(Image.open(self.banner3_path))

        self.banner_label = tk.Label(self.shop_window)
        self.banner_label.pack()

        self.dot1_path = "MAIN\Picture\ShopPage\movingdot1.png"
        self.dot2_path = "MAIN\Picture\ShopPage\movingdot2.png"
        self.dot3_path = "MAIN\Picture\ShopPage\movingdot3.png"
        self.dot1 = ImageTk.PhotoImage(Image.open(self.dot1_path))
        self.dot2 = ImageTk.PhotoImage(Image.open(self.dot2_path))
        self.dot3 = ImageTk.PhotoImage(Image.open(self.dot3_path))

        self.dot_label = tk.Label(self.shop_window)
        self.dot_label.pack()

        button1_path = "MAIN\Picture\ShopPage\\button1.png"
        img_button1 = ImageTk.PhotoImage(Image.open(button1_path).resize((175, 48)))
        self.button1 = Button(image=img_button1)
        canvas.create_window(0, 222, window=self.button1,anchor = "nw")

        button2_path = "MAIN\Picture\ShopPage\\button2.png"
        img_button2 = ImageTk.PhotoImage(Image.open(button2_path).resize((175, 48)))
        self.button2 = Button(image=img_button2)
        canvas.create_window(0, 307, window=self.button2,anchor = "nw")

        button3_path = "MAIN\Picture\ShopPage\\button3.png"
        img_button3 = ImageTk.PhotoImage(Image.open(button3_path).resize((175, 48)))
        self.button3 = Button(image=img_button3)
        canvas.create_window(0, 393, window=self.button3,anchor = "nw")

        button4_path = "MAIN\Picture\ShopPage\\button4.png"
        img_button4 = ImageTk.PhotoImage(Image.open(button4_path).resize((175, 48)))
        self.button4 = Button(image=img_button4)
        canvas.create_window(0, 477, window=self.button4,anchor = "nw")

        button5_path = "MAIN\Picture\ShopPage\\button5.png"
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

class Payment_screen:
    def __init__(self):
        self.payment_window = tk.Tk()
        self.payment_window.title("Unknown Book Store // Payment")
        x = (700) - (750/2)
        y = (420) - (500/2)
        self.payment_window.geometry("1280x720+%d+%d" % (x, y))
        bg_path = "MAIN\Picture\PaymentPage\Infobook_BG.png"
        bg = ImageTk.PhotoImage(Image.open(bg_path).resize((1280, 720)))
        canvas = Canvas(self.payment_window, width=1280, height=720)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor="nw")

        self.payment_window.resizable(0, 0)
        self.payment_window.mainloop()
RunMain = main_account_screen()
