
from tkinter import *
from PIL import Image, ImageDraw, ImageFont, ImageTk
from tkinter import filedialog, simpledialog
import os
import cv2
from tkinter.filedialog import SaveFileDialog, askopenfilename

root = Tk()
root.geometry("800x700+300+150")
root.resizable(width=True, height=True)


def op():
        im = Image.open(askopenfilename())
        caption = simpledialog.askstring("Label", "What would you like the label on your picture to say?")
        fontsize = 30
        if im.mode != "RGBA":
            im = im.convert("RGBA")
        txt = Image.new('RGBA', im.size, (255,255,255,0))

        draw = ImageDraw.Draw(txt)
        font = ImageFont.truetype("arial.ttf", fontsize)
        draw.text((0, 0),caption,(255,0,0),font=font)



        file = filedialog.asksaveasfile(mode='w', defaultextension=".png", filetypes=(("PNG file", "*.png"),("All Files", "*.*") ))
        if file:
            abs_path = os.path.abspath(file.name)
            out = Image.alpha_composite(im, txt)
            out.save(abs_path) # saves the image to the input file name. 

global filename
filename = ''
def openfn():
    filename = filedialog.askopenfilename(initialdir='UnknownShop\\Picture\\ShopPage\\USER_PIC',title='open')
    return filename

def open_img():
    x = openfn()
    img = Image.open(x)
    img = img.resize((500, 500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    my_label = Label(root, text=x,font=20).pack()

    panel = Label(root, image=img)
    panel.image = img
    panel.pack()

    # save_img(x)
    # x = str(x)
    # picture_path = os.path.split(x)
    print(f"Open Flie : {x}")
    # x.destroyAllWindows()

    

def save_img(filename):
    # print(f"Save Flie : {x}")
    # print("Save Image Successfully!")
    filename = filedialog.askopenfilename(initialdir='UnknownShop\\Picture\\ShopPage\\USER_PIC',title='open')
    img = cv2.imread(filename)
    cv2.imshow('Cat image', img)
    cv2.imwrite('55555555555rrrrrrrrr.png', img )
    
    # img.save("Proj_2563\\UnknownShop")

btn = Button(root, text=' <open image> ', command=open_img).pack()
bbb = Button(root, text=' <save image> ', command=save_img).pack()

root.mainloop()