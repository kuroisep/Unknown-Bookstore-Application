# import tkinter as tk
 

# window = tk.Tk()
# window.title('My Window')
# window.geometry('100x100')
 
# l = tk.Label(window, bg='white', width=20, text='empty')
# l.pack()
 
# def print_selection():
#     if (var1.get() == 1) & (var2.get() == 0):
#         l.config(text='I love Python ')
#     elif (var1.get() == 0) & (var2.get() == 1):
#         l.config(text='I love C++')
#     elif (var1.get() == 0) & (var2.get() == 0):
#         l.config(text='I do not anything')
#     else:
#         l.config(text='I love both')
 
# var1 = tk.IntVar()
# var2 = tk.IntVar()
# c1 = tk.Checkbutton(window, text='Python',variable=var1, onvalue=1, offvalue=0, command=print_selection)
# c1.pack()
# c2 = tk.Checkbutton(window, text='C++',variable=var2, onvalue=1, offvalue=0, command=print_selection)
# c2.pack()
 
# window.mainloop()




# import tkinter as tk
# root=tk.Tk()

# c1=tk.BooleanVar()
# c2=tk.BooleanVar()
# c3=tk.BooleanVar()
# c4=tk.BooleanVar()

# def get_value():
#     for c in (c1,c2,c3,c4):
#         print(c.get())

# tk.Checkbutton(root,text='checkbox1',variable=c1,).pack()
# tk.Checkbutton(root,text='checkbox2',variable=c2,).pack()
# tk.Checkbutton(root,text='checkbox3',variable=c3,).pack()
# tk.Checkbutton(root,text='checkbox4',variable=c4,).pack()
# tk.Button(root,text='get value',command=get_value).pack()

# root.mainloop()


# import tkinter  as tk 
# my_w = tk.Tk()
# my_w.geometry("400x150")
# def my_upd():
#     i=0
#     if(c1_v.get()==1):i=i+1
#     if(c2_v.get()==1):i=i+1     
#     if(i>=1):
#         if(c1_v.get()!=1):c1.config(state='disabled')
#         if(c2_v.get()!=1):c2.config(state='disabled')
       
#     else:
#         c1.config(state='normal')
#         c2.config(state='normal')
# c1_v=tk.IntVar(my_w)    
# c1=tk.Checkbutton(my_w,text='Mele',command=my_upd,variable=c1_v)
# c1.grid(row=1,column=1)

# c2_v=tk.IntVar(my_w)
# c2=tk.Checkbutton(my_w,text='Female',command=my_upd,variable=c2_v)
# c2.grid(row=1,column=2)



# my_w.mainloop()



# import PySimpleGUI as psg
# #set the theme for the screen/window
# psg.theme('TealMono')
# #define layout
# layout=[[psg.Text('Choose your Bread',size=(20, 1), font='Lucida',justification='left')],
#         [psg.Radio('Whole Wheat','rd_bread', key ='Whole Wheat'), psg.Radio('Multigrain','rd_bread', key='Multigrain'),
#          psg.Radio('Normal','rd_bread', key='Normal'),psg.Radio('Stuffed','rd_bread', key='Stuffed'),psg.Radio('Healthy seeds','rd_bread', key='Healthy seeds')],
#         [psg.Text('Choose your Toppings',size=(20, 1), font='Lucida',justification='left')],
#         [psg.Checkbox('Pepperoni',key='Pepperoni'), psg.Checkbox('Mushroom',key='Mushroom'),
#          psg.Checkbox('Corn',key='Corn'),psg.Checkbox('Cherry Tomatoes',key='Cherry Tomatoes'),psg.Checkbox('Olives',key='Olives')],
#         [psg.Text('Choose your Sauces',size=(20, 1), font='Lucida',justification='left')],
#         [psg.Checkbox('Onion',key='Onion Sauce'), psg.Checkbox('Paprika',key='Paprika'),
#          psg.Checkbox('Schezwan',key='Schezwan'),psg.Checkbox('Tandoori',key='Tandoori')],
#         [psg.Button('SAVE', font=('Times New Roman',12)),psg.Button('CANCEL', font=('Times New Roman',12))]]
# #Define Window
# win =psg.Window('Make your Pizza',layout)
# #Read  values entered by user
# e,v=win.read()
# #close first window
# win.close()
# #access all the values and if selected add them to a string
# strx=""
# for val in v:
#     if win.FindElement(val).get()==True:
#         strx=strx+ " "+ val+","
# #display string in a popup         
# psg.popup('Custom Pizza',      
#             'Your chosen pizza will be made with', strx[0:len(strx)-1]) 


# import tkinter

# root = tkinter.Tk()
# root.title('Pack layout')

# lbl1 = tkinter.Label(root, width=20, height=5, bg='SteelBlue2')
# lbl1.pack(side=tkinter.LEFT, padx=10, pady=10)

# lbl2 = tkinter.Label(root, width=20, height=5, bg='SteelBlue3')
# lbl2.pack(side=tkinter.LEFT)

# lbl3 = tkinter.Label(root, width=20, height=5, bg='SteelBlue4')
# lbl3.pack(side=tkinter.LEFT, padx=10)

# root.geometry('+300+250')
# root.mainloop()





# import tkinter as tk

# # --- functions ---

# def on_click():
#     print('clicked')

# # --- main ---

# root = tk.Tk()

# img = tk.PhotoImage(data="iVBORw0KGgoAAAANSUhEUgAAACMAAAAjAQMAAAAkFyEaAAAABlBMVEX///8AAABVwtN+AAAAJ0lEQVQI12P4DwQPGCDkAQYGhgRSSDv+BjwkqabZ/2/AQ+LVi+QLAGveQwjt4H11AAAAAElFTkSuQmCC")

# for y in range(9):
#     for x in range(9):
#         button = tk.Button(root, image=img, command=on_click)
#         button.grid(row=y, column=x)

# root.mainloop()




# from tkinter import *

# class Colors(Frame):
#     def __init__(self):
#         Frame.__init__(self)
#         self._image = PhotoImage(file="r.gif")
#         self._imageLabel = Label(self, image=self._image)
#         self._imageLabel.grid()

#         self.master.title("Color Changer")
#         self.grid()

#         self.red = Scale(self, from_=0, to=255, label="Red", fg="red", )
#         self.red.grid(row=0, column=1)

#         self.green = Scale(self, from_=0, to=255, label="Green", fg='green')
#         self.green.grid(row=0, column=2)

#         self.blue = Scale(self, from_=0, to=255, label="Blue", fg="blue")
#         self.blue.grid(row=0, column=3)

#         self.button = Button(self, text="Change Colors", command=self.changeColor)
#         self.button.grid(row=1, column=2)

#     def changeColor(self):
#         red = self.red.get()
#         blue = self.blue.get()
#         green = self.green.get()
#         for y in range(self._image.height()):
#             for x in range(self._image.width()):
#                 self._image.put("#%02x%02x%02x" % (red,green,blue), (x, y))


#     Colors().mainloop()

# main()

# from tkinter import *
# from tkmacosx import Button, ColorVar, Marquee, Colorscale

# root = Tk()
# var = ColorVar(value='pink')
# root['bg'] = var
# m = Marquee(root, left_margin=30, bg= var, initial_delay=2000,
#             text='Welcome to tkmacosx!! Slide the slider to change color :)')
# m.pack(pady=(10,0))
# b = Button(root, text='Button', borderless=1, fg=var, bg='black')
# b.pack(pady=10)
# c = Colorscale(root, variable=var, value='hex', height=25, mousewheel=0)
# c.pack(pady=(0,10))

# root.mainloop()




# #Date Calendar
# from tkinter import *
# from tkinter import ttk

# root = Tk()
# root.geometry("200x150")
# root.resizable(False,False)

# frame = Frame(root)
# frame.pack()
# vlist = ["January up to December"]

# vlist2 = ["1 up to 31"]

# vlist3 = ["2015 up to 2040"]

# vlist4 = ["1 up to 30"]

# Combo = ttk.Combobox(frame, values = vlist, state='readonly')
# Combo.set("Pick a month")
# Combo.pack(padx = 5, pady = 5)

# Combo2 = ttk.Combobox(frame, values = vlist2, state='readonly')
# Combo2.set("Pick a day")
# Combo2.pack(padx = 5, pady = 5)

# Combo3 = ttk.Combobox(frame, values = vlist3, state='readonly')
# Combo3.set("Pick a year")
# Combo3.pack(padx = 5, pady = 5)

# def retrieve():
#     if Combo.get() == "April":
#         Combo2["values"] = (vlist4)
#     else:
#         Combo2["values"] = (vlist2)
    
#     print(Combo.get(), Combo2.get(), Combo3.get())

# Button = Button(frame, text = "Submit", command = retrieve)
# Button.pack(padx = 5, pady = 5)

# root.mainloop()




# # Upload picture to
# from tkinter import *
# from tkinter.ttk import *
# from tkinter.filedialog import askopenfile 
# import time

# ws = Tk()
# ws.title('PythonGuides')
# ws.geometry('400x200') 


# def open_file():
#     file_path = askopenfile(mode='r', filetypes=[('Image Files', '*jpeg')])
#     if file_path is not None:
#         pass


# def uploadFiles():
#     pb1 = Progressbar(
#         ws, 
#         orient=HORIZONTAL, 
#         length=300, 
#         mode='determinate'
#         )
#     pb1.grid(row=4, columnspan=3, pady=20)
#     for i in range(5):
#         ws.update_idletasks()
#         pb1['value'] += 20
#         time.sleep(1)
#     pb1.destroy()
#     Label(ws, text='File Uploaded Successfully!', foreground='green').grid(row=4, columnspan=3, pady=10)
        
    
    
# adhar = Label(
#     ws, 
#     text='Upload Government id in jpg format '
#     )
# adhar.grid(row=0, column=0, padx=10)

# adharbtn = Button(
#     ws, 
#     text ='Choose File', 
#     command = lambda:open_file()
#     ) 
# adharbtn.grid(row=0, column=1)

# dl = Label(
#     ws, 
#     text='Upload Driving License in jpg format '
#     )
# dl.grid(row=1, column=0, padx=10)

# dlbtn = Button(
#     ws, 
#     text ='Choose File ', 
#     command = lambda:open_file()
#     ) 
# dlbtn.grid(row=1, column=1)

# ms = Label(
#     ws, 
#     text='Upload Marksheet in jpg format '
#     )
# ms.grid(row=2, column=0, padx=10)

# msbtn = Button(
#     ws, 
#     text ='Choose File', 
#     command = lambda:open_file()
#     ) 
# msbtn.grid(row=2, column=1)

# upld = Button(
#     ws, 
#     text='Upload Files', 
#     command=uploadFiles
#     )
# upld.grid(row=3, columnspan=3, pady=10)



# ws.mainloop()
# import the necessary packages

# from tkinter import *
# from PIL import Image
# from PIL import ImageTk
# import tkFileDialog
# import cv2
# def select_image():
# 	# grab a reference to the image panels
# 	global panelA, panelB
# 	# open a file chooser dialog and allow the user to select an input
# 	# image
# 	path = tkFileDialog.askopenfilename()
# # ensure a file path was selected
# 	if len(path) > 0:
# 		# load the image from disk, convert it to grayscale, and detect
# 		# edges in it
# 		image = cv2.imread(path)
# 		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 		edged = cv2.Canny(gray, 50, 100)
# 		# OpenCV represents images in BGR order; however PIL represents
# 		# images in RGB order, so we need to swap the channels
# 		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# 		# convert the images to PIL format...
# 		image = Image.fromarray(image)
# 		edged = Image.fromarray(edged)
# 		# ...and then to ImageTk format
# 		image = ImageTk.PhotoImage(image)
# 		edged = ImageTk.PhotoImage(edged)
# # if the panels are None, initialize them
# 		if panelA is None or panelB is None:
# 			# the first panel will store our original image
# 			panelA = Label(image=image)
# 			panelA.image = image
# 			panelA.pack(side="left", padx=10, pady=10)
# 			# while the second panel will store the edge map
# 			panelB = Label(image=edged)
# 			panelB.image = edged
# 			panelB.pack(side="right", padx=10, pady=10)
# 		# otherwise, update the image panels
# 		else:
# 			# update the pannels
# 			panelA.configure(image=image)
# 			panelB.configure(image=edged)
# 			panelA.image = image
# 			panelB.image = edged
# # initialize the window toolkit along with the two image panels
# root = Tk()
# panelA = None
# panelB = None
# # create a button, then when pressed, will trigger a file chooser
# # dialog and allow the user to select an input image; then add the
# # button the GUI
# btn = Button(root, text="Select an image", command=select_image)
# btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
# # kick off the GUI
# root.mainloop()



# try:
#     import os
#     import tkinter as tk
#     import tkinter.ttk as ttk
#     from tkinter import filedialog
# except ImportError:
#     import Tkinter as tk
#     import ttk
#     import tkFileDialog as filedialog
 
 
# root = tk.Tk()
 
# style = ttk.Style(root)
# style.theme_use("clam")
 
 
# def c_open_file_old():
#     rep = filedialog.askopenfilenames(
#     	parent=root,
#     	initialdir='/',
#     	initialfile='tmp',
#     	filetypes=[
#     		("PNG", "*.png"),
#     		("JPEG", "*.jpg"),
#     		("All files", "*")])
#     print(rep)
#     try:
# 	    os.startfile(rep[0])
#     except IndexError:
#         print("No file selected")
 
# ttk.Button(root, text="Open files", command=c_open_file_old).grid(row=1, column=0, padx=4, pady=4, sticky='ew')
 
# root.mainloop()







from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

root = Tk()
root.geometry("550x600+300+150")
root.resizable(width=True, height=True)

def openfn():
    filename = filedialog.askopenfilename(title='open')
    print(filename)
    return filename
def open_img():
    x = openfn()
    img = Image.open(x)
    img = img.resize((400, 400), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()
def save_img():
    x = openfn().waitKey(0)
    #Check if user hits ‘c’ or ‘g’ key
    if( k == ord('c') ):
        x.imwrite('color.jpg', color_img )
        print("Image is saved color")
        x.destroyAllWindows()
    if( k == ord('g') ):
        x.imwrite('gray.jpg', gray_img )
        print("Image saved in grayscale")
        x.destroyAllWindows()

btn = Button(root, text='open image', command=open_img).pack()
bbb = Button(root, text='save image', command=save_img).pack()


root.mainloop()



import tkinter as tk
from tkinter import ttk

root = tk.Tk()

b1 = tk.Button(root, text='tk.Button', borderwidth=0)
b1.pack()

s = ttk.Style(root)
s.theme_use('clam')
s.configure('flat.TButton', borderwidth=0)
# s.configure('flat.TButton', relief='flat') gives the same result

b2 = ttk.Button(root, style='flat.TButton', text='ttk.Button')
b2.pack()

root.mainloop()






# # VideoCapture

# from tkinter import *
# from PIL import ImageTk, Image
# import cv2

# root2=Tk()
# root2.title('Video preview')


# #Layout of display
# topFrame =Frame(root2,width=100,height=100)
# topFrame.grid(rowspan=2)



# #topFrame
# lmain = Label(topFrame,width=600,height=500)
# lmain.grid()

# cap=cv2.VideoCapture(0)


# def video_stream():


#     _, frame = cap.read()
  

   
#     cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
#     img = Image.fromarray(cv2image)
#     imgtk = ImageTk.PhotoImage(image=img)
#     lmain.imgtk = imgtk
#     lmain.configure(image=imgtk)
#     lmain.after(1, video_stream)


# video_stream()

   
# root2.mainloop()







#capture

import cv2
#Reading images in color and grayscale

color_img = cv2.imread('Mayuyu.jpg')
gray_img = cv2.imread('Mayuyu.jpg',0)
#Displaying the image
cv2.imshow('Cat image', color_img)
#Storing the key pressed by user 
k = cv2.waitKey(0)
#Check if user hits ‘c’ or ‘g’ key
if( k == ord('c') ):
  cv2.imwrite('color.jpg', color_img )
  print("Image is saved color")
  cv2.destroyAllWindows()
if( k == ord('g') ):
  cv2.imwrite('gray.jpg', gray_img )
  print("Image saved in grayscale")
  cv2.destroyAllWindows()

