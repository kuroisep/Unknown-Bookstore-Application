import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image
from tkinter.ttk import *
from tkinter import ttk
import pandas
from pandas import DataFrame
import csv
import datetime
import cv2
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from UnknownShop import LoginPage

class Stack:
    def __init__(self):
        self.items = []
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def __str__(self):
        return str(self.items)
    def isEmpty(self):
        return self.items == []
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)

class main_admin_screen:
    #---------------------------    init     -------------------------------------------------------------#
    def __init__(self):
        self.admin_window = tk.Tk()
        self.admin_window.title("Unknown Book Store // Admin")
        x = (700) - (750/2)
        y = (420) - (500/2)
        self.admin_window.geometry("1280x720+%d+%d" % (x, y))
        

        # LOGO
        img_logo_path = "Shop_Page\PICTURE\logo.png"
        self.img_logo = ImageTk.PhotoImage(
            Image.open(img_logo_path).resize((150, 150)))
        Label(image=self.img_logo).place(x=25, y=5)

        self.menubar()
        self.orderframe = LabelFrame(
            self.admin_window, text="Order Management")
        self.bookframe = LabelFrame(self.admin_window, text="Book Management")
        self.menberframe = LabelFrame(
            self.admin_window, text="Member Management")
        self.orderhistoryframe = LabelFrame(
            self.admin_window, text="Order History")

        self.time_label = Label(self.admin_window, font=(
            'calibri', 12, 'bold'), background='black', foreground='white')
        self.time_label.place(x=1135, y=2)
        self.time()

        """ 
        THEAM
        """
        style = ttk.Style(self.admin_window)
        style.configure('Treeview', rowheight=25)
        # style.configure("TButton", foreground="blue", background="orange")
        # Import the tcl file
        # self.admin_window.tk.call('source', 'UnknownShop/azure.tcl')

        # Set the theme with the theme_use method
        # style.theme_use('azure')
        """ 
        THEAM
        """
        #---------------------------    OrderPage     -------------------------------------------------------------#
        self.OrderTime = StringVar()
        self.OrderID = StringVar()
        self.Customer = StringVar()
        self.Address = StringVar()
        self.Total = StringVar()
        self.Status = StringVar()
        self.ShippedTime = StringVar()
        self.CompletedTime = StringVar()
        #---------------------------    BookPage     -------------------------------------------------------------#
        self.No = StringVar()
        self.Code = StringVar()
        self.Name = StringVar()
        self.Author = StringVar()
        self.Category = StringVar()
        self.Price = StringVar()
        self.Page = StringVar()
        self.Ex = StringVar()
        self.Stock = StringVar()
        self.Rating = StringVar()
        self.list_img_book = os.listdir('BookPics')

        #---------------------------    MemberPage     -------------------------------------------------------------#
        self.username = StringVar()
        self.password = StringVar()
        self.fname = StringVar()
        self.lname = StringVar()
        self.gender = StringVar()
        self.birthday = StringVar()
        self.email = StringVar()
        self.telphone = StringVar()

        #---------------------------     Database     ------------------------------------------------------------ #
        # Order Manangement
        self.df = pandas.read_csv('UnknownShop\\database\\order.csv')
        # print(self.df)
        self.order_data = self.df.values.tolist()


        # Order Detail
        self.df1 = pandas.read_csv('UnknownShop\\database\\order_detail.csv')
        self.order_detail_data = self.df1.values.tolist()

        # Book Page
        self.df2 = pandas.read_csv('UnknownShop\\database\\DataBookList.csv')
        self.book_data = self.df2.values.tolist()
        
        # Member Page
        self.df3 = pandas.read_csv('login.csv')
        self.member_data = self.df3.values.tolist()

        self.admin_window.resizable(0, 0)
        self.admin_window.mainloop()

    def time(self):
        nowtime = datetime.datetime.now()
        string = nowtime.strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.config(text=string)
        self.time_label.after(1000, self.time)

    def menubar(self):
        # Menubar
        menuframe = LabelFrame(self.admin_window, text="Menu")
        menuframe.place(x=2, y=150, height=570, width=200)
        Button(menuframe, text='Check Order', width=27,
               command=self.orderPage).grid(row=0, padx=10, pady=10)
        Button(menuframe, text='Order history', width=27,
               command=self.orderhistoryPage).grid(row=1, padx=5, pady=10)
        Button(menuframe, text='Book management', width=27,
               command=self.bookPage).grid(row=2, padx=5, pady=10)
        Button(menuframe, text='Member management', width=27,
               command=self.menberPage).grid(row=3, padx=5, pady=10)
        Button(menuframe, text='Admin', width=27).grid(row=4, padx=5, pady=10)

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  Order Page      <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
    def orderPage(self):
        self.destoryframe()
        #------------------------------    init    ------------------------------------------------------------#
        self.orderframe = LabelFrame(
            self.admin_window, text="Order Management")
        self.order_table_frame = LabelFrame(self.orderframe)
        #------------------------------   Table Plane     ------------------------------------------------------------#
        columns = ("Order Time", "Order ID", "Customer",
                   "Address", "Quantity", "Total Amount", "Status")
        self.order_treeview = Treeview(
            self.order_table_frame, column=columns, show="headings", height="20")
        yscrollbar = ttk.Scrollbar(
            self.order_table_frame, orient="vertical", command=self.order_treeview.yview)
        self.order_treeview.config(yscrollcommand=yscrollbar.set)
        yscrollbar.pack(side="right", fill="y")
        self.order_treeview.bind(
            "<ButtonRelease-1>", self.orderPage_lookuptreeview)
        for col in columns:
            self.order_treeview.heading(col, text=col, command=lambda _col=col: self.treeview_sort_column(
                self.order_treeview, _col, False))

        self.order_treeview.column(0, anchor='center', width=150)
        self.order_treeview.column(1, anchor='center', width=100)
        self.order_treeview.column(2, anchor='center', width=120)
        self.order_treeview.column(3, anchor='w', width=230)
        self.order_treeview.column(4, anchor='center', width=100)
        self.order_treeview.column(5, anchor='center', width=100)
        self.order_treeview.column(6, anchor='center', width=150)

        # self.order_treeview.insert('', 'end', values=["Order Time","Order ID","Customer","Address","Quantity","Total Amount","Status"])
        for i in self.order_data:
            self.order_treeview.insert('', 'end', values=[i][0])

        self.order_treeview.pack()
        self.order_table_frame.place(x=20, y=10, height=400, width=1000)

        #------------------------------    Detail Plane     ------------------------------------------------------------#
        self.order_detail_frame = LabelFrame(self.orderframe, text="Details")

        Label(self.order_detail_frame, text="Order ID#").grid(
            row=0, column=0, padx=10, pady=5, sticky="E")
        self.order_id_entry = Text(self.order_detail_frame, width=20, height=1)
        self.order_id_entry.insert(1.0, '')
        self.order_id_entry.bind("<Key>", lambda e: "break")
        self.order_id_entry.grid(row=0, column=1, padx=10, pady=5)

        Label(self.order_detail_frame, text="Customer :").grid(
            row=1, column=0, padx=10, pady=5, sticky="E")
        self.order_user_entry = Text(
            self.order_detail_frame, width=20, height=1)
        self.order_user_entry.insert(1.0, '')
        self.order_user_entry.bind("<Key>", lambda e: "break")
        self.order_user_entry.grid(row=1, column=1, padx=10, pady=5)

        Label(self.order_detail_frame, text="Order Time :").grid(
            row=2, column=0, padx=10, pady=5, sticky="E")
        self.order_ordertime_entry = Text(
            self.order_detail_frame, width=20, height=1)
        self.order_ordertime_entry.insert(1.0, '')
        self.order_ordertime_entry.bind("<Key>", lambda e: "break")
        self.order_ordertime_entry.grid(row=2, column=1, padx=10, pady=5)

        Label(self.order_detail_frame, text="Shipped Time :").grid(
            row=3, column=0, padx=10, pady=5, sticky="E")
        self.order_shiptime_entry = Text(
            self.order_detail_frame, width=20, height=1)
        self.order_shiptime_entry.insert(1.0, '')
        self.order_shiptime_entry.bind("<Key>", lambda e: "break")
        self.order_shiptime_entry.grid(row=3, column=1, padx=10, pady=5)

        Label(self.order_detail_frame, text="Completed Time :").grid(
            row=4, column=0, padx=10, pady=5, sticky="E")
        self.order_completedtime_entry = Text(
            self.order_detail_frame, width=20, height=1)
        self.order_completedtime_entry.insert(1.0, '')
        self.order_completedtime_entry.bind("<Key>", lambda e: "break")
        self.order_completedtime_entry.grid(row=4, column=1, padx=10, pady=5)

        Label(self.order_detail_frame, text="Address :").grid(
            row=0, column=2, padx=10, pady=5, sticky="E")
        self.order_address_entry = Text(
            self.order_detail_frame, width=20, height=5)
        self.order_address_entry.insert(1.0, '')
        self.order_address_entry.grid(
            row=0, column=3, padx=10, pady=5, sticky="W", rowspan=3)

        Label(self.order_detail_frame, text="Order Status :").grid(
            row=3, column=2, padx=10, pady=5, sticky="E")
        self.order_status_entry = Combobox(self.order_detail_frame, value=[
                                           'Payment confirmed', 'Waiting for shipment', 'Shipped', 'Delivered', 'Cancelled order'])
        self.order_status_entry.insert(0, '')

        self.order_status_entry.grid(
            row=3, column=3, padx=10, pady=5, sticky="W")

        self.order_detail_frame.place(x=20, y=430, height=200, width=700)

        #------------------------------  Option Plane     ------------------------------------------------------------#
        self.order_option_frame = LabelFrame(self.orderframe, text="Option")
        self.order_update_button = Button(
            self.order_option_frame, text='Update', command=self.orderPage_update_state, state=DISABLED)
        self.order_update_button.grid(row=0, column=0, padx=10, pady=5)

        self.order_detail_button = Button(
            self.order_option_frame, text='Order Details', command=self.orderdetailPage)
        self.order_detail_button.grid(row=0, column=1, padx=10, pady=5)
        self.order_option_frame.place(x=750, y=430, height=200, width=250)
        self.order_search_entry = Text(self.order_option_frame, width=10, height=1)
        self.order_search_entry.grid(row=1, column=0, padx=10, pady=5)
        self.order_search_button = Button(
            self.order_option_frame, text='Search Order', command=self.search_order_treeview)
        self.order_search_entry.insert(1.0, 'Order ID')
        self.order_search_entry.bind("<Button-1>", self.order_id_clear)
        self.order_search_button.grid(row=1, column=1, padx=10, pady=5)
        self.order_option_frame.place(x=750, y=430, height=200, width=250)

        self.orderframe.place(x=220, y=25, height=680, width=1040)

    ##################################    Update Button   <Order Page>  #######################################################
    def orderPage_update_state(self):
        self.nowtime = datetime.datetime.now()
        if(messagebox.askokcancel("Confirmation", "Update OrderID \n[ {} ] ?".format(self.OrderID.get()), parent=self.orderframe)) == True:
            self.order_update_button.config(state=DISABLED)
            if self.order_status_entry.get() == 'Shipped':
                self.order_shiptime_entry.delete('1.0', END)
                self.order_shiptime_entry.insert(
                    1.0, self.nowtime.strftime("%Y-%m-%d %H:%M:%S"))
            elif self.order_status_entry.get() == 'Delivered':
                self.order_completedtime_entry.delete('1.0', END)
                self.order_completedtime_entry.insert(
                    1.0, self.nowtime.strftime("%Y-%m-%d %H:%M:%S"))
            self.df.loc[self.df['Order_ID'] == self.OrderID.get(
            ), 'Address'] = self.order_address_entry.get('1.0', 'end-1c')
            self.df.loc[self.df['Order_ID'] == self.OrderID.get(
            ), 'Shipped_time'] = self.order_shiptime_entry.get('1.0', 'end-1c')
            self.df.loc[self.df['Order_ID'] == self.OrderID.get(
            ), 'Completed_time'] = self.order_completedtime_entry.get('1.0', 'end-1c')
            self.df.loc[self.df['Order_ID'] == self.OrderID.get(
            ), 'Status'] = self.order_status_entry.get()
            self.df.to_csv("UnknownShop\\database\\order.csv", index=False)
            # Treeview Update
            self.order_treeview.delete(*self.order_treeview.get_children())
            treeview = pandas.read_csv('UnknownShop\\database\\order.csv')
            treeview_update = treeview.values.tolist()
            for i in treeview_update:
                self.order_treeview.insert('', 'end', values=[i][0])

    ###############################    Treeview Focus    <Order Page> #########################################################
    def orderPage_lookuptreeview(self, event):
        self.order_update_button.config(state=NORMAL)
        curItem = self.order_treeview.focus()
        cur = self.order_treeview.item(curItem)['values']
        if cur == '':
            self.order_update_button.config(state=DISABLED)
            return
        if len(cur) != 9:
            for i in range(9-len(cur)):
                cur.append('')
        self.OrderTime.set(cur[0])
        self.OrderID.set(cur[1])
        self.Customer.set(cur[2])
        self.Address.set(cur[3])
        self.Total.set(cur[4])
        self.Status.set(cur[6])
        self.ShippedTime.set(cur[7])
        self.CompletedTime.set(cur[8])
        self.orderPage_detailupdate()

    ###############################    Detail Plane Update    <Order Page> #########################################################
    def orderPage_detailupdate(self):
        self.order_id_entry.delete('1.0', END)
        self.order_user_entry.delete('1.0', END)
        self.order_ordertime_entry.delete('1.0', END)
        self.order_completedtime_entry.delete('1.0', END)
        self.order_shiptime_entry.delete('1.0', END)
        self.order_address_entry.delete('1.0', END)
        self.order_status_entry.delete(0, END)
        self.order_id_entry.insert(1.0, self.OrderID.get())
        self.order_user_entry.insert(1.0, self.Customer.get())
        self.order_ordertime_entry.insert(1.0, self.OrderTime.get())
        self.order_shiptime_entry.insert(1.0, self.ShippedTime.get())
        self.order_completedtime_entry.insert(1.0, self.CompletedTime.get())
        self.order_address_entry.insert(1.0, self.Address.get())
        self.order_status_entry.insert(0, self.Status.get())
    ###############################    Searching    <Order Page> #########################################################
    def order_id_clear(self,e):
        if self.order_search_entry.get('1.0', 'end-1c') == 'Order ID':
            self.order_search_entry.delete('1.0', END)
    def search_order_treeview(self):
        query = self.order_search_entry.get('1.0','end-1c')
        selections = []
        for child in self.order_treeview.get_children(''):
            # print(self.order_treeview.item(child)['values'][1])
            if query in self.order_treeview.item(child)['values'][1]:   # compare strings in  lower cases.
                selections.append(child)
        self.order_treeview.selection_set(selections)
    ###############################    Treeview sort   <Function> #######################################################
    def treeview_sort_column(self, tv, col, reverse):
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)

        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)

        # reverse sort next time
        tv.heading(col, command=lambda _col=col: self.treeview_sort_column(
            tv, _col, not reverse))

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  Pop-up OrderDetail Page  <Order Page>   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
    def orderdetailPage(self):
        #------------------------------    init     ------------------------------------------------------------#
        self.order_detail_screen = Toplevel(self.admin_window)
        self.order_detail_screen.title("Order Details")
        self.order_detail_screen.focus_set()
        self.order_detail_screen.grab_set()
        self.order_detail_screen.resizable(0, 0)
        x = (960) - (750/2)
        y = (540) - (650/2)
        self.order_detail_screen.geometry("750x600+%d+%d" % (x, y))

        self.orderdetail_table_frame = LabelFrame(
            self.order_detail_screen, text="Order List")
        self.orderdetail_detail_frame = LabelFrame(
            self.order_detail_screen, text='')
        #------------------------------   Table Plane     ------------------------------------------------------------#
        columns = ("BookCode", "BookName", "Quantity", "Total amount")
        self.orderdetail_treeview = Treeview(
            self.orderdetail_table_frame, column=columns, show="headings", height="20")
        yscrollbar = ttk.Scrollbar(
            self.orderdetail_table_frame, orient="vertical", command=self.orderdetail_treeview.yview)
        self.orderdetail_treeview.config(yscrollcommand=yscrollbar.set)
        yscrollbar.pack(side="right", fill="y")
        self.orderdetail_treeview.bind(
            "<ButtonRelease-1>", self.orderPage_lookuptreeview)
        for col in columns:
            self.orderdetail_treeview.heading(col, text=col, command=lambda _col=col: self.treeview_sort_column(
                self.orderdetail_treeview, _col, False))

        self.orderdetail_treeview.column(0, anchor='center', width=150)
        self.orderdetail_treeview.column(1, anchor='center', width=300)
        self.orderdetail_treeview.column(2, anchor='center', width=100)
        self.orderdetail_treeview.column(3, anchor='center', width=100)

        # self.orderdetail_treeview.insert('', 'end', values=['Timestamp','Order ID','Name ',"Address","Order Total","status"])

        data_check = False
        for i in self.order_detail_data:
            if i[0] == self.OrderID.get():
                self.orderdetail_treeview.insert('', 'end', values=i[1:])
                data_check = True

        self.orderdetail_treeview.pack()
        #------------------------------    Detail Plane     ------------------------------------------------------------#

        self.orderdetail_table_frame.place(x=20, y=10, height=400, width=700)
        self.orderdetail_detail_frame.place(x=20, y=430, height=150, width=700)
        if not data_check:
            messagebox.showerror(
                "Error", "The selected order not found", parent=self.order_detail_screen)

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  Order History Page     <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#

    def orderhistoryPage(self):
        self.destoryframe()
        self.orderhistoryframe = LabelFrame(
            self.admin_window, text="Order History")
        self.orderhistory_table_frame = LabelFrame(self.orderhistoryframe)
        #------------------------------    Table Plane     ------------------------------#
        columns = ("Order Time", "Order ID", "Customer",
                   "Shipped Time", "Completed Time", "Status")
        self.orderhistory_treeview = Treeview(
            self.orderhistory_table_frame, column=columns, show="headings", height="18")
        yscrollbar = ttk.Scrollbar(self.orderhistory_table_frame,
                                   orient="vertical", command=self.orderhistory_treeview.yview)
        self.orderhistory_treeview.config(yscrollcommand=yscrollbar.set)
        yscrollbar.pack(side="right", fill="y")
        for col in columns:
            self.orderhistory_treeview.heading(col, text=col, command=lambda _col=col: self.treeview_sort_column(
                self.orderhistory_treeview, _col, False))

        self.orderhistory_treeview.column(0, anchor='center', width=150)
        self.orderhistory_treeview.column(1, anchor='center', width=100)
        self.orderhistory_treeview.column(2, anchor='center', width=150)
        self.orderhistory_treeview.column(3, anchor='center', width=150)
        self.orderhistory_treeview.column(4, anchor='center', width=150)
        self.orderhistory_treeview.column(5, anchor='center', width=150)

        # self.orderhistory_treeview.insert('', 'end', values=['Timestamp','Order ID','Name ',"Address","Order Total","status"])

        for i in self.order_data:
            self.orderhistory_treeview.insert(
                '', 'end', values=[i[0], i[1], i[2], i[7], i[8], i[6]])

        self.orderhistory_treeview.pack()
        self.orderhistory_table_frame.place(x=20, y=10, height=420, width=1000)
        #------------------------------    Graph Plane     ------------------------------#
        self.orderhistory_graphframe = LabelFrame(
            self.orderhistoryframe, text="Graph")
        figure2 = plt.Figure(figsize=(5, 4), dpi=100)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, self.orderhistory_graphframe)
        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        # df = self.df[['Order_time',len(self.order_data[0])]].groupby('Order_time').sum()
        # df.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)

        data = []
        for i in self.order_data:
            data.extend(i[0].split())
        del data[1::2]
        check = dict()
        for i in data:
            if i in check:
                check[i] += 1
            else:
                check[i] = 1

        data_plot = {'Date': list(check.keys()),
         'Sales': list(check.values())
        }
        dataplot = DataFrame(data_plot,columns=['Date','Sales'])
        # ax2.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])
        dataplot = dataplot[['Date','Sales']].groupby('Date').sum()
        dataplot.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=5)
        ax2.set_title('Daily Sales Summary')
        self.orderhistory_graphframe.place(x=20, y=440, height=220, width=1000)

        self.orderhistoryframe.place(x=220, y=25, height=690, width=1040)

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   Book Manangment Page     <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#

    def bookPage(self):
        self.destoryframe()
        #------------------------------    init     ------------------------------#
        self.bookframe = LabelFrame(self.admin_window, text="Book Management")
        self.book_table_frame = LabelFrame(self.bookframe)
        self.book_pic_input = 'BookPics\\NOT_FOUND.png'

        #------------------------------    Table Plane     ------------------------------#
        columns = ("No", "Code", "Name", "Author", "Category", "Price")
        self.book_treeview = Treeview(
            self.book_table_frame, column=columns, show="headings", height="20")
        yscrollbar = ttk.Scrollbar(
            self.book_table_frame, orient="vertical", command=self.book_treeview.yview)
        self.book_treeview.config(yscrollcommand=yscrollbar.set)
        yscrollbar.pack(side="right", fill="y")
        self.book_treeview.bind("<ButtonRelease-1>",
                                self.bookpage_lookuptreeview)
        for col in columns:
            self.book_treeview.heading(col, text=col, command=lambda _col=col: self.treeview_sort_column(
                self.book_treeview, _col, False))

        self.book_treeview.column(0, anchor='center', width=50)
        self.book_treeview.column(1, anchor='center', width=80)
        self.book_treeview.column(2, anchor='w', width=300)
        self.book_treeview.column(3, anchor='w', width=150)
        self.book_treeview.column(4, anchor='center', width=170)
        self.book_treeview.column(5, anchor='center', width=100)

        for i in self.book_data:
            self.book_treeview.insert('', 'end', values=[i][0])

        self.book_treeview.pack()

        #------------------------------  Detail Plane     ------------------------------------------------------------#
        self.book_detail_frame = LabelFrame(self.bookframe, text="Details")
        Label(self.book_detail_frame, text="No").grid(
            row=0, column=0, padx=10, pady=5, sticky="E")
        self.no_entry = Text(self.book_detail_frame, width=10, height=1)
        self.no_entry.insert(1.0, '')
        self.no_entry.grid(row=0, column=1, padx=10, pady=5)
        Label(self.book_detail_frame, text="Code").grid(
            row=1, column=0, padx=10, pady=5, sticky="E")
        self.code_entry = Text(self.book_detail_frame, width=10, height=1)
        self.code_entry.insert(1.0, '')
        self.code_entry.grid(row=1, column=1, padx=10, pady=5)
        Label(self.book_detail_frame, text="Name").grid(
            row=0, column=2, padx=10, pady=5, sticky="E")
        self.name_entry = Text(self.book_detail_frame, width=65, height=1)
        self.name_entry.insert(1.0, '')
        self.name_entry.grid(row=0, column=3, padx=10, pady=5, columnspan=4)
        Label(self.book_detail_frame, text="Author").grid(
            row=1, column=2, padx=10, pady=5, sticky="E")
        self.author_entry = Text(self.book_detail_frame, width=65, height=1)
        self.author_entry.insert(1.0, '')
        self.author_entry.grid(row=1, column=3, padx=10, pady=5, columnspan=4)
        Label(self.book_detail_frame, text="Category").grid(
            row=2, column=2, padx=10, pady=5, sticky="E")
        self.category_entry = Text(self.book_detail_frame, width=50, height=1)
        self.category_entry.insert(1.0, '')
        self.category_entry.grid(
            row=2, column=3, padx=10, pady=5, columnspan=2)
        Label(self.book_detail_frame, text="Price").grid(
            row=2, column=0, padx=10, pady=5, sticky="E")
        self.price_entry = Text(self.book_detail_frame, width=10, height=1)
        self.price_entry.insert(1.0, '')
        self.price_entry.grid(row=2, column=1, padx=10, pady=5)
        Label(self.book_detail_frame, text="Page").grid(
            row=3, column=0, padx=10, pady=5, sticky="E")
        self.page_entry = Text(self.book_detail_frame, width=10, height=1)
        self.page_entry.insert(1.0, '')
        self.page_entry.grid(row=3, column=1, padx=10, pady=5)
        Label(self.book_detail_frame, text="Ex").grid(
            row=4, column=0, padx=10, pady=5, sticky="E")
        self.ex_entry = Text(self.book_detail_frame, width=90, height=5)
        self.ex_entry.insert(1.0, '')
        self.ex_entry.grid(row=4, column=1, padx=10,
                           pady=5, columnspan=15, rowspan=5)
        Label(self.book_detail_frame, text="Stock").grid(
            row=3, column=2, padx=10, pady=5, sticky="E")
        self.stock_entry = Text(self.book_detail_frame, width=10, height=1)
        self.stock_entry.insert(1.0, '')
        self.stock_entry.grid(row=3, column=3, padx=10, pady=5, sticky='W')
        Label(self.book_detail_frame, text="Rating").grid(
            row=3, column=3, padx=10, pady=5, sticky="E")
        self.rating_entry = Text(self.book_detail_frame, width=10, height=1)
        self.rating_entry.insert(1.0, '')
        self.rating_entry.grid(row=3, column=4, padx=10, pady=5)
        self.viewpic_book_button = Button(
            self.book_detail_frame, text='Show Pic', command=self.viewPicbookPage)
        self.viewpic_book_button.grid(row=3, column=5, padx=5, pady=5)

        self.book_detail_frame.place(x=20, y=430, height=235, width=800)
        #------------------------------  Option Plane     ------------------------------------------------------------#
        self.book_option_frame = LabelFrame(self.bookframe, text="Option")
        self.update_book_button = Button(
            self.book_option_frame, text='Update', state=DISABLED, command=self.bookPage_update_state)
        self.update_book_button.grid(row=0, column=0, padx=5, pady=5)
        self.delete_book_button = Button(
            self.book_option_frame, text='Delete', state=DISABLED, command=self.bookPage_delete_state)
        self.delete_book_button.grid(row=0, column=1, padx=5, pady=5)
        self.add_book_button = Button(
            self.book_option_frame, text='Add New', command=self.addbookPage)
        self.add_book_button.grid(row=1, column=0, padx=5, pady=5)

        self.book_option_frame.place(x=850, y=430, height=230, width=180)

        self.book_table_frame.place(x=20, y=10, height=400, width=1000)
        self.bookframe.place(x=220, y=25, height=690, width=1040)

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  Pop-up ViewPic Page  <Book Page>    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
    def viewPicbookPage(self):
        #------------------------------    init     ------------------------------------------------------------#
        self.viewpic_book_screen = Toplevel(self.admin_window)
        self.viewpic_book_screen.title(
            "{} : {}".format(self.Code.get(), self.Name.get()))
        self.viewpic_book_screen.focus_set()
        self.viewpic_book_screen.grab_set()
        self.viewpic_book_screen.resizable(0, 0)
        x = (960) - (400/2)
        y = (540) - (300/2)
        self.viewpic_book_screen.geometry("400x300+%d+%d" % (x, y))

        #------------------------------  Picture Plane     ------------------------------------------------------------#

        self.book_pic = ImageTk.PhotoImage(
            Image.open(self.book_pic_input).resize((120, 170)))
        self.viewpic_book_frame = LabelFrame(
            self.viewpic_book_screen, text='Picture')
        self.pic_book_label = Label(
            self.viewpic_book_frame, image=self.book_pic)
        self.pic_book_label.pack(anchor=CENTER)

        #------------------------------  Option Plane     ------------------------------------------------------------#
        self.viewpic_book_option_frame = LabelFrame(
            self.viewpic_book_screen, text='Option')
        self.select_pic_button = Button(
            self.viewpic_book_option_frame, text='Select', command=self.openimage)
        self.select_pic_button.grid(row=0, column=0, padx=25, pady=5)
        self.save_pic_button = Button(
            self.viewpic_book_option_frame, text='Save', state=DISABLED, command=self.saveimage)
        self.save_pic_button.grid(row=0, column=1, padx=25, pady=5)
        self.delete_pic_button = Button(
            self.viewpic_book_option_frame, text='Delete', state=DISABLED, command=self.deleteimage)
        self.delete_pic_button.grid(row=0, column=2, padx=25, pady=5)
        if self.book_pic_input != 'BookPics\\NOT_FOUND.png':
            self.delete_pic_button.config(state=NORMAL)

        self.viewpic_book_frame.place(x=10, y=10, height=200, width=380)
        self.viewpic_book_option_frame.place(x=10, y=210, height=80, width=380)
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  Picture Function  <Book Page>    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
    def openfn(self):
        temp = filedialog.askopenfilename(
            initialdir='BookPics\\', title='open')
        return temp
    def openimage(self):
        self.book_pic_input = self.openfn()
        if self.book_pic_input != '':
            self.delete_pic_button.config(state=NORMAL)
            self.save_pic_button.config(state=NORMAL)
            self.book_pic = ImageTk.PhotoImage(
                Image.open(self.book_pic_input).resize((120, 170)))
            self.pic_book_label.destroy()
            self.pic_book_label = Label(
                self.viewpic_book_frame, image=self.book_pic)
            self.pic_book_label.pack(anchor=CENTER)

    def deleteimage(self):
        self.save_pic_button.config(state=NORMAL)
        self.delete_pic_button.config(state=DISABLED)
        self.book_pic_input = 'BookPics\\NOT_FOUND.png'
        self.book_pic = ImageTk.PhotoImage(
            Image.open(self.book_pic_input).resize((120, 170)))
        self.pic_book_label.destroy()
        self.pic_book_label = Label(
            self.viewpic_book_frame, image=self.book_pic)
        self.pic_book_label.pack(anchor=CENTER)

    def saveimage(self):
        if self.book_pic_input != '':
            if(messagebox.askokcancel("Confirmation", "Save Picture \n[ {} ] ?".format(self.Name.get()), parent=self.viewpic_book_screen)) == True:
                self.save_pic_button.config(state=DISABLED)
                temp_img = cv2.imread(self.book_pic_input)
                cv2.imwrite('BookPics\\{}.png'.format(self.Code.get()), temp_img)
        else:
            messagebox.showerror("Error", "Please select .png file",parent=self.viewpic_book_screen)
            self.save_pic_button.config(state=DISABLED)

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  Pop-up AddBook Page  <Book Page>    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#

    def addbookPage(self):
        #------------------------------    init     ------------------------------------------------------------#
        self.add_book_screen = Toplevel(self.admin_window)
        self.add_book_screen.title("Add Book")
        self.add_book_screen.focus_set()
        self.add_book_screen.grab_set()
        self.add_book_screen.resizable(0, 0)
        x = (960) - (800/2)
        y = (540) - (350/2)
        self.add_book_screen.geometry("800x300+%d+%d" % (x, y))
        self.addbook_pic_input = 'BookPics\\NOT_FOUND.png'

        #------------------------------    Picture Plane     ------------------------------------------------------------#
        self.add_picbook_frame = LabelFrame(
            self.add_book_screen, text='Picture')
        self.addbook_pic = ImageTk.PhotoImage(
            Image.open(self.addbook_pic_input).resize((120, 170)))
        self.addpic_book_label = Label(
            self.add_picbook_frame, image=self.addbook_pic)
        self.addpic_book_label.pack(anchor=CENTER)

        #------------------------------    Detail Plane     ------------------------------------------------------------#
        self.add_book_frame = LabelFrame(
            self.add_book_screen, text='Book Details')
        Label(self.add_book_frame, text="No").grid(
            row=0, column=0, padx=10, pady=5, sticky="E")
        self.addbook_no_entry = Text(self.add_book_frame, width=10, height=1)
        self.addbook_no_entry.insert(1.0, '')
        self.addbook_no_entry.grid(row=0, column=1, padx=10, pady=5)
        Label(self.add_book_frame, text="Code").grid(
            row=1, column=0, padx=10, pady=5, sticky="E")
        self.addbook_code_entry = Text(self.add_book_frame, width=10, height=1)
        self.addbook_code_entry.insert(1.0, '')
        self.addbook_code_entry.grid(row=1, column=1, padx=10, pady=5)
        Label(self.add_book_frame, text="Name").grid(
            row=0, column=2, padx=10, pady=5, sticky="E")
        self.addbook_name_entry = Text(self.add_book_frame, width=40, height=1)
        self.addbook_name_entry.insert(1.0, '')
        self.addbook_name_entry.grid(
            row=0, column=3, padx=10, pady=5, columnspan=3)
        Label(self.add_book_frame, text="Author").grid(
            row=1, column=2, padx=10, pady=5, sticky="E")
        self.addbook_author_entry = Text(
            self.add_book_frame, width=40, height=1)
        self.addbook_author_entry.insert(1.0, '')
        self.addbook_author_entry.grid(
            row=1, column=3, padx=10, pady=5, columnspan=3)
        Label(self.add_book_frame, text="Category").grid(
            row=2, column=2, padx=10, pady=5, sticky="W")
        self.addbook_category_entry = Text(
            self.add_book_frame, width=30, height=1)
        self.addbook_category_entry.insert(1.0, '')
        self.addbook_category_entry.grid(
            row=2, column=3, padx=10, pady=5, columnspan=2)
        Label(self.add_book_frame, text="Price").grid(
            row=2, column=0, padx=10, pady=5, sticky="E")
        self.addbook_price_entry = Text(
            self.add_book_frame, width=10, height=1)
        self.addbook_price_entry.insert(1.0, '')
        self.addbook_price_entry.grid(row=2, column=1, padx=10, pady=5)
        Label(self.add_book_frame, text="Page").grid(
            row=3, column=0, padx=10, pady=5, sticky="E")
        self.addbook_page_entry = Text(self.add_book_frame, width=10, height=1)
        self.addbook_page_entry.insert(1.0, '')
        self.addbook_page_entry.grid(row=3, column=1, padx=10, pady=5)
        Label(self.add_book_frame, text="Ex").grid(
            row=3, column=2, padx=10, pady=5, sticky="E")
        self.addbook_ex_entry = Text(self.add_book_frame, width=40, height=5)
        self.addbook_ex_entry.insert(1.0, '')
        self.addbook_ex_entry.grid(
            row=3, column=3, padx=10, pady=5, columnspan=3, rowspan=3)
        Label(self.add_book_frame, text="Stock").grid(
            row=4, column=0, padx=10, pady=5, sticky="E")
        self.addbook_stock_entry = Text(
            self.add_book_frame, width=10, height=1)
        self.addbook_stock_entry.insert(1.0, '')
        self.addbook_stock_entry.grid(row=4, column=1, padx=10, pady=5)
        Label(self.add_book_frame, text="Rating").grid(
            row=5, column=0, padx=10, pady=5, sticky="E")
        self.addbook_rating_entry = Text(
            self.add_book_frame, width=10, height=1)
        self.addbook_rating_entry.insert(1.0, '')
        self.addbook_rating_entry.grid(row=5, column=1, padx=10, pady=5)

        #------------------------------    Option Detail Plane     ------------------------------------------------------------#
        self.add_book_option_frame = LabelFrame(self.add_book_screen, text='')
        self.clear_addbook_button = Button(
            self.add_book_option_frame, text='Clear', command=self.clear_addbook)
        self.clear_addbook_button.grid(row=0, column=0, padx=12, pady=0)
        self.save_addbook_button = Button(
            self.add_book_option_frame, text='Save', command=self.save_addbook)
        self.save_addbook_button.grid(row=0, column=1, padx=12, pady=0)

        #------------------------------    Option Picture Plane     ------------------------------------------------------------#
        self.add_picbook_option_frame = LabelFrame(
            self.add_book_screen, text='')
        self.select_addpic_button = Button(
            self.add_picbook_option_frame, text='Select', command=self.openimage_new)
        self.select_addpic_button.grid(row=0, column=0, padx=3, pady=0)

        self.delete_addpic_button = Button(
            self.add_picbook_option_frame, text='Delete', state=DISABLED, command=self.deleteimage_new)
        self.delete_addpic_button.grid(row=0, column=1, padx=3, pady=0)

        self.add_book_option_frame.place(x=585, y=220, height=50, width=200)
        self.add_picbook_frame.place(x=10, y=10, height=210, width=170)
        self.add_picbook_option_frame.place(x=10, y=220, height=50, width=170)
        self.add_book_frame.place(x=200, y=10, height=210, width=585)

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  Addbook Picture Function  <Book Page>    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
    def openimage_new(self):
        self.addbook_pic_input = self.openfn()
        if self.addbook_pic_input != '':
            self.delete_addpic_button.config(state=NORMAL)
            self.addbook_pic = ImageTk.PhotoImage(
                Image.open(self.addbook_pic_input).resize((120, 170)))
            self.addpic_book_label.destroy()
            self.addpic_book_label = Label(
                self.add_picbook_frame, image=self.addbook_pic)
            self.addpic_book_label.pack(anchor=CENTER)

    def deleteimage_new(self):
        self.delete_addpic_button.config(state=DISABLED)
        self.addbook_pic_input = 'BookPics\\NOT_FOUND.png'
        self.addbook_pic = ImageTk.PhotoImage(
            Image.open(self.addbook_pic_input).resize((120, 170)))
        self.addpic_book_label.destroy()
        self.addpic_book_label = Label(
            self.add_picbook_frame, image=self.addbook_pic)
        self.addpic_book_label.pack(anchor=CENTER)
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  Addbook Clear Function  <Book Page>    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#

    def clear_addbook(self):
        if(messagebox.askokcancel("Confirmation", "Are you sure?", parent=self.add_book_screen)) == True:
            self.addbook_no_entry.delete('1.0', END)
            self.addbook_code_entry.delete('1.0', END)
            self.addbook_name_entry.delete('1.0', END)
            self.addbook_author_entry.delete('1.0', END)
            self.addbook_category_entry.delete('1.0', END)
            self.addbook_price_entry.delete('1.0', END)
            self.addbook_page_entry.delete('1.0', END)
            self.addbook_ex_entry.delete('1.0', END)
            self.addbook_stock_entry.delete('1.0', END)
            self.addbook_rating_entry.delete('1.0', END)

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  Addbook Save Function  <Book Page>    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
    def save_addbook(self):
        if self.addbook_no_entry.get('1.0', 'end-1c') != '' and self.addbook_code_entry.get('1.0', 'end-1c') != '' and self.addbook_name_entry.get('1.0', 'end-1c') != '' and self.addbook_author_entry.get('1.0', 'end-1c') != '' and self.addbook_category_entry.get('1.0', 'end-1c') != '' and self.addbook_price_entry.get('1.0', 'end-1c') != '' and self.addbook_page_entry.get('1.0', 'end-1c') != '' and self.addbook_ex_entry.get('1.0', 'end-1c') != '' and self.addbook_stock_entry.get('1.0', 'end-1c') != '' and self.addbook_rating_entry.get('1.0', 'end-1c') != '':
            if(messagebox.askokcancel("Confirmation", "Are you sure?", parent=self.add_book_screen)) == True:
                with open("UnknownShop\\database\\DataBookList.csv", 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([self.addbook_no_entry.get('1.0', 'end-1c'), self.addbook_code_entry.get('1.0', 'end-1c'), self.addbook_name_entry.get('1.0', 'end-1c'), self.addbook_author_entry.get('1.0', 'end-1c'),
                                    self.addbook_category_entry.get(
                                        '1.0', 'end-1c'), self.addbook_price_entry.get('1.0', 'end-1c'),
                                    self.addbook_page_entry.get('1.0', 'end-1c'), self.addbook_ex_entry.get(
                                        '1.0', 'end-1c'), self.addbook_stock_entry.get('1.0', 'end-1c'),
                                    self.addbook_rating_entry.get('1.0', 'end-1c')])
                if self.addbook_pic_input != '':
                    temp_img = cv2.imread(self.addbook_pic_input)
                    cv2.imwrite('BookPics\\{}.png'.format(
                        self.addbook_code_entry.get('1.0', 'end-1c')), temp_img)

                self.addbook_no_entry.delete('1.0', END)
                self.addbook_code_entry.delete('1.0', END)
                self.addbook_name_entry.delete('1.0', END)
                self.addbook_author_entry.delete('1.0', END)
                self.addbook_category_entry.delete('1.0', END)
                self.addbook_price_entry.delete('1.0', END)
                self.addbook_page_entry.delete('1.0', END)
                self.addbook_ex_entry.delete('1.0', END)
                self.addbook_stock_entry.delete('1.0', END)
                self.addbook_rating_entry.delete('1.0', END)
                self.add_book_screen.destroy()
                messagebox.showinfo("Alert", "Add Book Sucessfully!!")
        else:
            messagebox.showerror("Error", "Please fill out all fields required", parent=self.add_book_screen)

    ###############################    Treeview Focus    <Order Page> #########################################################

    def bookpage_lookuptreeview(self, event):
        self.update_book_button.config(state=NORMAL)
        self.delete_book_button.config(state=NORMAL)
        curItem = self.book_treeview.focus()
        cur = self.book_treeview.item(curItem)['values']
        if cur == '':
            self.update_book_button.config(state=DISABLED)
            self.delete_book_button.config(state=DISABLED)
            return
        if len(cur) != 10:
            for i in range(10-len(cur)):
                cur.append('')
        self.No.set(cur[0])
        self.Code.set(cur[1])
        self.Name.set(cur[2])
        self.Author.set(cur[3])
        self.Category.set(cur[4])
        self.Price.set(cur[5])
        self.Page.set(cur[6])
        self.Ex.set(cur[7])
        self.Stock.set(cur[8])
        self.Rating.set(cur[9])
        self.book_pic_input = 'BookPics\\{}.png'.format(self.Code.get())
        if str(self.Code.get()) + '.png' in self.list_img_book:
            self.book_pic_input = 'BookPics\\{}.png'.format(self.Code.get())
            self.book_pic = ImageTk.PhotoImage(
                Image.open(self.book_pic_input).resize((80, 130)))
        else:
            self.book_pic_input = 'BookPics\\NOT_FOUND.png'
            self.book_pic = ImageTk.PhotoImage(
                Image.open(self.book_pic_input).resize((80, 130)))

        self.bookPage_detailupdate()

    ###############################    Detail Plane Update    <Book Page> #########################################################
    def bookPage_detailupdate(self):
        self.no_entry.delete('1.0', END)
        self.code_entry.delete('1.0', END)
        self.name_entry.delete('1.0', END)
        self.author_entry.delete('1.0', END)
        self.category_entry.delete('1.0', END)
        self.price_entry.delete('1.0', END)
        self.page_entry.delete('1.0', END)
        self.ex_entry.delete('1.0', END)
        self.stock_entry.delete('1.0', END)
        self.rating_entry.delete('1.0', END)
        self.no_entry.insert(1.0, self.No.get())
        self.code_entry.insert(1.0, self.Code.get())
        self.name_entry.insert(1.0, self.Name.get())
        self.author_entry.insert(1.0, self.Author.get())
        self.category_entry.insert(1.0, self.Category.get())
        self.price_entry.insert(1.0, self.Price.get())
        self.page_entry.insert(1.0, self.Page.get())
        self.ex_entry.insert(1.0, self.Ex.get())
        self.stock_entry.insert(1.0, self.Stock.get())
        self.rating_entry.insert(1.0, self.Rating.get())

    ##################################    Update Button   <Book Page>  #######################################################
    def bookPage_update_state(self):
        if(messagebox.askokcancel("Confirmation", "Update Book \n[ {} ] ?".format(self.Name.get()), parent=self.bookframe)) == True:
            self.update_book_button.config(state=DISABLED)

            self.df2.loc[self.df2['Code'] == self.Code.get(), 'Name'] = self.name_entry.get('1.0','end-1c')
            self.df2.loc[self.df2['Code'] == self.Code.get(), 'Author'] = self.author_entry.get('1.0','end-1c')
            self.df2.loc[self.df2['Code'] == self.Code.get(), 'Category'] = self.category_entry.get('1.0','end-1c')
            self.df2.loc[self.df2['Code'] == self.Code.get(), 'Price'] = self.price_entry.get('1.0','end-1c')
            self.df2.loc[self.df2['Code'] == self.Code.get(), 'Page'] = self.page_entry.get('1.0','end-1c')
            self.df2.loc[self.df2['Code'] == self.Code.get(), 'Ex.'] = self.ex_entry.get('1.0','end-1c')
            self.df2.loc[self.df2['Code'] == self.Code.get(), 'Stock(s)'] = self.stock_entry.get('1.0','end-1c')
            self.df2.loc[self.df2['Code'] == self.Code.get(), 'Rating'] = self.rating_entry.get('1.0','end-1c')

            self.df2.to_csv("UnknownShop\\database\\DataBookList.csv", index=False)

            ### Treeview Update
            self.book_treeview.delete(*self.book_treeview.get_children())
            treeview = pandas.read_csv('UnknownShop\\database\\DataBookList.csv')
            treeview_update = treeview.values.tolist()
            for i in treeview_update:
                self.book_treeview.insert('', 'end', values=[i][0])

    ##################################    Delete Button   <Book Page>  #######################################################
    def bookPage_delete_state(self):
        if(messagebox.askokcancel("Confirmation", "Delete Book \n[ {} ] ?".format(self.Name.get()), parent=self.bookframe)) == True:
            self.delete_book_button.config(state=DISABLED)
            self.update_book_button.config(state=DISABLED)

            ## Database
            self.df2.drop(self.df2.loc[self.df2['Code']==self.Code.get()].index, inplace=True)

            self.df2.to_csv("UnknownShop\\database\\DataBookList.csv", index=False)

            ### Treeview Update
            self.book_treeview.delete(*self.book_treeview.get_children())
            treeview = pandas.read_csv('UnknownShop\\database\\DataBookList.csv')
            treeview_update = treeview.values.tolist()
            for i in treeview_update:
                self.book_treeview.insert('', 'end', values=[i][0])

            messagebox.showinfo("Info", "Deleted book \n[ {} ]".format(self.Name.get()), parent=self.bookframe)

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    Menber Manangment Page     <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#

    def menberPage(self):
        self.destoryframe()
        #------------------------------    init    ------------------------------------------------------------#
        self.memberframe = LabelFrame(
            self.admin_window, text="Member Management")

        #------------------------------   Table Plane     ------------------------------------------------------------#
        self.member_table_frame = LabelFrame(self.memberframe)
        columns = ("Loged in", "Username", "Name", "LastName",
                   "Gender", "Birthday", "Email", "PhoneNumber")
        self.member_treeview = Treeview(
            self.member_table_frame, column=columns, show="headings", height="20")
        yscrollbar = ttk.Scrollbar(
            self.member_table_frame, orient="vertical", command=self.member_treeview.yview)
        self.member_treeview.config(yscrollcommand=yscrollbar.set)
        yscrollbar.pack(side="right", fill="y")
        self.member_treeview.bind("<ButtonRelease-1>", self.memberPage_lookuptreeview)
        for col in columns:
            self.member_treeview.heading(col, text=col, command=lambda _col=col: self.treeview_sort_column(
                self.member_treeview, _col, False))

        self.member_treeview.column(0, anchor='center', width=60)
        self.member_treeview.column(1, anchor='center', width=100)
        self.member_treeview.column(2, anchor='w', width=100)
        self.member_treeview.column(3, anchor='w', width=100)
        self.member_treeview.column(4, anchor='center', width=80)
        self.member_treeview.column(5, anchor='center', width=100)
        self.member_treeview.column(6, anchor='center', width=200)
        self.member_treeview.column(7, anchor='center', width=150)

        for i in self.member_data:
            self.member_treeview.insert('', 'end', values=[i[0],i[1],i[3],i[4],i[5],i[6],i[7],i[8],i[2]])

        self.member_treeview.pack()
        self.member_table_frame.place(x=20, y=10, height=400, width=1000)

        #------------------------------    Detail Plane     ------------------------------------------------------------#
        self.member_detail_frame = LabelFrame(self.memberframe, text="Details")

        Label(self.member_detail_frame, text="Username").grid(
            row=0, column=0, padx=10, pady=5, sticky="E")
        self.username_entry = Text(
            self.member_detail_frame, width=20, height=1)
        self.username_entry.insert(1.0, '')
        self.username_entry.bind("<Key>", lambda e: "break")
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        Label(self.member_detail_frame, text="Password").grid(
            row=1, column=0, padx=10, pady=5, sticky="E")
        self.password_entry = Text(
            self.member_detail_frame, width=20, height=1)
        self.password_entry.insert(1.0, '')
        self.password_entry.bind("<Button-1>", self.password_clear)
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        Label(self.member_detail_frame, text="Firstname").grid(
            row=2, column=0, padx=10, pady=5, sticky="E")
        self.fname_entry = Text(
            self.member_detail_frame, width=20, height=1)
        self.fname_entry.insert(1.0, '')
        self.fname_entry.grid(row=2, column=1, padx=10, pady=5)

        Label(self.member_detail_frame, text="Lastname").grid(
            row=3, column=0, padx=10, pady=5, sticky="E")
        self.lname_entry = Text(
            self.member_detail_frame, width=20, height=1)
        self.lname_entry.insert(1.0, '')
        self.lname_entry.grid(row=3, column=1, padx=10, pady=5)

        Label(self.member_detail_frame, text="Gender").grid(
            row=0, column=2, padx=10, pady=5, sticky="E")
        self.gender_entry = Text(
            self.member_detail_frame, width=20, height=1)
        self.gender_entry.insert(1.0, '')
        self.gender_entry.grid(row=0, column=3, padx=10, pady=5)

        Label(self.member_detail_frame, text="Birthday").grid(
            row=1, column=2, padx=10, pady=5, sticky="E")
        self.birthday_entry = Text(
            self.member_detail_frame, width=20, height=1)
        self.birthday_entry.insert(1.0, '')
        self.birthday_entry.grid(
            row=1, column=3, padx=10, pady=5, sticky="W")

        Label(self.member_detail_frame, text="Email").grid(
            row=2, column=2, padx=10, pady=5, sticky="E")
        self.email_entry = Text(
            self.member_detail_frame, width=20, height=1)
        self.email_entry.insert(1.0, '')
        self.email_entry.grid(row=2, column=3, padx=10, pady=5)

        Label(self.member_detail_frame, text="Telphone").grid(
            row=3, column=2, padx=10, pady=5, sticky="E")
        self.tel_entry = Text(
            self.member_detail_frame, width=20, height=1)
        self.tel_entry.insert(1.0, '')
        self.tel_entry.grid(row=3, column=3, padx=10, pady=5)

        self.member_detail_frame.place(x=20, y=430, height=200, width=700)

        #------------------------------  Option Plane     ------------------------------------------------------------#
        self.member_option_frame = LabelFrame(self.memberframe, text="Option")
        self.member_update_button = Button(
            self.member_option_frame, text='Update', state=DISABLED,command=self.memberPage_update_state)
        self.member_update_button.grid(row=0, column=1, padx=10, pady=5)

        self.member_delete_button = Button(
            self.member_option_frame, text='Delete', state=DISABLED,command=self.memberkPage_delete_state)
        self.member_delete_button.grid(row=0, column=2, padx=10, pady=5)
        self.member_add_button = Button(self.member_option_frame, text='Register',command=self.add_member)
        self.member_add_button.grid(row=1, column=1, padx=10, pady=5)

        self.member_option_frame.place(x=750, y=430, height=200, width=250)

        self.memberframe.place(x=220, y=25, height=680, width=1040)
    ###############################    Treeview Focus    <Member Page> #########################################################
    def memberPage_lookuptreeview(self, event):
        self.member_update_button.config(state=NORMAL)
        self.member_delete_button.config(state=NORMAL)
        curItem = self.member_treeview.focus()
        cur = self.member_treeview.item(curItem)['values']
        if cur == '':
            self.member_update_button.config(state=DISABLED)
            self.member_delete_button.config(state=DISABLED)
            return
        if len(cur) != 9:
            for i in range(9-len(cur)):
                cur.append('')
        self.username.set(cur[1])
        self.password.set(cur[8])
        self.fname.set(cur[2])
        self.lname.set(cur[3])
        self.gender.set(cur[4])
        self.birthday.set(cur[5])
        self.email.set(cur[6])
        self.telphone.set(cur[7])
        self.memberPage_detailupdate()
    ###############################    Detail Plane Update    <Member Page> #########################################################
    def memberPage_detailupdate(self):
        self.username_entry.delete('1.0', END)
        self.password_entry.delete('1.0', END)
        self.fname_entry.delete('1.0', END)
        self.lname_entry.delete('1.0', END)
        self.gender_entry.delete('1.0', END)
        self.birthday_entry.delete('1.0', END)
        self.email_entry.delete('1.0', END)
        self.tel_entry.delete('1.0', END)
        self.username_entry.insert(1.0, self.username.get())
        self.password_entry.insert(1.0, '********')
        self.fname_entry.insert(1.0, self.fname.get())
        self.lname_entry.insert(1.0, self.lname.get())
        self.gender_entry.insert(1.0, self.gender.get())
        self.birthday_entry.insert(1.0, self.birthday.get())
        self.email_entry.insert(1.0, self.email.get())
        self.tel_entry.insert(1.0, self.telphone.get())
    def password_clear(self,e):
        if self.password_entry.get('1.0', 'end-1c') == '********':
            self.password_entry.delete('1.0', END)
    ##################################    Delete Button   <Member Page>  #######################################################
    def memberkPage_delete_state(self):
        if(messagebox.askokcancel("Confirmation", "Delete member \n[ {} {} ] ?".format(self.fname.get(),self.lname.get()), parent=self.memberframe)) == True:
            self.member_delete_button.config(state=DISABLED)
            self.member_update_button.config(state=DISABLED)

            ## Database
            self.df3.drop(self.df3.loc[self.df3['USER']==self.username.get()].index, inplace=True)

            self.df3.to_csv("login.csv", index=False)

            ### Treeview Update
            self.member_treeview.delete(*self.member_treeview.get_children())
            treeview = pandas.read_csv('login.csv')
            treeview_update = treeview.values.tolist()
            for i in treeview_update:
                self.member_treeview.insert('', 'end', values=[i[0],i[1],i[3],i[4],i[5],i[6],i[7],i[8],i[2]])
            messagebox.showinfo("Info", "Deleted member \n[ {} {} ]".format(self.fname.get(),self.lname.get()), parent=self.memberframe)
            
    ##################################    Update Button   <Member Page>  #######################################################
    def memberPage_update_state(self):
        if(messagebox.askokcancel("Confirmation", "Update Member \n[ {} {} ] ?".format(self.fname.get(),self.lname.get()), parent=self.memberframe)) == True:
            self.member_delete_button.config(state=DISABLED)
            self.member_update_button.config(state=DISABLED)
            if self.password_entry.get('1.0', 'end-1c') != '********' and self.password_entry.get('1.0', 'end-1c') != '':
                self.df3.loc[self.df3['USER'] == self.username.get(
                ), 'PASSWORD'] = self.password_entry.get('1.0', 'end-1c')
            self.df3.loc[self.df3['USER'] == self.username.get(
            ), 'NAME'] = self.fname_entry.get('1.0', 'end-1c')
            self.df3.loc[self.df3['USER'] == self.username.get(
            ), 'LNAME'] = self.lname_entry.get('1.0', 'end-1c')
            self.df3.loc[self.df3['USER'] == self.username.get(
            ), 'GENDER'] = self.gender_entry.get('1.0', 'end-1c')
            self.df3.loc[self.df3['USER'] == self.username.get(
            ), 'BIRTHDAY'] = self.birthday_entry.get('1.0', 'end-1c')
            self.df3.loc[self.df3['USER'] == self.username.get(
            ), 'EMAIL'] = self.email_entry.get('1.0', 'end-1c')
            self.df3.loc[self.df3['USER'] == self.username.get(
            ), 'TEL'] = self.tel_entry.get('1.0', 'end-1c')
            self.df3.to_csv("login.csv", index=False)
            ### Treeview Update
            self.member_treeview.delete(*self.member_treeview.get_children())
            treeview = pandas.read_csv('login.csv')
            treeview_update = treeview.values.tolist()
            for i in treeview_update:
                self.member_treeview.insert('', 'end', values=[i[0],i[1],i[3],i[4],i[5],i[6],i[7],i[8],i[2]])
    ##################################    Register Button   <Member Page>  #######################################################
    def add_member(self):
         #------------------------------    init     ------------------------------------------------------------#
        self.add_member_screen = Toplevel(self.memberframe)
        self.add_member_screen.title("Register member")
        self.add_member_screen.focus_set()
        self.add_member_screen.grab_set()
        self.add_member_screen.resizable(0, 0)
        x = (960) - (620/2)
        y = (540) - (310/2)
        self.add_member_screen.geometry("620x260+%d+%d" % (x, y))

        #------------------------------    Detail Plane     ------------------------------------------------------------#
        self.add_member_frame = LabelFrame(
            self.add_member_screen, text='Details')
        Label(self.add_member_frame, text="Username").grid(
            row=0, column=0, padx=10, pady=5, sticky="E")
        self.addmember_username_entry = Text(self.add_member_frame, width=20, height=1)
        self.addmember_username_entry.insert(1.0, '')
        self.addmember_username_entry.grid(row=0, column=1, padx=10, pady=5)
        Label(self.add_member_frame, text="Password").grid(
            row=1, column=0, padx=10, pady=5, sticky="E")
        self.addmember_pass_entry = Text(self.add_member_frame, width=20, height=1)
        self.addmember_pass_entry.insert(1.0, '')
        self.addmember_pass_entry.grid(row=1, column=1, padx=10, pady=5)
        Label(self.add_member_frame, text="Confrimpassword").grid(
            row=2, column=0, padx=10, pady=5, sticky="E")
        self.addmember_cpass_entry = Text(self.add_member_frame, width=20, height=1)
        self.addmember_cpass_entry.insert(1.0, '')
        self.addmember_cpass_entry.grid(
            row=2, column=1, padx=10, pady=5)
        Label(self.add_member_frame, text="Firstname").grid(
            row=0, column=2, padx=10, pady=5, sticky="E")
        self.addmember_fname_entry = Text(
            self.add_member_frame, width=20, height=1)
        self.addmember_fname_entry.insert(1.0, '')
        self.addmember_fname_entry.grid(
            row=0, column=3, padx=10, pady=5)
        Label(self.add_member_frame, text="Lastname").grid(
            row=1, column=2, padx=10, pady=5, sticky="E")
        self.addmember_lname_entry = Text(
            self.add_member_frame, width=20, height=1)
        self.addmember_lname_entry.insert(1.0, '')
        self.addmember_lname_entry.grid(
            row=1, column=3, padx=10, pady=5)
        Label(self.add_member_frame, text="Gender").grid(
            row=3, column=0, padx=10, pady=5, sticky="E")
        self.addmember_gender_entry = Text(
            self.add_member_frame, width=20, height=1)
        self.addmember_gender_entry.insert(1.0, '')
        self.addmember_gender_entry.grid(row=3, column=1, padx=10, pady=5)
        Label(self.add_member_frame, text="Birthday").grid(
            row=4, column=0, padx=10, pady=5, sticky="E")
        self.addmember_birthday_entry = Text(self.add_member_frame, width=20, height=1)
        self.addmember_birthday_entry.insert(1.0, '')
        self.addmember_birthday_entry.grid(row=4, column=1, padx=10, pady=5)
        Label(self.add_member_frame, text="Email").grid(
            row=3, column=2, padx=10, pady=5, sticky="E")
        self.addmember_email_entry = Text(self.add_member_frame, width=20, height=1)
        self.addmember_email_entry.insert(1.0, '')
        self.addmember_email_entry.grid(
            row=3, column=3, padx=10, pady=5)
        Label(self.add_member_frame, text="Phonenumber").grid(
            row=2, column=2, padx=10, pady=5, sticky="E")
        self.addmember_tel_entry = Text(
            self.add_member_frame, width=20, height=1)
        self.addmember_tel_entry.insert(1.0, '')
        self.addmember_tel_entry.grid(row=2, column = 3, padx=10, pady=5)


        #------------------------------    Option Detail Plane     ------------------------------------------------------------#
        self.add_member_option_frame = LabelFrame(self.add_member_screen, text='')
        self.clear_addmember_button = Button(
            self.add_member_option_frame, text='Clear',command=self.clear_addmember)
        self.clear_addmember_button.grid(row=0, column=0, padx=12, pady=0)
        self.save_addmember_button = Button(
            self.add_member_option_frame, text='Save',command=self.save_member)
        self.save_addmember_button.grid(row=0, column=1, padx=12, pady=0)


        self.add_member_option_frame.place(x=410, y=200, height=50, width=200)
        self.add_member_frame.place(x=10, y=10, height=190, width=600)
    def clear_addmember(self):
        if(messagebox.askokcancel("Confirmation", "Are you sure?", parent=self.add_member_screen)) == True:
            self.addmember_username_entry.delete('1.0', END)
            self.addmember_pass_entry.delete('1.0', END)
            self.addmember_cpass_entry.delete('1.0', END)
            self.addmember_fname_entry.delete('1.0', END)
            self.addmember_lname_entry.delete('1.0', END)
            self.addmember_gender_entry.delete('1.0', END)
            self.addmember_birthday_entry.delete('1.0', END)
            self.addmember_email_entry.delete('1.0', END)
            self.addmember_tel_entry.delete('1.0', END)
    def save_member(self):
        if self.addmember_username_entry.get('1.0', 'end-1c') != '' and self.addmember_pass_entry.get('1.0', 'end-1c') != '' and self.addmember_cpass_entry.get('1.0', 'end-1c') != '' and self.addmember_fname_entry.get('1.0', 'end-1c') != '' and self.addmember_lname_entry.get('1.0', 'end-1c') != '' and self.addmember_gender_entry.get('1.0', 'end-1c') != '' and self.addmember_birthday_entry.get('1.0', 'end-1c') != '' and self.addmember_email_entry.get('1.0', 'end-1c') != '' and self.addmember_tel_entry.get('1.0', 'end-1c') != '' :
            if(messagebox.askokcancel("Confirmation", "Are you sure?", parent=self.add_member_screen)) == True:
                with open('login.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['F',self.addmember_username_entry.get('1.0', 'end-1c'), self.addmember_pass_entry.get('1.0', 'end-1c'),
                                    self.addmember_fname_entry.get('1.0', 'end-1c').capitalize(), self.addmember_lname_entry.get('1.0', 'end-1c').capitalize(), self.addmember_gender_entry.get('1.0', 'end-1c'),self.addmember_birthday_entry.get('1.0', 'end-1c'), self.addmember_email_entry.get('1.0', 'end-1c'), str(self.addmember_tel_entry.get('1.0', 'end-1c')),'account'])
                self.addmember_username_entry.delete('1.0', END)
                self.addmember_pass_entry.delete('1.0', END)
                self.addmember_cpass_entry.delete('1.0', END)
                self.addmember_fname_entry.delete('1.0', END)
                self.addmember_lname_entry.delete('1.0', END)
                self.addmember_gender_entry.delete('1.0', END)
                self.addmember_birthday_entry.delete('1.0', END)
                self.addmember_email_entry.delete('1.0', END)
                self.addmember_tel_entry.delete('1.0', END)
                self.add_member_screen.destroy()
                messagebox.showinfo("Alert", "Register Sucessfully!!")
        else:
            messagebox.showerror("Error", "Please fill out all fields required", parent=self.add_member_screen)

    def destoryframe(self):
        self.orderframe.destroy()
        self.orderhistoryframe.destroy()
        self.menberframe.destroy()
        self.bookframe.destroy()


def showAdminPage():
    run = main_admin_screen()


if __name__ == '__main__':
    showAdminPage()
