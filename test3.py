# from tkinter import *        
# from PIL import ImageTk, Image


# app_root = Tk()

# #Setting it up
# img = ImageTk.PhotoImage(Image.open("image.jpg"))

# #Displaying it
# imglabel = Label(app_root, image=img).grid(row=1, column=1)        


# app_root.mainloop()

from tkinter import *
from winsound import *

root = Tk() # create tkinter window

play = lambda: PlaySound('music.wav', SND_FILENAME)
button = Button(root, text = 'Play', command = play).grid(row=1,column=8)
text = Label(root,text= 'Hello').grid(row=2,column=8)

# button.pack()
# button.place(x=200,y=200)
root.mainloop()