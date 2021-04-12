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
from functools import partial

def validateLogin(username, password):
	print("Username entered :", username.get())
	print("Password entered :", password.get())
	return

#window
tkWindow = Tk()  
tkWindow.geometry('777x777')  
tkWindow.title('READ A BOOK')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").place(x=230, y=100)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username,background='pink').place(x=330, y=100)

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").place(x=230, y=130) 
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*', background='pink').place(x=330, y=130)

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).place(x=330, y=170)  

tkWindow.mainloop()

#OHYEAH
