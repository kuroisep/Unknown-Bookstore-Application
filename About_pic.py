
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import cv2
from tkinter.filedialog import SaveFileDialog

root = Tk()
root.geometry("550x600+300+150")
root.resizable(width=True, height=True)

def openfn():
    filename = filedialog.askopenfilename(title='open')
    print(filename)
    return str(filename)

def open_img():
    x = openfn()
    img = Image.open(x)

    img = img.resize((400, 400), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    panel = Label(root, image=img)
    panel.image = img
    panel.pack()

def save_img():
    
    # img = cv2.imread(openfn())
    # # cv2.imshow('Cat image', img)
    # cv2.imwrite('colorrrrrrrrr.jpg', img )

btn = Button(root, text=' <open image> ', command=open_img).pack()
bbb = Button(root, text=' <save image> ', command=save_img).pack()


root.mainloop()