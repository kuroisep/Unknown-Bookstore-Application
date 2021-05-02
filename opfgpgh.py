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






# from tkinter import *
# def shift():
#     x1,y1,x2,y2 = canvas.bbox("marquee")
#     if(x2<0 or y1<0): #reset the coordinates
#         x1 = canvas.winfo_width()
#         y1 = canvas.winfo_height()//2
#         canvas.coords("marquee",x1,y1)
#     else:
#         canvas.move("marquee", -2, 0)
#     canvas.after(1000//fps,shift)
# ############# Main program ###############
# root=Tk()
# root.title('Move Text')
# canvas=Canvas(root,bg='#7242f5')
# canvas.pack(fill=BOTH, expand=1)
# text_var=" ______ Welcome to the land of bookS ______"
# text=canvas.create_text(0,-2000,text=text_var,font=('Times New Roman',20,'bold'),fill='white',tags=("marquee",),anchor='w')
# x1,y1,x2,y2 = canvas.bbox("marquee")
# width = x2-x1
# height = y2-y1
# canvas['width']=width
# canvas['height']=height
# fps=40    #Change the fps to make the animation faster/slower
# shift()
# root.mainloop()



import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import pandas as pd

# initalise the tkinter GUI
root = tk.Tk()

root.geometry("500x500") # set the root dimensions
root.pack_propagate(False) # tells the root to not let the widgets inside it determine its size.
# root.resizable(0, 0) # makes the root window fixed in size.

# Frame for TreeView
frame1 = tk.LabelFrame(root, text="Excel Data")
frame1.place( height=500, width=500)

# Frame for open file dialog
file_frame = tk.LabelFrame(root, text="Open File")
file_frame.place(height=100, width=400, rely=0.65, relx=0)

# Buttons
button1 = tk.Button(file_frame, text="Browse A File", command=lambda: File_dialog())
button1.place(rely=0.65, relx=0.50)

button2 = tk.Button(file_frame, text="Load File", command=lambda: Load_excel_data())
button2.place(rely=0.65, relx=0.30)

# The file/file path text
label_file = ttk.Label(file_frame, text="No File Selected")
label_file.place(rely=0, relx=0)


## Treeview Widget
tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).

treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview) # command means update the yaxis view of the widget
treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview) # command means update the xaxis view of the widget
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget


def File_dialog():
    """This Function will open the file explorer and assign the chosen file path to label_file"""
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select A File",
                                          filetype=(("xlsx files", "*.xlsx"),("All Files", "*.*")))
    label_file["text"] = filename
    return None


def Load_excel_data():
    """If the file selected is valid this will load the file into the Treeview"""
    file_path = label_file["text"]
    try:
        excel_filename = r"{}".format(file_path)
        if excel_filename[-4:] == ".csv":
            df = pd.read_csv(excel_filename,engine='python')
        else:
            df = pd.read_excel(excel_filename)

    except ValueError:
        tk.messagebox.showerror("Information", "The file you have chosen is invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information", f"No such file as {file_path}")
        return None

    clear_data()
    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column) # let the column heading = column name

    df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
    for row in df_rows:
        tv1.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
    return None


def clear_data():
    tv1.delete(*tv1.get_children())
    return None


root.mainloop()