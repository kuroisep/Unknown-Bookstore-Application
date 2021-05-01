# import tkinter as tk
# from tkinter import ttk
   
  
# Num_Vertical = ("\nA\nB\nC\nD\nE\nF\nG\n\
# H\nI\nJ\nK\nL\nM\nN\nO\nP\nQ\nR\nS\nT\n\
# U\nV\nW\nX\nY\nZ")
# Num_Horizontal = ("A  B  C  D  E  F  G  H \
# I  J  K  L  M  N  O  P  Q  R  S  T  U  V \
# W  X  Y  Z")
   
# window = tk.Tk()
# window.geometry("250x200+800+400")
# window.overrideredirect(1)


# style = ttk.Style(window)
# # Import the tcl file
# window.tk.call('source', 'UnknownShop/azure-dark.tcl')

# # Set the theme with the theme_use method
# style.theme_use('azure-dark')
# style.configure('flat.TButton', borderwidth=0)


# SVBar = ttk.Scrollbar(window)
# SVBar.pack (side = tk.RIGHT, 
#             fill = "y")
   
# SHBar = ttk.Scrollbar(window, 
#                      orient = tk.HORIZONTAL)
# SHBar.pack (side = tk.BOTTOM, 
#             fill = "x")
   
# TBox = tk.Text(window, 
#                height = 500, 
#                width = 500,
#                yscrollcommand = SVBar.set,
#                xscrollcommand = SHBar.set, 
#                wrap = "none")
  
# TBox = tk.Text(window,
#                height = 500,
#                width = 500,
#                yscrollcommand = SVBar.set, 
#                xscrollcommand = SHBar.set, 
#                wrap = "none")
  
# TBox.pack(expand = 0, fill = tk.BOTH)
   
# TBox.insert(tk.END, Num_Horizontal)
# TBox.insert(tk.END, Num_Vertical)
   
# SHBar.config(command = TBox.xview)
# SVBar.config(command = TBox.yview)
   
# window.mainloop()
# import tkinter
# import tkinter as tk  
# from tkinter import ttk  
# from tkinter import StringVar, Tk, scrolledtext  
# from tkinter.ttk import Label
# # win = tk.Tk()  
# # win.title("Python GUI App")  
# # ttk.Label(win, text="This is Scrolled Text Area").grid(column=0,row=0)  
# # #Create Scrolled Text  
# # scrolW=30  
# # scrolH=2  
# # scr=scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)  
# # scr.grid(column=0, columnspan=3)  
# # #Calling Main()  
# # win.mainloop()


# root = Tk()
# delay = 50
# label_var = StringVar()
# label = tk.Label(root, textvariable=label_var, height=10)
# num = 0

# def scroll():
#     global num
#     roll_text = list(message) # Edit: deleted this line
#     num = num + 1
#     label_var.set(roll_text[1:num]) # Edit: changed roll_text to message
#     root.after(delay, scroll)

# message = ' This message should be scrolling left to right. '
# while True :
#     scroll()
# label.pack()
# root.mainloop()

from tkinter import *
def shift():
    x1,y1,x2,y2 = canvas.bbox("marquee")
    if(x2<0 or y1<0): #reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords("marquee",x1,y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000//fps,shift)
############# Main program ###############
root=Tk()
root.title('Move Text')
canvas=Canvas(root,bg='#7242f5')
canvas.pack(fill=BOTH, expand=1)
text_var=" ______ Welcome to the land of bookS ______"
text=canvas.create_text(0,-2000,text=text_var,font=('Times New Roman',20,'bold'),fill='white',tags=("marquee",),anchor='w')
x1,y1,x2,y2 = canvas.bbox("marquee")
width = x2-x1
height = y2-y1
canvas['width']=width
canvas['height']=height
fps=40    #Change the fps to make the animation faster/slower
shift()
root.mainloop()