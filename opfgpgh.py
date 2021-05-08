# # # # # # import tkinter as tk
# # # # # # from tkinter import ttk
   
  
# # # # # # Num_Vertical = ("\nA\nB\nC\nD\nE\nF\nG\n\
# # # # # # H\nI\nJ\nK\nL\nM\nN\nO\nP\nQ\nR\nS\nT\n\
# # # # # # U\nV\nW\nX\nY\nZ")
# # # # # # Num_Horizontal = ("A  B  C  D  E  F  G  H \
# # # # # # I  J  K  L  M  N  O  P  Q  R  S  T  U  V \
# # # # # # W  X  Y  Z")
   
# # # # # # window = tk.Tk()
# # # # # # window.geometry("250x200+800+400")
# # # # # # window.overrideredirect(1)


# # # # # # style = ttk.Style(window)
# # # # # # # Import the tcl file
# # # # # # window.tk.call('source', 'UnknownShop/azure-dark.tcl')

# # # # # # # Set the theme with the theme_use method
# # # # # # style.theme_use('azure-dark')
# # # # # # style.configure('flat.TButton', borderwidth=0)


# # # # # # SVBar = ttk.Scrollbar(window)
# # # # # # SVBar.pack (side = tk.RIGHT, 
# # # # # #             fill = "y")
   
# # # # # # SHBar = ttk.Scrollbar(window, 
# # # # # #                      orient = tk.HORIZONTAL)
# # # # # # SHBar.pack (side = tk.BOTTOM, 
# # # # # #             fill = "x")
   
# # # # # # TBox = tk.Text(window, 
# # # # # #                height = 500, 
# # # # # #                width = 500,
# # # # # #                yscrollcommand = SVBar.set,
# # # # # #                xscrollcommand = SHBar.set, 
# # # # # #                wrap = "none")
  
# # # # # # TBox = tk.Text(window,
# # # # # #                height = 500,
# # # # # #                width = 500,
# # # # # #                yscrollcommand = SVBar.set, 
# # # # # #                xscrollcommand = SHBar.set, 
# # # # # #                wrap = "none")
  
# # # # # # TBox.pack(expand = 0, fill = tk.BOTH)
   
# # # # # # TBox.insert(tk.END, Num_Horizontal)
# # # # # # TBox.insert(tk.END, Num_Vertical)
   
# # # # # # SHBar.config(command = TBox.xview)
# # # # # # SVBar.config(command = TBox.yview)
   
# # # # # # window.mainloop()
# # # # # # import tkinter
# # # # # # import tkinter as tk  
# # # # # # from tkinter import ttk  
# # # # # # from tkinter import StringVar, Tk, scrolledtext  
# # # # # # from tkinter.ttk import Label
# # # # # # # win = tk.Tk()  
# # # # # # # win.title("Python GUI App")  
# # # # # # # ttk.Label(win, text="This is Scrolled Text Area").grid(column=0,row=0)  
# # # # # # # #Create Scrolled Text  
# # # # # # # scrolW=30  
# # # # # # # scrolH=2  
# # # # # # # scr=scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)  
# # # # # # # scr.grid(column=0, columnspan=3)  
# # # # # # # #Calling Main()  
# # # # # # # win.mainloop()


# # # # # # root = Tk()
# # # # # # delay = 50
# # # # # # label_var = StringVar()
# # # # # # label = tk.Label(root, textvariable=label_var, height=10)
# # # # # # num = 0

# # # # # # def scroll():
# # # # # #     global num
# # # # # #     roll_text = list(message) # Edit: deleted this line
# # # # # #     num = num + 1
# # # # # #     label_var.set(roll_text[1:num]) # Edit: changed roll_text to message
# # # # # #     root.after(delay, scroll)

# # # # # # message = ' This message should be scrolling left to right. '
# # # # # # while True :
# # # # # #     scroll()
# # # # # # label.pack()
# # # # # # root.mainloop()



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
canvas=Canvas(root,bg='#724287')
canvas.pack(fill=BOTH, expand=1)
text_var=" ______|   Welcome to the land of bookS   |______" 

text=canvas.create_text(0,-2000,text=text_var,font=('Times New Roman',20,'bold'),fill='white',tags=("marquee",),anchor='w')
x1,y1,x2,y2 = canvas.bbox("marquee")
width = x2-x1
height = y2-y1
canvas['width']=width
canvas['height']=height
fps=40    #Change the fps to make the animation faster/slower
shift()
root.mainloop()


# from tkinter import *

# class AllTkinterWidgets:
#     def __init__(self, master):
#         frame = Frame(master, width=500, height=400, bd=1)
#         frame.pack()

#         iframe5 = Frame(frame, bd=2, relief=RAISED)
#         iframe5.pack(expand=1, fill=X, pady=10, padx=5)
#         c = Canvas(iframe5, bg='white', width=340, height=100)
#         c.pack()
#         for i in range(25):
#             c.create_oval(5+(4*i),5+(3*i),(5*i)+60,(i)+60, fill='gray70')
#         c.create_text(260, 80, text='Canvas', font=('verdana', 10, 'bold'))
#         iframe5.pack(expand=1, fill=X, pady=10, padx=5)



    
# root = Tk()
# #root.option_add('*font', ('verdana', 10, 'bold'))
# all = AllTkinterWidgets(root)
# root.title('Tkinter Widgets')
# root.mainloop()
           


# # # # # import tkinter as tk
# # # # # from tkinter import filedialog, messagebox, ttk

# # # # # import pandas as pd

# # # # # # initalise the tkinter GUI
# # # # # root = tk.Tk()

# # # # # root.geometry("500x500") # set the root dimensions
# # # # # root.pack_propagate(False) # tells the root to not let the widgets inside it determine its size.
# # # # # # root.resizable(0, 0) # makes the root window fixed in size.

# # # # # # Frame for TreeView
# # # # # frame1 = tk.LabelFrame(root, text="Excel Data")
# # # # # frame1.place( height=500, width=500)

# # # # # # Frame for open file dialog
# # # # # file_frame = tk.LabelFrame(root, text="Open File")
# # # # # file_frame.place(height=100, width=400, rely=0.65, relx=0)

# # # # # # Buttons
# # # # # button1 = tk.Button(file_frame, text="Browse A File", command=lambda: File_dialog())
# # # # # button1.place(rely=0.65, relx=0.50)

# # # # # button2 = tk.Button(file_frame, text="Load File", command=lambda: Load_excel_data())
# # # # # button2.place(rely=0.65, relx=0.30)

# # # # # # The file/file path text
# # # # # label_file = ttk.Label(file_frame, text="No File Selected")
# # # # # label_file.place(rely=0, relx=0)


# # # # # ## Treeview Widget
# # # # # tv1 = ttk.Treeview(frame1)
# # # # # tv1.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).

# # # # # treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview) # command means update the yaxis view of the widget
# # # # # treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview) # command means update the xaxis view of the widget
# # # # # tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
# # # # # treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
# # # # # treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget


# # # # # def File_dialog():
# # # # #     """This Function will open the file explorer and assign the chosen file path to label_file"""
# # # # #     filename = filedialog.askopenfilename(initialdir="/",
# # # # #                                           title="Select A File",
# # # # #                                           filetype=(("xlsx files", "*.xlsx"),("All Files", "*.*")))
# # # # #     label_file["text"] = filename
# # # # #     return None


# # # # # def Load_excel_data():
# # # # #     """If the file selected is valid this will load the file into the Treeview"""
# # # # #     file_path = label_file["text"]
# # # # #     try:
# # # # #         excel_filename = r"{}".format(file_path)
# # # # #         if excel_filename[-4:] == ".csv":
# # # # #             df = pd.read_csv(excel_filename)
# # # # #         else:
# # # # #             df = pd.read_excel(excel_filename)

# # # # #     except ValueError:
# # # # #         tk.messagebox.showerror("Information", "The file you have chosen is invalid")
# # # # #         return None
# # # # #     except FileNotFoundError:
# # # # #         tk.messagebox.showerror("Information", f"No such file as {file_path}")
# # # # #         return None

# # # # #     clear_data()
# # # # #     tv1["column"] = list(df.columns)
# # # # #     tv1["show"] = "headings"
# # # # #     for column in tv1["columns"]:
# # # # #         tv1.heading(column, text=column) # let the column heading = column name

# # # # #     df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
# # # # #     for row in df_rows:
# # # # #         tv1.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
# # # # #     return None


# # # # # def clear_data():
# # # # #     tv1.delete(*tv1.get_children())
# # # # #     return None


# # # # # root.mainloop()

# # # # import tkinter as tk
# # # # import time

# # # # class App(tk.Tk):

# # # #     def __init__(self,*args, **kwargs):
# # # #         tk.Tk.__init__(self, *args, **kwargs)
# # # #         # ... YOUR widgets here ...
# # # #         self.T = tk.Text(self, height=25, width=80)
# # # #         self.S = tk.Scrollbar(self)
# # # #         self.T.config(yscrollcommand=self.S.set)
# # # #         self.T.pack(side=tk.LEFT, fill=tk.Y)
# # # #         self.S.config(command=self.T.yview)
# # # #         self.S.pack(side=tk.RIGHT, fill=tk.Y)
# # # #         self.updateWidgets()

# # # #     def updateWidgets(self):
# # # #         with open('realTimeUpdatingTextWidget_Cg.py') as f:
# # # #             newText = f.read()
# # # #         # ... YOUR code for updating the Widgets ...
# # # #         self.T.delete('1.0', tk.END)
# # # #         self.T.insert(tk.END, newText)
# # # #         self.after(1000, self.updateWidgets)

# # # # app = App()
# # # # app.mainloop()
# # # import sys
# # # import time
# # # import multiprocessing as mp
# # # import multiprocessing.queues as mpq
# # # from threading import Thread
# # # from tkinter import *


# # # class StdoutQueue(mpq.Queue):

# # #     def __init__(self, *args, **kwargs):
# # #         ctx = mp.get_context()
# # #         super(StdoutQueue, self).__init__(*args, **kwargs, ctx=ctx)

# # #     def write(self,msg):
# # #         self.put(msg)

# # #     def flush(self):
# # #         sys.__stdout__.flush()
        
        
# # # def text_catcher(text_widget,queue):
# # #     while True:
# # #         text_widget.insert(END, queue.get())


# # # def test_child(q):
# # #     sys.stdout = q
# # #     print('child running')


# # # def test_parent(q):
# # #     sys.stdout = q
# # #     print('parent running')
# # #     time.sleep(5.)
# # #     mp.Process(target=test_child,args=(q,)).start()


# # # if __name__ == '__main__':
# # #     gui_root = Tk()
# # #     gui_txt = Text(gui_root)
# # #     gui_txt.pack()
# # #     q = StdoutQueue()
# # #     gui_btn = Button(gui_root, text='Test', command=lambda: test_parent(q),)
# # #     gui_btn.pack()

# # #     monitor = Thread(target=text_catcher, args=(gui_txt, q))
# # #     monitor.daemon = True
# # #     monitor.start()

# # #     gui_root.mainloop()

# # from tkinter import *
# # from tkFont import *

# # import random
# # from tkinter.font import Font

# # root = Tk()

# # fixed_width = Font(family = 'Courier', size = 10)
# # textbox = Text(root, font = fixed_width, width = 40, height = 20)
# # textbox.pack()

# # def blank_matrix(sizeX, sizeY, fillchar):

# #     sizeX += 1
# #     sizeY += 1

# #     letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# #     letter_matrix = []

# #     for row in range(1,sizeY):
# #         line = []
# #         for _column in range(1, sizeX):
# #             if fillchar == 'letters':
# #                 letter = random.randrange(0, 26)
# #                 line.append(letters[letter])
# #             else:
# #                 line.append(fillchar)
# #         letter_matrix.append(line)

# #     return letter_matrix
    
# # def print_matrix(matrix):
# #     textbox.delete(1.0, END)
# #     for line in matrix:
# #         #print ' '.join(line)
# #         line = ' '.join(line) + '\n'
# #         textbox.insert(END, line)

# # def insert_word(word, print_dir, x, y, matrix):

# #     word = word.upper()
# #     word = list(word)
    
# #     print_dirs = dict()
# #     print_dirs['e'] = (1,0)
# #     print_dirs['ne'] = (1,-1)
# #     print_dirs['n'] = (0,-1)
# #     print_dirs['nw'] = (-1,-1)
# #     print_dirs['w'] = (-1, 0)
# #     print_dirs['sw'] = (-1, 1)
# #     print_dirs['s'] = (0, 1)
# #     print_dirs['se'] = (1,1)
         
# #     x_plus, y_plus = print_dirs[print_dir]
    
# #     for i in range(0, len(word)):
# #         matrix[y + (i * y_plus)][x + (i * x_plus)] = word[i]
       
# #     return matrix

# # directions = ['e', 'ne', 'n', 'nw', 'w', 'sw', 's', 'se']
# # for direction in directions:
# #     print (direction)
# #     matrix = blank_matrix(20, 20, '.')
# #     matrix = insert_word('test_word', direction, 10, 10, matrix)
# #     print_matrix(matrix)
    
# # root.mainloop()
# import time
# import datetime
# import tkinter as tk
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



# import tkinter as tk
# from tkinter import filedialog, messagebox, ttk

# import pandas as pd

# # initalise the tkinter GUI
# root = tk.Tk()

# root.geometry("500x500") # set the root dimensions
# root.pack_propagate(False) # tells the root to not let the widgets inside it determine its size.
# # root.resizable(0, 0) # makes the root window fixed in size.

# # Frame for TreeView
# frame1 = tk.LabelFrame(root, text="Excel Data")
# frame1.place( height=500, width=500)

# # Frame for open file dialog
# file_frame = tk.LabelFrame(root, text="Open File")
# file_frame.place(height=100, width=400, rely=0.65, relx=0)

# # Buttons
# button1 = tk.Button(file_frame, text="Browse A File", command=lambda: File_dialog())
# button1.place(rely=0.65, relx=0.50)

# button2 = tk.Button(file_frame, text="Load File", command=lambda: Load_excel_data())
# button2.place(rely=0.65, relx=0.30)

# # The file/file path text
# label_file = ttk.Label(file_frame, text="No File Selected")
# label_file.place(rely=0, relx=0)


# ## Treeview Widget
# tv1 = ttk.Treeview(frame1)
# tv1.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).

# treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview) # command means update the yaxis view of the widget
# treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview) # command means update the xaxis view of the widget
# tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
# treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
# treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget


# def File_dialog():
#     """This Function will open the file explorer and assign the chosen file path to label_file"""
#     filename = filedialog.askopenfilename(initialdir="/",
#                                           title="Select A File",
#                                           filetype=(("xlsx files", "*.xlsx"),("All Files", "*.*")))
#     label_file["text"] = filename
#     return None


# def Load_excel_data():
#     """If the file selected is valid this will load the file into the Treeview"""
#     file_path = label_file["text"]
#     try:
#         excel_filename = r"{}".format(file_path)
#         if excel_filename[-4:] == ".csv":
#             df = pd.read_csv(excel_filename,engine='python')
#         else:
#             df = pd.read_excel(excel_filename)

#     except ValueError:
#         tk.messagebox.showerror("Information", "The file you have chosen is invalid")
#         return None
#     except FileNotFoundError:
#         tk.messagebox.showerror("Information", f"No such file as {file_path}")
#         return None

#     clear_data()
#     tv1["column"] = list(df.columns)
#     tv1["show"] = "headings"
#     for column in tv1["columns"]:
#         tv1.heading(column, text=column) # let the column heading = column name

#     df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
#     for row in df_rows:
#         tv1.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
#     return None


# def clear_data():
#     tv1.delete(*tv1.get_children())
#     return None


# class MainApp(tk.Tk):

#     def __init__(self, *args, **kwargs):
#         tk.Tk.__init__(self, *args, **kwargs)

#         container = tk.Frame(self)
#         container.pack(side="top", fill="both", expand=True)
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)

#         self.timevar = tk.StringVar()  # Added.

#         self.frames = {}
#         for F in (MainPage, Page1, Help):
#             page_name = F.__name__
#             frame = F(parent=container, controller=self)
#             self.frames[page_name] = frame
#             frame.grid(row=0, column=0, columnspan=12,sticky="nsew")
#             frame.grid_columnconfigure(0, weight=1)
#             frame.grid_columnconfigure(1, weight=1)
#             frame.grid_columnconfigure(2, weight=1)
#             frame.grid_columnconfigure(3, weight=1)
#             frame.grid_columnconfigure(4, weight=1)
#             frame.grid_columnconfigure(5, weight=1)
#             frame.grid_columnconfigure(6, weight=1)
#             frame.grid_columnconfigure(7, weight=1)
#             frame.grid_columnconfigure(8, weight=1)
#             frame.grid_columnconfigure(9, weight=1)
#             frame.grid_columnconfigure(10, weight=1)
#             frame.grid_columnconfigure(11, weight=1)

#         # Synchronize with the computer's clock.
#         snooze = (1000000 - datetime.datetime.now().microsecond) / 1000000.
#         if snooze > 0:
#             time.sleep(snooze)  # Sleep until next whole second.
#         self.clock()  # Starts string variable update process.

#         self.show_frame("MainPage")

#     def show_frame(self, page_name):
#         frame = self.frames[page_name]
#         frame.tkraise()

#     # Additional method added.
#     def clock(self):
#         self.timevar.set(datetime.datetime.now().strftime("Time: %H:%M:%S"))
#         self.after(1000, self.clock)  # Update every second (1000 millsecs)


# class MainPage(tk.Frame):

#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller

#         # line 0
#         label00 = tk.Label(self, text='00', height=2)
#         label00.configure(relief='raised')
#         label00.grid(row=0, column=0, sticky='nsew', columnspan=12)
#         # line 1
#         label10 = tk.Label(self, text='10')
#         label10.configure(relief='raised')
#         label10.grid(row=1, column=0, sticky='nsew')
#         label11 = tk.Label(self, text='LOGO')
#         label11.configure(relief='raised')
#         label11.grid(row=1, column=1, sticky='nsew', columnspan=4, rowspan=2)
#         label12 = tk.Label(self, text='12')
#         label12.configure(relief='raised')
#         label12.grid(row=1, column=5, sticky='nsew')
#         label13 = tk.Label(self, text='TITLE')
#         label13.configure(relief='raised')
#         label13.grid(row=1, column=6, sticky='nsew', columnspan=5)
#         label14 = tk.Label(self, text='14')
#         label14.configure(relief='raised')
#         label14.grid(row=1, column=11, sticky='nsew')
#         # line 2
#         label20 = tk.Label(self, text='20')
#         label20.configure(relief='raised')
#         label20.grid(row=2, column=0, sticky='nsew')
#         label21 = tk.Label(self, text='21')
#         label21.configure(relief='raised')
#         label21.grid(row=2, column=5, sticky='nsew')
#         label22 = tk.Label(self, text='Desc')
#         label22.configure(relief='raised')
#         label22.grid(row=2, column=6, sticky='nsew', columnspan=5)
#         label23 = tk.Label(self, text='23')
#         label23.configure(relief='raised')
#         label23.grid(row=2, column=11, sticky='nsew')
#         # line 3
#         label30 = tk.Label(self, text='30', height=2)
#         label30.configure(relief='raised')
#         label30.grid(row=3, column=0, sticky='nsew', columnspan=12)
#         #line 4
#         label40 = tk.Label(self, text='40', width=10)
#         label40.configure(relief='raised')
#         label40.grid(row=4, column=0, sticky='nsew')
#         label41 = tk.Label(self, text='STATUS', font=("Helvetica", 16), justify='center', fg="blue")
#         label41.configure(relief='raised')
#         label41.grid(row=4, column=1, columnspan=10)
#         label42 = tk.Label(self, text='42', width=10)
#         label42.configure(relief='raised')
#         label42.grid(row=4, column=11, sticky='nsew')
#         #line 5
#         label50 = tk.Label(self, text='50', height=2)
#         label50.configure(relief='raised')
#         label50.grid(row=5, column=0, columnspan=12, sticky="nsew")
#         #line 6
#         label60 = tk.Label(self, text='60', height=2)
#         label60.configure(relief='raised')
#         label60.grid(row=6, column=0, sticky='nsew')
#         buttonauto = tk.Button(self, text="PAGE1", font=("Helvetica", 16), justify='center', width=40, height=5,
#                               command=lambda: controller.show_frame("Page1"))
#         buttonauto.grid(row=6, column=1, columnspan=4)
#         label61 = tk.Label(self, text='61', height=2)
#         label61.configure(relief='raised')
#         label61.grid(row=6, column=5, sticky='nsew')
#         label62 = tk.Label(self, text='62', height=2)
#         label62.configure(relief='raised')
#         label62.grid(row=6, column=6, sticky='nsew')
#         buttoncam = tk.Button(self, text="HELP",font=("Helvetica", 16), justify='center', width=40, height=5,
#                               command=lambda: controller.show_frame("Help"))
#         buttoncam.grid(row=6 , column=7, columnspan=4)
#         label63 = tk.Label(self, text='63', height=2)
#         label63.configure(relief='raised')
#         label63.grid(row=6, column=11, sticky='nsew')
#         # line 7
#         label70 = tk.Label(self, text='70', height=2)
#         label70.configure(relief='raised')
#         label70.grid(row=7, column=0, sticky='nsew', columnspan=12)

#         #line 13
#         label13 = tk.Label(self, text='', height=2)
#         label13.configure(relief='raised')
#         label13.grid(row=13, column=0, columnspan=12, sticky="nsew")
#         #line 14
#         label14 = tk.Label(self, text='', width=10)
#         label14.grid(row=14, column=0, sticky='w')
#         buttonhlp = tk.Button(self, text="Help", width=20, height = 3,
#                               command=lambda: controller.show_frame("Help"))
#         buttonhlp.grid(row=14, column=1, columnspan=4)
#         label14 = tk.Label(self, text='')
#         label14.grid(row=14, column=5, columnspan=2)
#         buttonquit = tk.Button(self, text="Quit", width=20, height = 3, command=close_window)
#         buttonquit.grid(row=14, column=7, columnspan=4)
#         label14 = tk.Label(self, text='', width=10)
#         label14.grid(row=14, column=11, sticky='e')
#         #line 15
#         label15 = tk.Label(self, text='', height=5)
#         label15.grid(row=15, column=0, columnspan=12, sticky="nsew")


# class Page1(tk.Frame):

#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller

#         #line 0
# #        label00 = tk.Label(self, text='PAGE1', height=2)
#         label00 = tk.Label(self, textvariable=controller.timevar, height=2)
#         label00.configure(relief='raised')
#         label00.grid(row=13, column=0, columnspan=12, sticky="nsew")
#         #line 1
#         label10 = tk.Label(self, text='', width=10)
#         label10.grid(row=14, column=0, sticky='w')
#         buttonback = tk.Button(self, text="Back", width=20, height = 3,
#                               command=lambda: controller.show_frame("MainPage"))
#         buttonback.grid(row=14, column=1, columnspan=4)
#         label10= tk.Label(self, text='')
#         label10.grid(row=14, column=5, columnspan=2)
#         buttonquit = tk.Button(self, text="Quit", width=20, height = 3, command=close_window)
#         buttonquit.grid(row=14, column=7, columnspan=4)
#         label10 = tk.Label(self, text='', width=10)
#         label10.grid(row=14, column=11, sticky='e')
#         #line 2
#         label20 = tk.Label(self, text='', height=5)
#         label20.grid(row=15, column=0, columnspan=12, sticky="nsew")

# class Help(tk.Frame):

#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller

#         #line 0
#         label00 = tk.Label(self, text='HELP', height=2)
#         label00.configure(relief='raised')
#         label00.grid(row=13, column=0, columnspan=12, sticky="nsew")
#         #line 1
#         label10 = tk.Label(self, text='', width=10)
#         label10.grid(row=14, column=0, sticky='w')
#         buttonback = tk.Button(self, text="Back", width=20, height = 3,
#                               command=lambda: controller.show_frame("MainPage"))
#         buttonback.grid(row=14, column=1, columnspan=4)
#         label10= tk.Label(self, text='')
#         label10.grid(row=14, column=5, columnspan=2)
#         buttonquit = tk.Button(self, text="Quit", width=20, height = 3, command=close_window)
#         buttonquit.grid(row=14, column=7, columnspan=4)
#         label10 = tk.Label(self, text='', width=10)
#         label10.grid(row=14, column=11, sticky='e')
#         #line 2
#         label20 = tk.Label(self, text='', height=5)
#         label20.grid(row=15, column=0, columnspan=12, sticky="nsew")


# def close_window ():
#     app.destroy()


# if __name__ == "__main__":
#     app = MainApp()

#     app.overrideredirect(True)
#     app.geometry("{0}x{1}+0+0".format(app.winfo_screenwidth(), app.winfo_screenheight()))
#     app.focus_set()  # <-- move focus to this widget


#     app.mainloop()

# from tkinter import *

# class Output:
#     def __init__(self,master):
#         self.u=Text(master,width=40)
#         self.u.grid(row=0,column=0)
#         self.v=Button(master,text="Add text",command=Write)
#         self.v.grid(row=1,column=0)

# def Write(self):
#     self.u.insert(1.0,"Meh")

# root=Tk()
# output=Output(root)
# root.mainloop()