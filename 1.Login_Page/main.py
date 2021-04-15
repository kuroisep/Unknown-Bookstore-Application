#import modules

from tkinter import *
import os
from PIL import ImageTk, Image
from tkinter import messagebox
# from tkinter_custom_button import TkinterCustomButton
import re


# Designing window for registration

def register():
    global register_screen
    global regis_bg
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    x = (960) - (750/2)
    y = (540) - (650/2)
    register_screen.geometry("750x600+%d+%d" % (x, y))

    regis_bg_path = "1.Login_Page\Picture\REGISTER.png"
    regis_bg = ImageTk.PhotoImage(Image.open(regis_bg_path).resize((750,600)))

    canvas = Canvas(register_screen, width=750, height=600)  
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=regis_bg,anchor="nw")


    global username
    global password
    global confpassword
    global username_entry
    global password_entry
    global confpassword_entry

    global name
    global lastname
    global gender1
    global gender2
    global email
    global name_entry
    global lastname_entry
    global gender_choice1
    global gender_choice2
    global email_entry

    username = StringVar()
    password = StringVar()
    confpassword = StringVar()

    name = StringVar()
    lastname = StringVar()

    email = StringVar()

    gender1 = IntVar()
    gender2 = IntVar()
    gender_choice1 = IntVar(register_screen)
    gender_choice2 = IntVar(register_screen)



    canvas.create_text(375, 60, text="Please enter details below", font=myfont)

    canvas.create_text(65, 150, text="Username *", font=myfont)
    username_entry = Entry(register_screen, textvariable=username)
    canvas.create_window(115, 175, window=username_entry, width=180)

    password_entry = Entry(register_screen, textvariable=password, show='●')
    canvas.create_text(290, 150, text="Password *", font=myfont)
    canvas.create_window(340, 175, window=password_entry, width=180)

    confpassword_entry = Entry(
        register_screen, textvariable=confpassword, show='●')
    canvas.create_text(580, 150, text="Confirm Password *", font=myfont)
    canvas.create_window(600, 175, window=confpassword_entry, width=180)

    name_entry = Entry(register_screen, textvariable=name)
    canvas.create_text(50, 225, text="Name *", font=myfont)
    canvas.create_window(115, 250, window=name_entry, width=180)

    lastname_entry = Entry(register_screen, textvariable=lastname)
    canvas.create_text(292, 225, text="Last Name *", font=myfont)
    canvas.create_window(340, 250, window=lastname_entry, width=180)

    canvas.create_text(600, 225, text="Gender *", font=myfont)
    gender_choice1 = Checkbutton(register_screen, text="Male", font=(myfont, 12), command=my_upd, variable=gender1)
    gender_choice2 = Checkbutton(register_screen, text="Female", font=(myfont, 12), command=my_upd, variable=gender2)
    gender_choice1 = Checkbutton(register_screen, text="Male",font=(myfont, 10), command=my_upd, variable=gender1)
    gender_choice2 = Checkbutton(register_screen, text="Female", font=(myfont, 10), command=my_upd, variable=gender2)
    canvas.create_window(550, 250, window=gender_choice1)
    canvas.create_window(650, 250, window=gender_choice2)

    canvas.create_text(85, 310, text="Email Address * ", font=myfont)
    email_entry = Entry(register_screen, textvariable=email)
    canvas.create_window(150, 335, window=email_entry, width=250)

    regis_button = Button(register_screen, text="Register", width=20,
                          height=3, bg="blue", fg="white", command=register_user)
    canvas.create_window(400, 420, window=regis_button)
    clear_button = Button(register_screen, text="Clear", width=20,
                          height=3, bg="blue", fg="white", command=clear_user)
    canvas.create_window(600, 420, window=clear_button)
    
  
    


def my_upd():
    i = 0
    if(gender1.get() == 1):
        i = i+1
    if(gender2.get() == 1):
        i = i+1
    if(i >= 1):
        if(gender1.get() != 1):
            gender_choice1.config(state='disabled')
        if(gender2.get() != 1):
            gender_choice2.config(state='disabled')
    else:
        gender_choice1.config(state='normal')
        gender_choice2.config(state='normal')
# c1_v=tk.IntVar(my_w)
# c1=tk.Checkbutton(my_w,text='Python',command=my_upd,variable=c1_v)
# c1.grid(row=1,column=1)

# c2_v=tk.IntVar(my_w)
# c2=tk.Checkbutton(my_w,text='PHP',command=my_upd,variable=c2_v)
# c2.grid(row=1,column=2)


# Designing window for login

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    x = (960) - (300/2)
    y = (540) - (250/2)
    login_screen.geometry("300x250+%d+%d" % (x, y))
    Label(login_screen, text="").pack()
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(
        login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10,
           height=1, command=login_verify).pack()


def clear_user():
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    confpassword_entry.delete(0, END)
    gender_choice1.deselect()
    gender_choice2.deselect()
    email_entry.delete(0, END)
    name_entry.delete(0, END)
    lastname_entry.delete(0, END)
    gender_choice1.config(state='normal')
    gender_choice2.config(state='normal')


def register_user():

    username_info = username.get()
    password_info = password.get()
    confpassword_info = confpassword.get()
    name_info = name.get()
    lastname_info = lastname.get()
    email_info = email.get()
    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")

    if (username_info == ''):
        messagebox.showinfo("Info", "Please Enter Username",parent=register_screen)

    elif (password_info == ''):
        messagebox.showinfo("Info", "Please Enter Password",parent=register_screen)
    
    elif (confpassword_info == ''):
        messagebox.showinfo("Info", "Please Enter Confirm Password",parent=register_screen)

    elif (password_info != confpassword_info):
        messagebox.showerror("Error", "Password Not Match",parent=register_screen)
        password_entry.delete(0, END)
        confpassword_entry.delete(0, END)
    
    elif (name_info == ''):
        messagebox.showinfo("Info", "Please Enter First Name",parent=register_screen)
    
    elif (lastname_info == ''):
        messagebox.showinfo("Info", "Please Enter Last Name",parent=register_screen)
    
    elif (gender1.get() == 0 and gender2.get() == 0):
        messagebox.showinfo("Error", "Please Select Your Gender",parent=register_screen)

    elif (email_info == ''):
        messagebox.showinfo("Info", "Please Enter Your Email",parent=register_screen)

    elif (email_regex.match(email_info) == None):
        messagebox.showerror("Error", "Email Invalid",parent=register_screen)

    else:
        # Write File
        # file = open(username_info, "w")
        # file.write(username_info + "\n")
        # file.write(password_info)
        # file.close()
        
        if (messagebox.askokcancel("Confirmation", "Are you sure?",parent = register_screen) ) == True:
            clear_user()
            register_screen.destroy()
            messagebox.showinfo("Alert", "Register Sucessfully!!")
        else:
            pass



def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()

# Designing popup for login success


def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(main_screen)
    login_success_screen.title("Success")
    x = (960) - (150/2)
    y = (540) - (100/2)
    login_success_screen.geometry("300x300+%d+%d" % (x, y))
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK",
           command=delete_login_success).pack()

# Designing popup for login invalid password


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title("Success")
    x = (910) - (150/2)
    y = (490) - (100/2)
    password_not_recog_screen.geometry("300x300d+%d" % (x, y))
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK",
           command=delete_password_not_recognised).pack()

# Designing popup for user not found


def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(main_screen)
    Label(user_not_found_screen, text='').pack()
    user_not_found_screen.title("Success")
    x = (910) - (150/2)
    y = (490) - (100/2)
    user_not_found_screen.geometry("300x300+%d+%d" % (x, y))
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK",
           command=delete_user_not_found_screen).pack()

# Deleting popups


def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()

# Designing Main(first) window


def main_account_screen():
    global main_screen
    global myfont
    myfont = 'TRACK'
    main_screen = Tk()
    base_folder = os.path.dirname(__file__)

    icon_path = os.path.join(base_folder, 'open-book.png')
    icon = PhotoImage(file=icon_path)
    main_screen.iconphoto(False, icon)

    x = (960) - (1280/2)
    y = (540) - (720/2)
    main_screen.geometry("1280x720+%d+%d" % (x, y))
    main_screen.title("Account Login")

    # bg_path = os.path.join(base_folder, 'LOGIN.png')
    bg_path = "1.Login_Page\Picture\LOGIN.png"
    bg = ImageTk.PhotoImage(Image.open(bg_path).resize((1280, 720)))
    # bg = PhotoImage(file = bg_path)

    # Create Canvas
    canvas = Canvas(main_screen, width=1280, height=720)

    canvas.pack(fill="both", expand=True)

    # Display image
    canvas.create_image(0, 0, image=bg,
                        anchor="nw")

    global username_verify
    global password_verify
    global username_login_entry

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    # img_logo_path = os.path.join(base_folder, 'logo.jpg')
    img_logo_path = "1.Login_Page\Picture\logo.png"
    img_logo = ImageTk.PhotoImage(Image.open(img_logo_path).resize((200, 200)))
    canvas.create_image(200, 150, image=img_logo, anchor="nw")

    canvas.create_text(280, 350, text="Welcome", font=(myfont, 60), anchor="n")
    canvas.create_text(320, 430, text="To the land of books",font=(myfont, 20), anchor="n")

    canvas.create_text(1000, 170, text="Signin", font=(myfont, 40))

    canvas.create_text(875, 250, text="Username", font=(myfont))
    username_login_entry = Entry(
        textvariable=username_verify, width=30, font=20)
    # username_login_entry.config(fg = 'blue')
    canvas.create_window(1000, 290, window=username_login_entry)

    canvas.create_text(875, 340, text="Password", font=myfont)
    password_login_entry = Entry(
        textvariable=password_verify, show='●', width=30, font=20)
    canvas.create_window(1000, 380, window=password_login_entry)

    # img_login_path = os.path.join(base_folder, 'login-button1.png')
    img_login_path = "1.Login_Page\Picture\login-button1.png"
    img_login_button = ImageTk.PhotoImage(
        Image.open(img_login_path).resize((200, 300)))
    login_button = Button(image=img_login_button, command=login_verify,
                          bd=0, highlightthickness=0, width=140, height=60)
    canvas.create_window(900, 450, window=login_button)

    img_regis_path = "1.Login_Page\Picture\\regis-button.png"
    img_regis_button = ImageTk.PhotoImage(
        Image.open(img_regis_path).resize((170, 80)))
    regis_button = Button(image=img_regis_button,width=140, height=60,
                          command=register, highlightthickness=0, borderwidth=0)
    canvas.create_window(1100, 450, window=regis_button)

    canvas.create_text(1230, 700, text="V.1.0.0", font=myfont)

    # canvas = Canvas(main_screen, width=700, height=300)
    # canvas.pack()

    # logo_path = os.path.join(base_folder,'logo.jpg')
    # img = ImageTk.PhotoImage(Image.open(logo_path).resize((700, 300)))
    # canvas.create_image(0, 0, anchor=NW, image=img)
    

    main_screen.resizable(0, 0)
    main_screen.overrideredirect(0)
    main_screen.mainloop()


main_account_screen()
