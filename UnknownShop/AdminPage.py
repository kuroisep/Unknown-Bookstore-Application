import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter.ttk import *
from tkinter import ttk
import pandas
import datetime

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

class main_admin_screen:
    def __init__(self):
        self.admin_window = tk.Tk()
        self.admin_window.title("Unknown Book Store // Admin")
        x = (700) - (750/2)
        y = (420) - (500/2)
        self.admin_window.geometry("1280x720+%d+%d" % (x, y))
        bg_path = "UnknownShop\Picture\PaymentPage\Infobook_BG.png"
        bg = ImageTk.PhotoImage(Image.open(bg_path).resize((1280, 720)))

        #LOGO
        img_logo_path = "Shop_Page\PICTURE\logo.png"
        self.img_logo = ImageTk.PhotoImage(Image.open(img_logo_path).resize((150, 150)))
        Label(image=self.img_logo).place(x=0,y=0)

        self.menubar()
        


        """ 
        THEAM
        """
        style = ttk.Style(self.admin_window)
        style.configure('Treeview', rowheight=30)
        # style.configure("TButton", foreground="blue", background="orange")
        # Import the tcl file
        # self.admin_window.tk.call('source', 'UnknownShop/azure.tcl')

        # Set the theme with the theme_use method
        # style.theme_use('azure')
        """ 
        THEAM
        """

        ###############################    OrderPage     #######################################################
        self.OrderTime = StringVar()
        self.OrderID = StringVar()
        self.Customer = StringVar()
        self.Address = StringVar()
        self.Total = StringVar()
        self.Status = StringVar()

        ###############################    Database     #######################################################
        self.df = pandas.read_csv('login.csv')

        self.admin_window.resizable(0, 0)
        self.admin_window.mainloop()
    
    def menubar(self):
        #Menubar
        menuframe = LabelFrame(self.admin_window , text="Menu")
        menuframe.place(x=2, y=150, height=570, width=200)
        Button(menuframe, text='Check Order',width=27,command=self.orderPage).grid(row=0,padx=5,pady=10)
        Button(menuframe, text='Book management',width=27,command=self.bookPage).grid(row=1,padx=5,pady=10)
        Button(menuframe, text='Member management',width=27,command=self.menberPage).grid(row=2,padx=5,pady=10)
        Button(menuframe, text='Admin',width=27).grid(row=3,padx=5,pady=10)


    def orderPage(self):
        self.orderframe = LabelFrame(self.admin_window , text="Order Management")
        self.order_table_frame = LabelFrame(self.orderframe)
        ###############################    Table Plane     #######################################################
        columns = ("Order Time","Order ID","Customer","Address","Total","Status")
        self.order_treeview = Treeview(self.order_table_frame, column=columns, show="headings", height="20")
        yscrollbar = ttk.Scrollbar(self.order_table_frame, orient="vertical", command=self.order_treeview.yview)
        self.order_treeview.config(yscrollcommand=yscrollbar.set)
        yscrollbar.pack(side="right", fill="y")
        self.order_treeview.bind("<ButtonRelease-1>", self.orderPage_lookuptreeview)
        for col in columns:
            self.order_treeview.heading(col, text=col,command=lambda _col=col: self.treeview_sort_column(self.order_treeview, _col, False))

        self.order_treeview.column(0, anchor='center', width=150)
        self.order_treeview.column(1, anchor='center', width=100)
        self.order_treeview.column(2, anchor='center', width=150)
        self.order_treeview.column(3, anchor='w', width=250)
        self.order_treeview.column(4, anchor='center', width=100)
        self.order_treeview.column(5, anchor='center', width=150)

        # self.order_treeview.insert('', 'end', values=['Timestamp','Order ID','Name ',"Address","Order Total","status"])
        self.order_treeview.insert('', 'end', values=['A','1','Name '])
        self.order_treeview.insert('', 'end', values=['C','3','Name '])
        self.order_treeview.insert('', 'end', values=['D','4','Name '])
        self.order_treeview.insert('', 'end', values=['B','0','Name ','212 LA','5 items','Payment confirmed'])
        for i in range(1,100):
            self.order_treeview.insert('', 'end', values=[100-i,i,'Name ','212 LA','5 items','Payment confirmed'])
        
        

        self.order_treeview.pack()
        self.order_table_frame.place(x=20,y=10,height=400, width=1000)

        ###############################    Detail Plane     #######################################################
        self.order_detail_frame = LabelFrame(self.orderframe , text="Details")

        Label(self.order_detail_frame, text="Order ID#").grid(row=0, column=0, padx=10, pady=5,sticky="E")
        self.order_id_entry = Text(self.order_detail_frame,width=20,height=1)
        self.order_id_entry.insert(1.0,'')
        self.order_id_entry.grid(row=0, column=1, padx=10, pady=5)

        Label(self.order_detail_frame, text="Customer :").grid(row=1, column=0, padx=10, pady=5,sticky="E")
        self.order_user_entry = Text(self.order_detail_frame,width=20,height=1)
        self.order_user_entry.insert(1.0,'')
        self.order_user_entry.grid(row=1, column=1, padx=10, pady=5)

        Label(self.order_detail_frame, text="Order Time :").grid(row=2, column=0, padx=10, pady=5,sticky="E")
        self.order_ordertime_entry = Text(self.order_detail_frame,width=20,height=1)
        self.order_ordertime_entry.insert(1.0,'')
        self.order_ordertime_entry.grid(row=2, column=1, padx=10, pady=5)

        Label(self.order_detail_frame, text="Ship Time :").grid(row=3, column=0, padx=10, pady=5,sticky="E")
        self.order_shiptime_entry = Text(self.order_detail_frame,width=20,height=1)
        self.order_shiptime_entry.insert(1.0,'')
        self.order_shiptime_entry.grid(row=3, column=1, padx=10, pady=5)

        Label(self.order_detail_frame, text="Completed Time :").grid(row=4, column=0, padx=10, pady=5,sticky="E")
        self.order_completedtime_entry = Text(self.order_detail_frame,width=20,height=1)
        self.order_completedtime_entry.insert(1.0,'')
        self.order_completedtime_entry.grid(row=4, column=1, padx=10, pady=5)

        Label(self.order_detail_frame, text="Address :").grid(row=0, column=2, padx=10, pady=5,sticky="E")
        self.order_address_entry = Text(self.order_detail_frame,width=20, height=5)
        self.order_address_entry.insert(1.0,'')
        self.order_address_entry.grid(row=0, column=3, padx=10, pady=5,sticky="W",rowspan = 3)

        Label(self.order_detail_frame, text="Order Status :").grid(row=3, column=2, padx=10, pady=5,sticky="E")
        self.order_status_entry = Combobox(self.order_detail_frame,value=['Payment confirmed','Waiting for shipment','Shipped','Delivered','Cancelled order'])
        self.order_status_entry.insert(0,'')
        
        self.order_status_entry.grid(row=3, column=3, padx=10, pady=5,sticky="W")



        self.order_detail_frame.place(x=20,y=430,height=200, width=700)

        ###############################    Option Plane     #######################################################
        self.order_option_frame = LabelFrame(self.orderframe , text="Option")
        self.order_update_button = Button(self.order_option_frame,text='Update',command=self.orderPage_update_state,state=DISABLED)
        self.order_update_button.grid(row=0, column=1, padx=10, pady=5)
        self.order_option_frame.place(x=750,y=430,height=200, width=250)





        
        self.orderframe.place(x=220,y=20,height=700, width=1040)

    def orderPage_update_state(self):
        self.nowtime = datetime.datetime.now()
        if(messagebox.askokcancel("Confirmation", "Update OrderID {} ?".format(self.OrderID.get()), parent=self.orderframe)) == True:
            self.order_update_button.config(state=DISABLED)
            if self.order_status_entry.get() == 'Shipped':
                self.order_shiptime_entry.delete('1.0',END)
                self.order_shiptime_entry.insert(1.0,self.nowtime.strftime("%Y-%m-%d %H:%M:%S"))
                focused = self.order_treeview.focus()
                self.order_treeview.insert("", str(focused)[1:], values=("", str(self.order_status_entry)))
                self.order_treeview.delete(focused)
            elif self.order_status_entry.get() == 'Delivered':
                self.order_completedtime_entry.delete('1.0',END)
                self.order_completedtime_entry.insert(1.0,self.nowtime.strftime("%Y-%m-%d %H:%M:%S"))

    def orderPage_lookuptreeview(self,event):
        self.order_update_button.config(state=NORMAL)
        curItem = self.order_treeview.focus()
        cur = self.order_treeview.item(curItem)['values']
        # print('cur:',cur)
        if cur == '':
            return
        if len(cur) != 6:
            for i in range(6-len(cur)):
                cur.append('')
        self.OrderTime.set(cur[0])
        self.OrderID.set(cur[1])
        self.Customer.set(cur[2])
        self.Address.set(cur[3])
        self.Total.set(cur[4])
        self.Status.set(cur[5])    
        self.orderPage_detailupdate()
    def orderPage_detailupdate(self):
        self.order_id_entry.delete('1.0',END)
        self.order_user_entry.delete('1.0',END)
        self.order_ordertime_entry.delete('1.0',END)
        self.order_completedtime_entry.delete('1.0',END)
        self.order_shiptime_entry.delete('1.0',END)
        self.order_address_entry.delete('1.0',END)
        self.order_status_entry.delete(0,END)
        self.order_id_entry.insert(1.0,self.OrderID.get())
        self.order_user_entry.insert(1.0,self.Customer.get())
        self.order_ordertime_entry.insert(1.0,'Order Time')
        self.order_shiptime_entry.insert(1.0,'Ship Time')
        self.order_completedtime_entry.insert(1.0,'Completed Time')
        self.order_address_entry.insert(1.0,self.Address.get())
        self.order_status_entry.insert(0,self.Status.get())

    def treeview_sort_column(self,tv, col, reverse):
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)

        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)

        # reverse sort next time
        tv.heading(col, command=lambda _col=col: self.treeview_sort_column(tv, _col, not reverse))





    def bookPage(self):
        self.bookframe = LabelFrame(self.admin_window , text="Book Management")
        self.bookframe.place(x=220,y=20,height=700, width=1040)
        
    def menberPage(self):
        self.menberframe = LabelFrame(self.admin_window , text="Member Management")
        self.menberframe.place(x=220,y=20,height=700, width=1040)




def showAdminPage():
    run = main_admin_screen()



if __name__ == '__main__':
    showAdminPage()