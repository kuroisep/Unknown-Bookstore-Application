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