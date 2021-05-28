import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import font as tkFont
from tkinter.ttk import Combobox
from tkinter import ttk
import pandas
from PIL import ImageTk, Image
import re
import os
import csv

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


from UnknownShop import ShopPage,AdminPage
from numpy.core.defchararray import upper

class main_account_screen:

    def __init__(self):
        self.main_screen = Tk()
        self.myfont = 'TRACK'

        """ set icon program desktop
        # icon_path = "UnknownShop\Picture\LoginPage\open-book.png"
        # icon = PhotoImage(file=icon_path)
        # self.main_screen.iconphoto(False, icon)
        """

        x = (960) - (1280/2)
        y = (540) - (720/2)
        self.main_screen.geometry("1280x720+%d+%d" % (x, y))
        self.main_screen.title("Account Login")

        bg_path = "UnknownShop\Picture\LoginPage\LOGIN.png"
        bg = ImageTk.PhotoImage(Image.open(bg_path).resize((1280, 720)))

        """ 
        THEAM
        """
        style = ttk.Style(self.main_screen)
        # Import the tcl file
        self.main_screen.tk.call('source', 'UnknownShop/azure.tcl')

        # Set the theme with the theme_use method
        style.theme_use('azure')
        """ 
        THEAM
        """

        loginframe = tk.LabelFrame( self.main_screen ,borderwidth=0, highlightthickness=0)
        loginframe.place(x=0, y=0, height=720, width=1280)

        # Create Canvas
        canvas = Canvas(loginframe, width=1280, height=720, bd=0, highlightthickness=0, relief='ridge')
        canvas.pack(fill="both", expand=True)

        # Display image
        canvas.create_image(0, 0, image=bg, anchor="nw")

        global username_verify
        global password_verify

        username_verify = StringVar()
        password_verify = StringVar()

        global username_login_entry
        global password_login_entry



        img_logo_path = "UnknownShop\Picture\LoginPage\logo.png"
        img_logo = ImageTk.PhotoImage(Image.open(img_logo_path).resize((200, 200)))
        canvas.create_image(200, 150, image=img_logo, anchor="nw")

        canvas.create_text(280, 350, text="Welcome", font=(self.myfont, 60), anchor="n")
        canvas.create_text(320, 430, text="To the land of books",
                        font=(self.myfont, 20), anchor="n")
                       
        
        canvas.create_text(1010, 170, text="Signin", font=(self.myfont, 40))

        canvas.create_text(915, 250, text="Username", font=(self.myfont))
        username_login_entry = ttk.Entry(
            textvariable=username_verify, width=20, font=20)

        canvas.create_window(1010, 290, window=username_login_entry)

        canvas.create_text(915, 340, text="Password", font=self.myfont)
        password_login_entry = ttk.Entry(
            textvariable=password_verify, show='●', width=20, font=20)
        canvas.create_window(1010, 380, window=password_login_entry)

        login_button = Button(text="LOGIN", command=self.login_verify,
                            bd=3, highlightthickness=0, width=20, height=2,background = "green3",highlightbackground = "black",activebackground="green2",activeforeground="white")
        login_button.place(x=840, y = 440)

        regis_button = Button(text="REGISTER", command=self.register ,
                            bd=3, highlightthickness=0, width=20, height=2,background = "orange2",highlightbackground = "black",activebackground="orange1",activeforeground="white")
        regis_button.place(x=1040, y = 440)

        canvas.create_text(1230, 700, text="V.2.1.99", font=self.myfont)

        exit_button = Button(text="EXIT", command=self.confirm_closing,
                            bd=3, highlightthickness=0, width=20, height=2, background = "red2",highlightbackground = "black",activebackground="red",activeforeground="white")
        exit_button.place(x=940, y=500)


        self.main_screen.resizable(1, 1)
        self.main_screen.overrideredirect(1)
        self.main_screen.mainloop()

    def confirm_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.main_screen.destroy()

    def login_verify(self):
        self.username1 = username_verify.get()
        self.password1 = password_verify.get()
        df = pandas.read_csv('login.csv')
        data = df.set_index('USER').T.to_dict('list')
        
        if data.get(self.username1) != None:
            if str(data.get(self.username1)[1]) == str(self.password1):
                self.info_NAME = data.get(self.username1)[2]
                self.info_LNAME = data.get(self.username1)[3]
                self.info_GENDER = data.get(self.username1)[4]
                self.info_EMAIL = data.get(self.username1)[6]
                self.info_telphone = data.get(self.username1)[7]
                username_login_entry.delete(0, END)
                password_login_entry.delete(0, END)

                df.loc[df['USER'] == self.username1, 'STATUS'] = 'T'
                df.to_csv("login.csv", index=False)
                print(df)
                self.login_sucess()
            else:
                self.password_not_recognised()
                password_login_entry.delete(0, END)
        elif str(self.username1) == 'admin' and str(self.password1) == 'admin':
                username_login_entry.delete(0, END)
                password_login_entry.delete(0, END)
                self.delete_main_screen()
                AdminPage.showAdminPage()

        else:
            self.user_not_found()
            username_login_entry.delete(0, END)
            password_login_entry.delete(0, END)


    def login_sucess(self):
        self.login_success_screen = Toplevel(self.main_screen)
        self.login_success_screen.title("Login Success.")
        self.login_success_screen.focus_set()
        self.login_success_screen.grab_set()
        self.login_success_screen.overrideredirect(1)
        x = (960) - (400/2)
        y = (540) - (300/2)
        self.login_success_screen.geometry("400x300+%d+%d" % (x, y))
        canvas = Canvas(self.login_success_screen, width=400, height=300, background = "#2ECC71")
        canvas.pack(fill="both", expand=True)

        if self.info_GENDER == 'MALE':
            sex = 'Mr.'
        else:
            sex = 'Mrs.'
        
        # image_path = "UnknownShop/Picture/ShopPage/USER_PIC/{}.png".format(self.user[0][9])
        # self.user_img = ImageTk.PhotoImage(Image.open(image_path).resize((100, 100)))

        # canvas.create_image(550,200,image=self.user_img, anchor="")

        canvas.create_text(200, 70, text="<< Login Successfully >>", font = (self.myfont, 15))
        canvas.create_text(200, 100, text="WELCOME  {} {}  {}.".format(sex, self.info_LNAME, upper(self.info_NAME[0]) ), font = (self.myfont, 12))
        canvas.create_text(200, 130, text="Email : {}   \nPhone Number : 0{} ".format(self.info_EMAIL, self.info_telphone), font = (self.myfont, 10))
        ok_button = ttk.Button(self.login_success_screen, text="OK",
                        command=self.delete_login_success)
        canvas.create_window(200, 200, window=ok_button)

    def delete_login_success(self):
        self.login_success_screen.destroy()
        self.delete_main_screen()
        ShopPage.showShopPage()

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
        ok_button = Button(self.password_not_recog_screen, text="<    OK   >",
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
        ok_button = Button(self.user_not_found_screen, text="<   OK   >", width = 10,
                        command=self.delete_user_not_found_screen)
        canvas.create_window(200, 150, window=ok_button)


    def register(self):
        self.register_screen = Toplevel(self.main_screen)
        self.register_screen.title("Register")
        self.register_screen.focus_set()
        self.register_screen.grab_set()
        # self.register_screen.overrideredirect(1)
        self.register_screen.resizable(0, 0)

        x = (960) - (750/2)
        y = (540) - (650/2)
        self.register_screen.geometry("750x600+%d+%d" % (x, y))

        

        regis_bg_path = "UnknownShop\Picture\LoginPage\REGISTER.png"
        self.regis_bg = ImageTk.PhotoImage(Image.open(regis_bg_path).resize((750, 600)))

        self.registerframe = tk.LabelFrame(self.register_screen , text="register".upper())
        self.registerframe.place(x=0, y=0, height=600, width=750)

        filename = "UnknownShop/Picture/ShopPage/BG1.png"
        self.filenameBG = ImageTk.PhotoImage(Image.open(filename))
        background_label = Label(self.registerframe, image=self.filenameBG)
        background_label.place(x=375, y=300, anchor=CENTER)

        self.inner_registerframe = tk.LabelFrame( self.register_screen , text="USER INPUT")
        self.inner_registerframe.place(x=150, y=20, height=550, width=450)

        self.inner_registerframe_button = tk.LabelFrame( self.inner_registerframe)
        self.inner_registerframe_button.place(x=20, y=400, height=80, width=400)
        # canvas = Canvas(self.register_screen, width=750, height=600)
        # canvas.pack(fill="both", expand=True)
        # canvas.create_image(0, 0, image=self.regis_bg, anchor="nw")

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


        titletext1 = ["User", "Password", "Name","Gender","BirthDay","Phone Number"]
        titletext2 = ["Confirm Password","Last Name","","","Email Address",""]
        y1 = 10
        y2 = 70
        for i in range(6):
            self.Ausername = Label(self.inner_registerframe, text= titletext1[i], font=self.myfont)
            self.Busername = Label(self.inner_registerframe, text= titletext2[i], font=self.myfont)
            self.Ausername.place(x=25, y=y1)
            self.Busername.place(x=220, y=y2)
            y1 += 60
            y2 += 60

        self.username_entry = ttk.Entry(self.inner_registerframe, textvariable=self.username, width=20)
        self.password_entry = ttk.Entry(self.inner_registerframe, textvariable=self.password, show='●', width=20)
        self.confpassword_entry = ttk.Entry(self.inner_registerframe, textvariable=self.confpassword, show='●', width=20)
        self.name_entry = ttk.Entry(self.inner_registerframe, textvariable=self.name, width=20)
        self.lastname_entry = ttk.Entry(self.inner_registerframe, textvariable=self.lastname, width=20)
        self.gender_choice1 = Checkbutton(self.inner_registerframe, text="Male", font=(
            self.myfont, 12), command=self.my_upd, variable=self.gender1)
        self.gender_choice2 = Checkbutton(self.inner_registerframe, text="Female", font=(
            self.myfont, 12), command=self.my_upd, variable=self.gender2)

        self.birth_date_entry = Combobox(self.inner_registerframe, width=5,state = "readonly",value=['----','1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
                                                                             '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', 
                                                                             '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'])
        self.birth_date_entry.current(0) 
        self.birth_month_entry = Combobox(self.inner_registerframe, width=5, state = "readonly",value=['----','Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                                                                                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] )
        self.birth_month_entry.current(0)  
        
        year_list = ['----']
        for i in range(1920,2022):
            year_list.append(str(i))
        self.birth_year_entry = Combobox(self.inner_registerframe, width=5, value=year_list,state = "readonly")
        self.birth_year_entry.current(0)   

        self.telphone_entry = ttk.Entry(self.inner_registerframe, textvariable=self.telphone, width=20)
        self.email_entry = ttk.Entry(self.inner_registerframe, textvariable=self.email,width=20)

        self.username_entry.place(x=30,y=35)

        self.password_entry.place(x=30,y=95)
        self.confpassword_entry.place(x=220,y=95)
        
        self.name_entry.place(x=30,y=155)
        self.lastname_entry.place(x=220,y=155)
        
        self.gender_choice1.place(x=30,y=215)
        self.gender_choice2.place(x=120,y=215)

        self.birth_date_entry.place(x=30,y=275)
        self.birth_month_entry.place(x=95,y=275)
        self.birth_year_entry.place(x=160,y=275)

        self.telphone_entry.place(x=30,y=335)
        self.email_entry.place(x=220,y=335)

    
        helv20 = tkFont.Font(family='Helvetica', size=12, weight=tkFont.BOLD)
        regis_button = Button(self.inner_registerframe_button, text="Register".upper(),
                            font=helv20, bg="orange", fg="white", command=self.register_user, width=10, height=2,activebackground="orange2")
        clear_button = Button(self.inner_registerframe_button, text="Clear".upper(),
                            font=helv20, bg="blue", fg="white", command=self.clear_user_confirm,width=10, height=2,activebackground="blue2")
        cancel_button = Button(self.inner_registerframe_button, text="CANCEL", command=self.delete_register_screen,
                            font=helv20, bg="red", fg="white", highlightthickness=0, width=10, height=2, activebackground="red2")

        regis_button.grid(row=0, column=0,padx=10, pady=10)
        clear_button.grid(row=0, column=1,padx=10, pady=10)
        cancel_button.grid(row=0, column=2,padx=10, pady=10)
        



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
    def Birthday_Check(self):
        pass

    def clear_user_confirm(self):
        if (messagebox.askokcancel("Confirmation", "Are your sure?", parent=self.register_screen)) == True:
            self.clear_user()

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
        self.birth_date_entry.current(0)
        self.birth_month_entry.current(0)
        self.birth_year_entry.current(0)
        

    def register_user(self):
        username_info = self.username.get()
        password_info = self.password.get()
        confpassword_info = self.confpassword.get()
        name_info = self.name.get()
        lastname_info = self.lastname.get()
        email_info = self.email.get()
        gender_info = 'MALE'
        tel_info = self.telphone.get()
        birthday_info = str(self.birth_date_entry.get()) + '/' +  str(self.birth_month_entry.get()) + '/' + str(self.birth_year_entry.get())

        email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")

        df = pandas.read_csv('login.csv')
        check_user = df['USER'].tolist()
        if username_info in check_user:
            messagebox.showinfo("Info", "This Username Already Exists.",
                                parent=self.register_screen)
        elif len(username_info) < 8:
            messagebox.showinfo("Info", "This Username Must have At Least 8 Characters.",
                                parent=self.register_screen)

        elif (username_info == ''):
            messagebox.showinfo("Info", "Please Enter Username.",
                                parent=self.register_screen)

        elif (password_info == ''):
            messagebox.showinfo("Info", "Please Enter Password.",
                                parent=self.register_screen)
        elif (len(password_info) < 8):
            messagebox.showinfo("Info", "Password Must Have At Least 8 Characters.",
                                parent=self.register_screen)

        elif (confpassword_info == ''):
            messagebox.showinfo(
                "Info", "Please Enter Confirm Password.", parent=self.register_screen)

        elif (password_info != confpassword_info):
            messagebox.showerror("Error", "Password Not Match.",
                                parent=self.register_screen)
            self.password_entry.delete(0, END)
            self.confpassword_entry.delete(0, END)

        elif (name_info == ''):
            messagebox.showinfo(
                "Info", "Please Enter First Name.", parent=self.register_screen)

        elif (lastname_info == ''):
            messagebox.showinfo("Info", "Please Enter Last Name.",
                                parent=self.register_screen)

        elif (str(self.birth_date_entry.get()) == '----') and (str(self.birth_month_entry.get()) == '----') and (str(self.birth_year_entry.get()) == '----'):
            messagebox.showinfo("Info", "Please Enter your Birthday.", parent=self.register_screen)
       
        elif (str(self.birth_date_entry.get()) == '----') and (str(self.birth_month_entry.get()) == '----'):
            messagebox.showinfo("Info", "Please Enter your Birth day and Birth month.", parent=self.register_screen)
        elif (str(self.birth_date_entry.get()) == '----') and (str(self.birth_year_entry.get()) == '----'):
            messagebox.showinfo("Info", "Please Enter your Birth day and Birth year.", parent=self.register_screen)
        elif (str(self.birth_month_entry.get()) == '----') and (str(self.birth_year_entry.get()) == '----'):
            messagebox.showinfo("Info", "Please Enter your Birth month and Birth year.", parent=self.register_screen)

        elif (str(self.birth_date_entry.get()) == '----'):
            messagebox.showinfo("Info", "Please Enter your Birth day.", parent=self.register_screen)
        elif (str(self.birth_month_entry.get()) == '----'):
            messagebox.showinfo("Info", "Please Enter your Birth month.", parent=self.register_screen)
        elif (str(self.birth_year_entry.get()) == '----'):
            messagebox.showinfo("Info", "Please Enter your Birth year.", parent=self.register_screen)

        elif (str(self.birth_month_entry.get()) == 'Feb'):
            if  (str(self.birth_date_entry.get()) == '29') and (int(self.birth_year_entry.get()) % 4 != 0 and int(self.birth_year_entry.get()) % 100 != 0 and int(self.birth_year_entry.get()) % 400 != 0):
                messagebox.showinfo("Info", "Please Check your Birthday.", parent=self.register_screen)
            elif (str(self.birth_date_entry.get()) == '30' or str(self.birth_date_entry.get()) == '31'):
                    messagebox.showinfo("Info", "Please Check your Birthday.", parent=self.register_screen)
        elif (str(self.birth_date_entry.get()) == '30') and (str(self.birth_month_entry.get()) != ['Apr', 'Jun', 'Sep', 'Nov']):
            messagebox.showinfo(
                "Info", "Please Check your Birthday.", parent=self.register_screen)
        elif (str(self.birth_date_entry.get()) == '31') and (str(self.birth_month_entry.get()) != ['Jan','Mar', 'May', 'Jul', 'Aug', 'Oct', 'Dec']):
            messagebox.showinfo(
                "Info", "Please Check your Birthday.", parent=self.register_screen)
        

        elif (self.gender1.get() == 0 and self.gender2.get() == 0):
            messagebox.showinfo(
                "Error", "Please Select Your Gender.", parent=self.register_screen)
        elif (tel_info == ''):
            messagebox.showinfo(
                "Info", "Please Enter Phone Number.", parent=self.register_screen)
        
        elif (tel_info[0] != "+" or tel_info[1] != '6' or tel_info[2] != '6' or ((len(tel_info) < 12) or (len(tel_info) > 13) ))  :
            messagebox.showerror("Error", "Phone Number Invalid.",parent=self.register_screen)
            self.telphone_entry.delete(0,END)

        elif (email_info == ''):
            messagebox.showinfo(
                "Info", "Please Enter Your Email.", parent=self.register_screen)

        elif (email_regex.match(email_info) == None):
            messagebox.showerror("Error", "Email Invalid.", parent=self.register_screen)

        
        
        else:
            if self.gender1.get() == 0:
                gender_info = 'FEMALE'
            # Write File
            if (messagebox.askokcancel("Confirmation", "Are your sure?", parent=self.register_screen)) == True:

                with open('login.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['F',username_info, password_info,
                                    name_info.capitalize(), lastname_info.capitalize(), gender_info,birthday_info, email_info, str(tel_info),'account',"100"])
                self.clear_user()
                self.register_screen.destroy()
                messagebox.showinfo("Alert", "Register Sucessfully!!")
            else:
                pass

def showLoginPage():
    run = main_account_screen()

if __name__ == '__main__':
    showLoginPage()