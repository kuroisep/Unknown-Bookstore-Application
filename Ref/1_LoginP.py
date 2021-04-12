# from tkinter import *        
# from PIL import ImageTk, Image

# app_root = Tk()

# #Setting it up
# img = ImageTk.PhotoImage(Image.open("image.jpg"))

# #Displaying it
# imglabel = Label(app_root, image=img).grid(row=1, column=1)        


# app_root.mainloop()
# # 'D:/CE/2.sophomore/term2/Data Structure And Algorithm/Project/Git/Proj/image.jpg'



from tkinter import * 
from tkinter.ttk import *
from time import strftime
from functools import partial
from tkinter import Tk

# creating tkinter window
root = Tk()
root.title("READ ME | READ ME UP !!")
root.geometry("700x700")

# Creating object of photoimage class
# Image should be in the same folder
# in which script is saved
p1 = PhotoImage(file = 'open-book.png')
 
# Setting icon of master window
root.iconphoto(False, p1)

# This function is used to 
# display time on the label
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)
def validateLogin(username, password):
	print("Username entered :", username.get())
	print("Password entered :", password.get())
	return

lbl = Label(root, 
            font = ('calibri', 40, 'bold'),
            background = 'purple',
            foreground = 'white'
            )
lbl.pack(anchor = 'center')
time()


#username label and text entry box
usernameLabel = Label(root, text="User Name").place(x=245, y=100)
username = StringVar()
usernameEntry = Entry(root, textvariable=username,background='pink').place(x=330, y=100)


#password label and password entry box
passwordLabel = Label(root,text="Password").place(x=245, y=130) 
password = StringVar()
passwordEntry = Entry(root, textvariable=password, show='*', background='pink').place(x=330, y=130)

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(root, text="Login", command=validateLogin).place(x=330, y=170)



# loginButton.pack(fill=X)

# btn_fill = Button(tkWindow, text="Button")
# btn_fill.pack(fill=X)

mainloop()