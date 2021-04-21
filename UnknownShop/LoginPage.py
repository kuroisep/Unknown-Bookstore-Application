import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import font as tkFont
import pandas
from PIL import ImageTk, Image
import re
import os
import csv

class main_account_screen:

    def __init__(self):
        self.main_screen = Tk()
        self.myfont = 'TRACK'
        base_folder = os.path.dirname(__file__)

        icon_path = "MAIN\Picture\LoginPage\open-book.png"
        icon = PhotoImage(file=icon_path)
        self.main_screen.iconphoto(False, icon)

        x = (960) - (1280/2)
        y = (540) - (720/2)
        self.main_screen.geometry("1280x720+%d+%d" % (x, y))
        self.main_screen.title("Account Login")


        # bg_path = os.path.join(base_folder, 'LOGIN.png')
        bg_path = "MAIN\Picture\LoginPage\LOGIN.png"
        bg = ImageTk.PhotoImage(Image.open(bg_path).resize((1280, 720)))
        # bg = PhotoImage(file = bg_path)

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

        # img_logo_path = os.path.join(base_folder, 'logo.jpg')
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

        # img_login_path = os.path.join(base_folder, 'login-button1.png')
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


RunMain = main_account_screen()
