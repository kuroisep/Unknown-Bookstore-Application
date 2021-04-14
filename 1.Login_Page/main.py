#import modules

from tkinter import *
import os
from PIL import ImageTk, Image
# from tkinter.ttk import *


# Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    x = (910) - (300/2)
    y = (460) - (250/2)
    register_screen.geometry("450x450+%d+%d" % (x, y))

    global username
    global password
    global confpassword
    global username_entry
    global password_entry
    global confpassword_entry


    global name
    global lastname
    global gender
    global email
    global name_entry
    global lastname_entry
    global email_entry

    username = StringVar()
    password = StringVar()
    confpassword = StringVar()
    
    name = StringVar()
    lastname = StringVar()
    email = StringVar()
    gender1 = StringVar()
    gender2 = StringVar()
    gender1 = ""
    gender2 = ""

    Label(register_screen, text="").pack()
    Label(register_screen, text="Please enter details below",bg="blue", fg="white").pack()
    
    Label(register_screen, text="").pack()
    
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()

    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='●')
    password_entry.pack()

    confpassword_lable = Label(register_screen, text="Confirm Password * ")
    confpassword_lable.pack()
    confpassword_entry = Entry(register_screen, textvariable=confpassword, show='●')
    confpassword_entry.pack()
    
    name_lable = Label(register_screen, text="Name * ")
    name_lable.pack()
    name_entry = Entry(register_screen, textvariable=name)
    name_entry.pack()

    lastname_lable = Label(register_screen, text="LastName * ")
    lastname_lable.pack()
    lastname_entry = Entry(register_screen, textvariable=lastname)
    lastname_entry.pack()

    gender_lable = Label(register_screen, text="Gender * ")
    gender_lable.pack()
    gender_choice = Checkbutton(register_screen, text="Male", command=my_upd, variable=gender1)
    gender_choice.pack()
    gender_choice = Checkbutton(register_screen, text="Female", command=my_upd, variable=gender2)
    gender_choice.pack()

    email_lable = Label(register_screen, text="Email Address * ")
    email_lable.pack()
    email_entry = Entry(register_screen, textvariable=email)
    email_entry.pack()

    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10,height=1, bg="blue", fg="white", command=register_user).pack()
    Button(register_screen, text="Clear", width=10,height=1, bg="blue", fg="white", command=register_user).pack()

def my_upd():  
    if(gender1.get() == 1):
        gender2.configure(state='disabled')
    if(gender2.get() == 1):
        gender1.configure(state='disabled')

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

# Implementing event on register button


def register_user():

    username_info = username.get()
    password_info = password.get()
    confpassword_info = confpassword.get()
    # name_info = name.get()
    # lastname_info = lastname.get
    # gender_info = gender.get()
    
    if (username_info == ''):
        Label(register_screen, text="Enter User",
              fg="red", font=(myfont, 11)).pack()

    elif (password_info == '' or confpassword_info == ''):
        Label(register_screen, text="Enter Pass",
              fg="red", font=(myfont, 11)).pack()

    elif (password_info != confpassword_info):
        Label(register_screen, text="Pass Not Match",
              fg="red", font=(myfont, 11)).pack()
        password_entry.delete(0, END)
        confpassword_entry.delete(0, END)

    else:
        file = open(username_info, "w")
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()

        username_entry.delete(0, END)
        password_entry.delete(0, END)
        confpassword_entry.delete(0, END)

        Label(register_screen, text="Registration Success",
              fg="green", font=(myfont, 11)).pack()

# Implementing event on login button


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
    login_success_screen.geometry("150x100+%d+%d" % (x, y))
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK",
           command=delete_login_success).pack()

# Designing popup for login invalid password


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title("Success")
    x = (960) - (150/2)
    y = (540) - (100/2)
    password_not_recog_screen.geometry("150x100+%d+%d" % (x, y))
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK",
           command=delete_password_not_recognised).pack()

# Designing popup for user not found


def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(main_screen)
    Label(user_not_found_screen, text='').pack()
    user_not_found_screen.title("Success")
    x = (960) - (150/2)
    y = (540) - (100/2)
    user_not_found_screen.geometry("150x100+%d+%d" % (x, y))
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

    bg_path = os.path.join(base_folder, 'LOGIN.png')
    bg = ImageTk.PhotoImage(Image.open(bg_path).resize((1280, 720)))
    # bg = PhotoImage(file = bg_path)
  
    # Create Canvas
    canvas = Canvas( main_screen, width = 1280,height = 720)
  
    canvas.pack(fill = "both", expand = True)
  
    # Display image
    canvas.create_image( 0, 0, image = bg, 
                     anchor = "nw")
    
    global username_verify
    global password_verify
    global username_login_entry

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    img_logo_path = os.path.join(base_folder, 'logo.jpg')
    img_logo = ImageTk.PhotoImage(Image.open(img_logo_path).resize((150, 150)))
    canvas.create_image(200,50,image = img_logo,anchor = "nw")

    canvas.create_text( 280, 250, text = "Welcome" ,font = (myfont,60),anchor = "n")
    canvas.create_text( 320, 330, text = "To the land of books" ,font = (myfont,20),anchor = "n")


    canvas.create_text( 1000, 170, text = "Signin" ,font = (myfont,40))

    canvas.create_text(875,250,text = "Username",font=(myfont))
    username_login_entry = Entry(textvariable=username_verify,width=30,font=20)
    # username_login_entry.config(fg = 'blue')
    canvas.create_window(1000,290,window = username_login_entry)

    canvas.create_text(875,340,text = "Password",font=myfont)
    password_login_entry = Entry(textvariable=password_verify, show='●',width=30,font=20)
    canvas.create_window(1000,380,window = password_login_entry)
    

    
    img_login_path = os.path.join(base_folder, 'login-button1.png')
    img_login_button = ImageTk.PhotoImage(Image.open(img_login_path).resize((200, 300)))
    login_button = Button(image = img_login_button,command=login_verify,bd=0,highlightthickness=0,width=140,height=60)
    canvas.create_window(900,450,window = login_button)

    regis_button = Button(text="Register", height="3", width="20", command=register,highlightthickness=0,borderwidth = 0)
    canvas.create_window(1100,450,window = regis_button)

    canvas.create_text(1230,700,text = "V.1.0.0",font=myfont)

    


    # canvas = Canvas(main_screen, width=700, height=300)
    # canvas.pack()

    # logo_path = os.path.join(base_folder,'logo.jpg')
    # img = ImageTk.PhotoImage(Image.open(logo_path).resize((700, 300)))
    # canvas.create_image(0, 0, anchor=NW, image=img)

    
    main_screen.resizable(0,0)
    main_screen.overrideredirect(0)
    main_screen.mainloop()


main_account_screen()
