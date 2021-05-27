from logging import disable
import tkinter as tk
from tkinter import *
from tkinter import ttk, Tk, Label
from PIL import ImageTk, Image
from tkinter.ttk import *
from tkinter import filedialog, messagebox
import pandas,csv
import os, sys
import re
import cv2
import datetime
from tkinter.filedialog import SaveFileDialog, askopenfilename
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import mysql.connector

from UnknownShop import LoginPage
import pandas as pd
from time import sleep
import time
from ttkthemes.themed_tk import ThemedTk
from ttkthemes import ThemedStyle
from tkinter.font import Font
import tkinter
import Pmw


class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.next = new_node.prev = new_node
            self.head = new_node
            return

        last = self.head.prev
        new_node = Node(data)

        new_node.next = self.head
        self.head.prev = new_node
        new_node.prev = last
        last.next = new_node

class Shop_main_screen:
    def __init__(self):
        self.shop_window = tk.Tk()
        self.shop_window.protocol("WM_DELETE_WINDOW", self.deleteX_show_window)
        self.shop_window.title("Unknown Book Store")
        x = (700) - (750/2)
        y = (420) - (500/2)
        self.shop_window.geometry("1280x720+%d+%d" % (x, y))
        # Create Canvas
        self.canvas = Canvas(self.shop_window, width=1280, height=720, bd=0, highlightthickness=0)
        self.myfont = 'TRACK'
        # self.pathcursor = ImageTk.PhotoImage(Image.open(pathcursor).resize((50, 50)))
        self.shop_window.configure(cursor='watch')

        # Variable Book
        self.No = StringVar()
        self.Name = StringVar()
        self.Author = StringVar()
        self.Category = StringVar()
        self.Language = StringVar()
        self.Price = StringVar()
        self.Code = StringVar()
        self.Rating = StringVar()
        self.Example = StringVar()
        self.confirm_order = False
        self.confirm_next = False
        self.order_id = 0
        self.payment_check = False
        self.total2 = StringVar(self.shop_window)
        self.total_amount = StringVar()


        self.review_Code = StringVar()
        self.review_Name = StringVar()
        self.review_Author = StringVar()
        self.review_Category = StringVar()
        self.review_Price = StringVar()


       
        # """ 
        # THEAM
        # """
        # style = ttk.Style(self.shop_window)
        # # Import the tcl file
        # self.shop_window.tk.call('source', 'UnknownShop/azure.tcl')


        style = ThemedStyle(self.shop_window)
        style.configure('resize1.TSpinbox', arrowsize=25)
        # style.set_theme("adapta")
        # style.set_theme("yaru")


        # # Set the theme with the theme_use method
        # style.theme_use('azure')
        # style.configure('flat.TButton', borderwidth=0)
        # # style.configure("Treeview", font=('TRACK',13,'bold'))
        # """ 
        # THEAM
        # """
      

        #USER LOGIN
        self.df = pandas.read_csv('login.csv')
        self.user = self.df.loc[self.df['STATUS']=='T'].values.tolist()
        self.user_imagefile = ''
        self.usercart = []
        if self.user == []:
            # messagebox.showerror("Error", "NO USER LOGIN FOUND")
            print("NO USER LOGIN FOUND")
            self.user = [['T', '\" Login Required \"', '', 
            'You are not logged in', 'You are not logged in', 
            '-','-/-/-', 'You are not logged in', 
            'You are not logged in','account']]
        #self.user[0][1] = username
        #self.user[0][2] = password
        #self.user[0][3] = name
        #self.user[0][4] = lastname
        #self.user[0][5] = gender
        #self.user[0][6] = birthday
        #self.user[0][7] = email
        #self.user[0][8] = telphone
        #self.user[0][9] = picture


        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Load data book >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.loadbookfile = pandas.read_csv('UnknownShop\database\DataBookList.csv')
        self.book_data = self.loadbookfile.values.tolist()

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.show_HomePage()

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.infomationPage() # หน้า info 
        self.categoryPage()
        self.paymentPage()
        self.deliveryPage()
        self.create_background()
        self.search_bar()
        self.shift()
        self.menuTab()
        
        ## <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # self.set_banner()
        self.count = 0
        self.moveBanner()
        ## <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
        self.show_HomePage()

        self.button_state()

        self.shop_window.resizable(0, 0)
        self.shop_window.overrideredirect(1)
        self.shop_window.mainloop()

    def create_background(self): # <<<<<<<<<<<<<<<<<<<<<<<<<<< BG
        self.bg_path = "UnknownShop/Picture/ShopPage/BG1.png" 
        self.bg = ImageTk.PhotoImage(Image.open(self.bg_path).resize((1280, 720)))

        # self.canvas = Canvas(self.shop_window, width=1280, height=720)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg,anchor="nw")

        self.bgg_path = "UnknownShop/Picture/ShopPage/BG2.png" 
        self.bgg = ImageTk.PhotoImage(Image.open(self.bgg_path).resize((1280, 720)))
    
    def search_bar(self):
        
        Frame1 = tk.LabelFrame(self.shop_window, borderwidth=0, highlightthickness=0, bg="#12aadb")
        Frame1.place(x=0, y=65, height=40, width=1280)

        searchLabel0 = tk.Label(Frame1, text="", font=('TRACK', 12), bg="#12aadb")
        searchLabel0.pack(side= LEFT, padx=125, pady=10, anchor=CENTER)

        searchLabel = tk.Label(Frame1, text="Search By", font=('TRACK', 12),bg="#12aadb")
        searchLabel.pack(side= LEFT, padx=5, pady=10, anchor=CENTER)

        self.drop1 = ttk.Combobox(Frame1, width=10, value=["All","Arts / Design / Decoration", "Literature", 
                                                                "Administration / Management", "Humanities / Science", 
                                                                "Children's Books","Career Academic Textbooks", "Psychology"])
        self.drop1.current((0))
        # drop1.place(x=345, y=100)
        self.drop1.pack(side= LEFT, padx=5, pady=10, anchor=CENTER)

        self.drop2 = ttk.Combobox(Frame1, width=10, value=["Name", "Code", "Author"])
        self.drop2.current((0))
        # drop2.place(x=440, y=100)
        self.drop2.pack(side= LEFT, padx=5, pady=10, anchor=CENTER)

        self.nameEntered = tk.Entry(Frame1, width = 50)
        # nameEntered.place(x=535, y=100)
        self.nameEntered.pack(side= LEFT, padx=5, pady=10, anchor=CENTER)

        search_button = tk.Button(Frame1, text = "Search", command = self.search ,height=10, width=10)
        # search_button.place(x=855, y=100)
        search_button.pack(side=LEFT, padx=5, pady=10, anchor=CENTER)

        show_all_books_button = tk.Button(Frame1, text = "Clear",command = self.Cclear_SearchBox, height=10, width=10)
        # show_all_books_button.place(x=943, y=100)
        show_all_books_button.pack(side= LEFT, padx=5, pady=10, anchor=CENTER)

    def search(self):
        self.show_categoryPage()

        self.book_treeview.delete(*self.book_treeview.get_children())
        for i in self.book_data:
                self.book_treeview.insert('', 'end', values = [i][0])

        selected = self.drop1.get()
        selected2 = self.drop2.get()

        # print(selected, selected2)

        query = str(self.nameEntered.get())
        selections = []
        for child in self.book_treeview.get_children(''):
            # print(self.book_treeview.item(child)['values'][2])
            if (query.lower() in str(self.book_treeview.item(child)['values'][2]).lower()) and (selected == "All") and (selected2 == "Name"):
                selections.append(self.book_treeview.item(child)['values'])
            elif (query.lower() in str(self.book_treeview.item(child)['values'][2]).lower()) and (selected == "Arts / Design / Decoration") and (selected2 == "Name") and (str(self.book_treeview.item(child)['values'][4]) == "Arts / Design / Decoration"):
                selections.append(self.book_treeview.item(child)['values'])
            elif (query.lower() in str(self.book_treeview.item(child)['values'][2]).lower()) and (selected == "Literature") and (selected2 == "Name") and (str(self.book_treeview.item(child)['values'][4]) == "Literature"):
                selections.append(self.book_treeview.item(child)['values'])
            elif (query.lower() in str(self.book_treeview.item(child)['values'][2]).lower()) and (selected == "Administration / Management") and (selected2 == "Name") and (str(self.book_treeview.item(child)['values'][4]) == "Administration / Management"):
                selections.append(self.book_treeview.item(child)['values'])
            elif (query.lower() in str(self.book_treeview.item(child)['values'][2]).lower()) and (selected == "Humanities / Science") and (selected2 == "Name") and (str(self.book_treeview.item(child)['values'][4]) == "Humanities / Science"):
                selections.append(self.book_treeview.item(child)['values'])
            elif (query.lower() in str(self.book_treeview.item(child)['values'][2]).lower()) and (selected == "Children's Books") and (selected2 == "Name") and (str(self.book_treeview.item(child)['values'][4]) == "Children's Books"):
                selections.append(self.book_treeview.item(child)['values'])
            elif (query.lower() in str(self.book_treeview.item(child)['values'][2]).lower()) and (selected == "Career Academic Textbooks") and (selected2 == "Name") and (str(self.book_treeview.item(child)['values'][4]) == "Career Academic Textbooks"):
                selections.append(self.book_treeview.item(child)['values'])
            elif (query.lower() in str(self.book_treeview.item(child)['values'][2]).lower()) and (selected == "Psychology") and (selected2 == "Name") and (str(self.book_treeview.item(child)['values'][4]) == "Psychology"):
                selections.append(self.book_treeview.item(child)['values'])

            elif (query.lower() in str(self.book_treeview.item(child)['values'][1]).lower()) and (selected == "All") and (selected2 == "Code"):
                selections.append(self.book_treeview.item(child)['values'])
            elif (query.lower() in str(self.book_treeview.item(child)['values'][1]).lower()) and (selected == "Arts / Design / Decoration") and (selected2 == "Code") and (str(self.book_treeview.item(child)['values'][4]) == "Arts / Design / Decoration"):
                selections.append(self.book_treeview.item(child)['values'])
            elif (query.lower() in str(self.book_treeview.item(child)['values'][1]).lower()) and (selected == "Literature") and (selected2 == "Code") and (str(self.book_treeview.item(child)['values'][4]) == "Literature"):
                selections.append(self.book_treeview.item(child)['values'])
            elif (query.lower() in str(self.book_treeview.item(child)['values'][1]).lower()) and (selected == "Administration / Management") and (selected2 == "Code") and (str(self.book_treeview.item(child)['values'][4]) == "Administration / Management"):
                selections.append(self.book_treeview.item(child)['values'])
            elif (query.lower() in str(self.book_treeview.item(child)['values'][1]).lower()) and (selected == "Humanities / Science") and (selected2 == "Code") and (str(self.book_treeview.item(child)['values'][4]) == "Humanities / Science"):
                selections.append(self.book_treeview.item(child)['values'])
            elif (query.lower() in str(self.book_treeview.item(child)['values'][1]).lower()) and (selected == "Children's Books") and (selected2 == "Code") and (str(self.book_treeview.item(child)['values'][4]) == "Children's Books"):
                selections.append(self.book_treeview.item(child)['values'])
            elif (query.lower() in str(self.book_treeview.item(child)['values'][1]).lower()) and (selected == "Career Academic Textbooks") and (selected2 == "Code") and (str(self.book_treeview.item(child)['values'][4]) == "Career Academic Textbooks"):
                selections.append(self.book_treeview.item(child)['values'])
            elif (query.lower() in str(self.book_treeview.item(child)['values'][1]).lower()) and (selected == "Psychology") and (selected2 == "Code") and (str(self.book_treeview.item(child)['values'][4]) == "Psychology"):
                selections.append(self.book_treeview.item(child)['values'])

            elif (query.lower() in str(self.book_treeview.item(child)['values'][3]).lower()) and (selected == "All") and (selected2 == "Author"):
                selections.append(self.book_treeview.item(child)['values'])
            elif (query.lower() in str(self.book_treeview.item(child)['values'][3]).lower()) and (selected == "Arts / Design / Decoration") and (selected2 == "Author") and (str(self.book_treeview.item(child)['values'][4]) == "Arts / Design / Decoration"):
                selections.append(self.book_treeview.item(child)['values'])
            elif (query.lower() in str(self.book_treeview.item(child)['values'][3]).lower()) and (selected == "Literature") and (selected2 == "Author") and (str(self.book_treeview.item(child)['values'][4]) == "Literature"):
                selections.append(self.book_treeview.item(child)['values'])
            elif (query.lower() in str(self.book_treeview.item(child)['values'][3]).lower()) and (selected == "Administration / Management") and (selected2 == "Author") and (str(self.book_treeview.item(child)['values'][4]) == "Administration / Management"):
                selections.append(self.book_treeview.item(child)['values'])
            elif (query.lower() in str(self.book_treeview.item(child)['values'][3]).lower()) and (selected == "Humanities / Science") and (selected2 == "Author") and (str(self.book_treeview.item(child)['values'][4]) == "Humanities / Science"):
                selections.append(self.book_treeview.item(child)['values'])
            elif (query.lower() in str(self.book_treeview.item(child)['values'][3]).lower()) and (selected == "Children's Books") and (selected2 == "Author") and (str(self.book_treeview.item(child)['values'][4]) == "Children's Books"):
                selections.append(self.book_treeview.item(child)['values'])
            elif (query.lower() in str(self.book_treeview.item(child)['values'][3]).lower()) and (selected == "Career Academic Textbooks") and (selected2 == "Author") and (str(self.book_treeview.item(child)['values'][4]) == "Career Academic Textbooks"):
                selections.append(self.book_treeview.item(child)['values'])
            elif (query.lower() in str(self.book_treeview.item(child)['values'][3]).lower()) and (selected == "Psychology") and (selected2 == "Author") and (str(self.book_treeview.item(child)['values'][4]) == "Psychology"):
                selections.append(self.book_treeview.item(child)['values'])
        # self.book_treeview.selection_set(selections)
        self.book_treeview.delete(*self.book_treeview.get_children())
        for i in selections:
                self.book_treeview.insert('', 'end', values = [i][0])
        
    def Cclear_SearchBox(self):
        self.drop1.current((0))
        self.drop2.current((0))
        self.nameEntered.delete(0, 'end')
        # MB1 = messagebox.showinfo(message='Clear Done!')
        self.book_treeview.delete(*self.book_treeview.get_children())
        for i in self.book_data:
                self.book_treeview.insert('', 'end', values = [i][0])

    def menuTab_logo(self):
        # self.Frame0 = tk.LabelFrame(self.shop_window, borderwidth=0, highlightthickness=0, bg="#528cdb")
        # self.Frame0.place(x=0, y=0, height=75, width=100)
        img_logo_path = "UnknownShop\\Picture\\LoginPage\\black-logo.png"
        self.img_logo = ImageTk.PhotoImage(Image.open(img_logo_path).resize((82, 72)))
        self.canvas.create_image(2, 0, image=self.img_logo, anchor="nw")

    def menuTabEnter(self, event):
        self.label1.config(fg="#120896")
        self.closebutton.config(fg="red")

    def menuTabLeave(self, event):
        self.label1.config(fg="white")
        self.closebutton.config(fg="white")


    def menuTab(self):
        
        self.Frame1 = tk.LabelFrame(self.shop_window, borderwidth=0, highlightthickness=0, bg="#1265db")
        self.Frame1.place(x=100, y=0, height=30, width=1280)
        
        self.closebutton = tk.Button(self.Frame1, text='***',background="#1265db",fg="white", width=30, borderwidth=0, 
                                highlightthickness=0, font=('TRACK', 12),activebackground="#1265db", 
                                command = self.delete_show_window)
        
        self.closebutton.place(x=1000, y=5)
        self.closebutton.bind("<Enter>", self.menuTabEnter)
        self.closebutton.bind("<Leave>", self.menuTabLeave)


        self.label1 = tk.Label(self.Frame1, text = "Welcome to The Land of books. ~~~",font=('TRACK', 15),background="#1265db")
        self.label1.place(x=350, y=0)
        self.label1.bind("<Enter>", self.menuTabEnter)
        self.label1.bind("<Leave>", self.menuTabLeave)
       
        Frame2 = tk.LabelFrame(self.shop_window, borderwidth=0, highlightthickness=0, bg="#1200db")
        Frame2.place(x=100, y=30, height=35, width=1280)

        self.one_button = tk.Button(Frame2, text='HOME',background="#1200db",fg="white", width=30, borderwidth=0, highlightthickness=0, font=('TRACK', 12),activebackground="#1200db",command = self.show_HomePage
               ).grid(column=0, row=0, padx=10, pady=2)
        self.two_button = tk.Button(Frame2, text='My Profile', width=10,bg="#1200db",fg="white", borderwidth=0, highlightthickness=0, font=('TRACK', 12),activebackground="#1200db",command = self.show_infomationPage
               ).grid(column=1, row=0, padx=5, pady=0)
        self.three_button = tk.Button(Frame2, text='Shopping', width=10,bg="#1200db",fg="white", borderwidth=0, highlightthickness=0, font=('TRACK', 12),activebackground="#1200db",command= self.show_selected_categoryPages
               ).grid(column=2, row=0, padx=5, pady=0)
        self.four_button = tk.Button(Frame2, text='My Cart', width=10,bg="#1200db",fg="white", borderwidth=0, highlightthickness=0, font=('TRACK', 12),activebackground="#1200db",command=self.show_paymentPage
               ).grid(column=3,row=0, padx=5, pady=0)
        self.five_button = tk.Button(Frame2, text='Delivery Status', width=15,bg="#1200db",fg="white", borderwidth=0, highlightthickness=0, font=('TRACK', 12),activeforeground="#120896",command=self.show_deliveryPage
               ).grid(column=4,row=0, padx=5, pady=0)
        self.six_button = tk.Button(Frame2, text='Contact Us', width=10,fg="white", bg="#1200db", borderwidth=0, highlightthickness=0, font=('TRACK', 12),activeforeground="#120896",command= self.show_ContactUSPage
               ).grid(column=5,row=0, padx=5, pady=0)
        self.seven_button = tk.Button(Frame2, text='Logout', width=10,fg="white", bg="#1200db", borderwidth=0, highlightthickness=0, font=('TRACK', 12),activeforeground= "#120896",command= self.delete_show_window,
               ).grid(column=6,row=0, padx=5, pady=0)

        self.menuTab_logo()

    def click_manuTab(self):
        self.one_button.config(bg="#8ac126") 

    def value_set_one(self):
        self.value = 1

    def print_value(self):
        print(self.value)
        
    def button_state(self):
        pass
    
    def delete_show_window(self):
        if messagebox.askokcancel("Quit", "Do you want to sign out?"):
            self.df.loc[self.df['USER'] == self.user[0][1], 'STATUS'] = 'F'
            self.df.to_csv("login.csv", index=False)
            self.shop_window.destroy()
            LoginPage.showLoginPage()

    def deleteX_show_window(self):
        self.df.loc[self.df['USER'] == self.user[0][1], 'STATUS'] = 'F'
        self.df.to_csv("login.csv", index=False)
        self.shop_window.destroy()
       
    def HomePage(self):
        self.inner_HomePage = Canvas(self.canvas, width=1280, height=550)

        filename = "UnknownShop/Picture/ShopPage/BG1.png"
        self.filenameBG = ImageTk.PhotoImage(Image.open(filename))
        background_label = Label(self.inner_HomePage, image=self.filenameBG)
        background_label.place(x=641, y=207, anchor=CENTER)
       

        self.HomePageFrame1 = tk.LabelFrame(self.inner_HomePage , text="HomePage_BANNER")
        self.HomePageFrame1.place(x=100, y=10, height=350, width=1080)
        Label(self.HomePageFrame1,  image=self.bgg).place(x=530, y=187, anchor=CENTER)

        # self.inner_HomePageFrame1 = Canvas(self.HomePageFrame1, width=300, height=0)   
        # # self.inner_HomePageFrame1.create_window(0, 0)
        # self.inner_HomePageFrame1.pack()

        HomePageFrame2 = tk.LabelFrame(self.inner_HomePage , text="Selected Menu")
        HomePageFrame2.place(x=100, y=370, height=150, width=1080)
        Label(HomePageFrame2,  image=self.bgg).place(x=530, y=187, anchor=CENTER)

        path1 = "UnknownShop\\Picture\\ShopPage\\ICON\\bag.png"
        path2 = "UnknownShop\\Picture\\ShopPage\\ICON\\box.png"
        path3 = "UnknownShop\\Picture\\ShopPage\\ICON\\open-book.png"
        path4 = "UnknownShop\\Picture\\ShopPage\\ICON\\operator.png"

        self.p1 = ImageTk.PhotoImage(Image.open(path1).resize((85, 75)))
        self.p2 = ImageTk.PhotoImage(Image.open(path2).resize((85, 75)))
        self.p3 = ImageTk.PhotoImage(Image.open(path3).resize((85, 75)))
        self.p4 = ImageTk.PhotoImage(Image.open(path4).resize((85, 75)))
        # self.img_logo = ImageTk.PhotoImage(Image.open(path1).resize((85, 75)))
        # button.config(image=logo, compound=LEFT)
        # small_logo = logo.subsample(5, 5)
        # button.config(image=small_logo)

        # buy_button = tk.Button(HomePageFrame2,text="1", width=10)
        # buy_button.grid(row=0,column=0,padx=20, pady=5)
        # buy_button = tk.Button(HomePageFrame2,text="2", width=10)
        # buy_button.grid(row=1,column=0,padx=20, pady=5)    

        buy_button = tk.Button(HomePageFrame2,text="Buy Books",image=self.p1,width=200, command= self.show_selected_categoryPages, compound=TOP,pady=5)
        # buy_button.config(image=p1, compound=LEFT)
        # buy_button.grid(row=2,column=2,padx=80, pady=10)
        buy_button.place(x=120,y=5)

        Status_button = tk.Button(HomePageFrame2,text="Status",image=self.p2,width=200, command= self.show_deliveryPage, compound=TOP, pady=5)
        Status_button.place(x=330,y=5)

        Review_button = tk.Button(HomePageFrame2,text="Recommed Book",image=self.p3,width=200, command= self.recommend_book_page, compound=TOP, pady=5)
        Review_button.place(x=540,y=5)

        ContactUs_button = tk.Button(HomePageFrame2,text="Contact Us",image=self.p4,width=200,  command= self.show_ContactUSPage, compound=TOP, pady=5)
        ContactUs_button.place(x=750,y=5)

    def recommend_book_page(self):

        #vvvvvvvvvvvvvvvvvvvvvvv Data Structure [ Sort :Quicksort ] vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        def QuickSort(arr):
            elements = len(arr)
            #Base case
            if elements < 2:
                return arr
            current_position = 0 #Position of the partitioning element
            for i in range(1, elements): #Partitioning loop
                if arr[i] > arr[0]:
                    current_position += 1
                    temp = arr[i]
                    arr[i] = arr[current_position]
                    arr[current_position] = temp
            temp = arr[0]
            arr[0] = arr[current_position] 
            arr[current_position] = temp #Brings pivot to it's appropriate position
            left = QuickSort(arr[0:current_position]) #Sorts the elements to the left of pivot
            right = QuickSort(arr[current_position+1:elements]) #sorts the elements to the right of pivot
            arr = left + [arr[current_position]] + right #Merging everything together
            return arr
        loadorder_deatil = pandas.read_csv('UnknownShop\\database\\order_detail.csv')
        order_detail = loadorder_deatil.values.tolist()
        to_sort = []
        duplicate = False
        for i in order_detail:
            if str(i[5]) != 'nan':
                for j in to_sort:
                    if i[1] in j[1]:
                        j[0] = (float(j[0]) + float(i[5]))/2
                        round(j[0],2)
                        duplicate = True
                if not duplicate:
                    to_sort.append([i[5],i[1],i[2]])
        recommend_sorted = QuickSort(to_sort)
        #^^^^^^^^^^^^^^^^^^^^^^^^^^ Data Structure [ Sort : Quicksort ] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        #------------------------------    init     ------------------------------------------------------------#
        self.recommend_screen = Toplevel(self.inner_HomePage)
        self.recommend_screen.title("Recommend Book")
        self.recommend_screen.focus_set()
        self.recommend_screen.grab_set()
        self.recommend_screen.resizable(0, 0)
        x = (960) - (700/2)
        y = (540) - (550/2)
        self.recommend_screen.geometry("700x500+%d+%d" % (x, y))
        #------------------------------   Table Plane     ------------------------------------------------------------#
        self.recommend_book_frame = LabelFrame(self.recommend_screen)
        columns = ("No.",'Code','Title','Rating')
        self.recommend_book_treeview = Treeview(
            self.recommend_book_frame, column=columns, show="headings", height="20")
        yscrollbar = ttk.Scrollbar(
            self.recommend_book_frame, orient="vertical", command=self.recommend_book_treeview.yview)
        self.recommend_book_treeview.config(yscrollcommand=yscrollbar.set)
        yscrollbar.pack(side="right", fill="y")
        for col in columns:
            self.recommend_book_treeview.heading(col, text=col, command=lambda _col=col: self.treeview_sort_column(
                self.recommend_book_treeview, _col, False))

        self.recommend_book_treeview.column(0, anchor='center', width=50)
        self.recommend_book_treeview.column(1, anchor='center', width=80)
        self.recommend_book_treeview.column(2, anchor='center', width=450)
        self.recommend_book_treeview.column(3, anchor='center', width=50)

        index = 1
        for i in recommend_sorted:
            self.recommend_book_treeview.insert('', 'end', values=[index,i[1],i[2],i[0]])
            index += 1

        self.recommend_book_treeview.pack()
        self.recommend_book_frame.place(x=10, y=10, height=470, width=670)
 
    def set_banner(self):
        # # BANNER <<<<<<<<<<<<<<<<<<<<<<<<<<
        banner1_path = "Shop_Page\PICTURE\\banner1.jpg"
        banner2_path = "Shop_Page\PICTURE\\banner2.jpg"
        banner3_path = "Shop_Page\PICTURE\\banner3.jpg"
        self.banner1 = ImageTk.PhotoImage(Image.open(banner1_path))
        self.banner2 = ImageTk.PhotoImage(Image.open(banner2_path))
        self.banner3 = ImageTk.PhotoImage(Image.open(banner3_path))

        self.banner_label = tk.Label(self.HomePageFrame1 )
        self.banner_label.pack()

        dot1_path = "Shop_Page\PICTURE\movingdot1.png"
        dot2_path = "Shop_Page\PICTURE\movingdot2.png"
        dot3_path = "Shop_Page\PICTURE\movingdot3.png"
        self.dot1 = ImageTk.PhotoImage(Image.open(dot1_path))
        self.dot2 = ImageTk.PhotoImage(Image.open(dot2_path))
        self.dot3 = ImageTk.PhotoImage(Image.open(dot3_path))

        self.dot_label = tk.Label( self.HomePageFrame1 )
        self.dot_label.pack()

    def moveBanner(self):
        global after_id
    
        if self.count == 30 :
            self.count = 0

        if self.count == 0 :
            self.banner_label.config(image = self.banner1)
            self.dot_label.config(image = self.dot1)
            self.canvas.create_image(700,300,image=self.banner1)
            self.canvas.create_image(700,475,image=self.dot1)
            self.banner_label.place()
            self.dot_label.place()
        elif self.count == 10 :
            self.banner_label.config(image = self.banner2)
            self.canvas.create_image(700,300,image=self.banner2)
            self.canvas.create_image(700,475,image=self.dot2)
            self.dot_label.config(image = self.dot2)
        elif self.count == 20 :
            self.banner_label.config(image = self.banner3)
            self.canvas.create_image(700,300,image=self.banner3)
            self.canvas.create_image(700,475,image=self.dot3)
            self.dot_label.config(image = self.dot3)
        self.count += 1
        after_id = self.banner_label.after(200, self.moveBanner)

    def infomationPage(self): # ข้อมูลหน้า info       #1
        
        self.inner_infomation = Canvas(self.canvas, width=1280, height=550)
        
        filename = "UnknownShop/Picture/ShopPage/BG1.png"
        self.filenameBG = ImageTk.PhotoImage(Image.open(filename))
        background_label = Label(self.inner_infomation, image=self.filenameBG)
        background_label.place(x=641, y=207, anchor=CENTER)

        infomationPageFrame1 = tk.LabelFrame(self.inner_infomation,borderwidth=0, highlightthickness=0,bg="#99aaff")
        infomationPageFrame1.place(x=100, y=0, height=550, width=1080)

        self.infomationPageFrame2 = tk.LabelFrame(infomationPageFrame1 , text="PICTURE",bg="#99aaff",borderwidth=0, highlightthickness=0)
        self.infomationPageFrame2.place(x=600, y=50, height=350, width=300)

        infomationPageFrame3 = tk.LabelFrame(infomationPageFrame1 , text="Info",bg="#99aaff",borderwidth=0, highlightthickness=0)
        infomationPageFrame3.place(x=200, y=50, height=400, width=365)

        infomationPageFrame4 = tk.LabelFrame(infomationPageFrame1 , text="Text Info",bg="#99aaff",borderwidth=0, highlightthickness=0)
        infomationPageFrame4.place(x=200, y= 420, height=100, width=700)

        infomationPage_custom_Frame1 = tk.LabelFrame(infomationPageFrame1, bg="#12aadb",borderwidth=0, highlightthickness=0,)
        infomationPage_custom_Frame1.place(x=0, y=0, height=550, width=100)

        infomationPage_custom_Frame2 = tk.LabelFrame(infomationPageFrame1, bg="#12fcdb",borderwidth=0, highlightthickness=0,)
        infomationPage_custom_Frame2.place(x=1000, y=0, height=550, width=280)


        if self.user != []:
            ## USERNAME
            username_text = Label(infomationPageFrame3, text="Username".format(self.user[0][1]), font = self.myfont)
            username1_text = Label(infomationPageFrame3, text=self.user[0][1],font = self.myfont)
            username_text.grid(row=0, column=0, padx=10, pady=10,sticky="W")
            username1_text.grid(row=0, column=1, padx=10, pady=5,sticky="W")
            ## NAME
            name_text = Label(infomationPageFrame3, text="Name",font = self.myfont)
            name_text.grid(row=1, column=0, padx=10, pady=5,sticky="W")
            self.name_entry = Entry(infomationPageFrame3,font = self.myfont)
            self.name_entry.insert(0,self.user[0][3])
            self.name_entry.config(state=DISABLED)
            self.name_entry.grid(row=1, column=1, padx=10, pady=5)
            ##LASTNAME
            lname_text = Label(infomationPageFrame3, text="Lastname",font = self.myfont)
            lname_text.grid(row=2, column=0, padx=10, pady=5,sticky="W")
            self.lname_entry = Entry(infomationPageFrame3,font = self.myfont)
            self.lname_entry.insert(0,self.user[0][4])
            self.lname_entry.config(state=DISABLED)
            self.lname_entry.grid(row=2, column=1, padx=10, pady=5)
            ##GENDER
            gender_text = Label(infomationPageFrame3, text="Gender",font = self.myfont)
            gender_text.grid(row=3, column=0, padx=10, pady=5,sticky="W")
            self.gender_entry = Combobox(infomationPageFrame3, width=8,value=['MALE','FEMALE'],font = self.myfont) 
            self.gender_entry.insert(0,self.user[0][5])
            self.gender_entry.config(state=DISABLED)
            self.gender_entry.grid(row=3, column=1, padx=10, pady=5,sticky="W")
            ##BIRTHDAY
                    #DATE
            birthday_text = Label(infomationPageFrame3, text="Birthday",font = self.myfont)
            birthday_text.grid(row=4, column=0, padx=10, pady=5,sticky="W")
            self.birthday_date_entry = Combobox(infomationPageFrame3, width=3,value=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
                                                                             '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', 
                                                                             '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],font = self.myfont) 
            self.birthday_date_entry.insert(0,self.user[0][6].split('/')[0])
            self.birthday_date_entry.config(state=DISABLED)
            self.birthday_date_entry.place(x=182, y=160)
                    #MONTH
            self.birthday_month_entry = Combobox(infomationPageFrame3, width=4, value=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                                                                                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] ,font = self.myfont)
            self.birthday_month_entry.insert(0,self.user[0][6].split('/')[1])
            self.birthday_month_entry.config(state=DISABLED)
            self.birthday_month_entry.place(x=236, y=160)
                    #YEAR
            year_list = []
            for i in range(1920,2022):
                year_list.append(str(i))
            self.birthday_year_entry = Combobox(infomationPageFrame3, width=4, value=year_list,font = self.myfont)
            self.birthday_year_entry.insert(0,self.user[0][6].split('/')[2])
            self.birthday_year_entry.config(state=DISABLED)
            self.birthday_year_entry.place(x=300, y=160)
            ##EMAIL
            email_text = Label(infomationPageFrame3, text="Email",font = self.myfont)
            email_text.grid(row=5, column=0, padx=10, pady=5,sticky="W")
            self.email_entry = Entry(infomationPageFrame3,font = self.myfont)
            self.email_entry.insert(0,self.user[0][7])
            self.email_entry.config(state=DISABLED)
            self.email_entry.grid(row=5, column=1, padx=10, pady=5)
            ##PHONE
            telphone_text = Label(infomationPageFrame3, text="Phone Number",font = self.myfont)
            telphone_text.grid(row=6, column=0, padx=10, pady=5,sticky="W")
            self.telphone_entry = Entry(infomationPageFrame3,font = self.myfont)
            self.telphone_entry.insert(0,self.user[0][8])
            self.telphone_entry.config(state=DISABLED)
            self.telphone_entry.grid(row=6, column=1, padx=10, pady=5)

            point_text = Label(infomationPageFrame3, text="Member Point(s)",font = self.myfont)
            point_text.grid(row=7, column=0, padx=10, pady=5,sticky="W")
            self.point_entry = Entry(infomationPageFrame3,font = self.myfont)
            self.point_entry.insert(0,self.user[0][9])
            self.point_entry.config(state=DISABLED)
            self.point_entry.grid(row=7, column=1, padx=10, pady=5)


            ##EDIT BUTTON
            Label(infomationPageFrame3, text="").grid(row=8, column=0, padx=10, pady=5)
            Label(infomationPageFrame3, text="").grid(row=8, column=1, padx=10, pady=5)
            self.edit_info_button = tk.Button(infomationPageFrame3,text='Edit', command=self.edit_infomation_state, width = 10)
            self.edit_info_button.grid(row=8, column=0, padx=35, pady=5)
            ##DONE BUTTON
            self.done_info_button = tk.Button(infomationPageFrame3,text='Done',state=DISABLED, command=self.edit_infomation_state, width = 10)
            self.done_info_button.grid(row=8, column=1, padx=10, pady=5)

            ##PICTURE
            image_path = "UnknownShop/Picture/ShopPage/USER_PIC/{}.png".format(self.user[0][9])
            self.user_img = ImageTk.PhotoImage(Image.open(image_path).resize((300, 300)))
            self.user_imginput = ''

            self.imageselect_info_button = tk.Button(self.infomationPageFrame2,text='select',state=DISABLED, command=self.openimage, width = 10 )
            self.imageselect_info_button.pack(side="bottom")
            self.user_image = Label(self.infomationPageFrame2, image=self.user_img)
            self.user_image.pack()
            
    def openfn(self):
        self.user_imagefile = filedialog.askopenfilename(initialdir='UnknownShop\\Picture\\ShopPage\\USER_PIC',title='open')
        return self.user_imagefile
    def openimage(self):
        self.user_imginput = self.openfn()
        if self.user_imginput != '':
            self.user_img = ImageTk.PhotoImage(Image.open(self.user_imginput).resize((300, 300)))
            self.user_image = Label(self.infomationPageFrame2, image=self.user_img)
            self.user_image.pack()
        
    def edit_infomation_state(self):
        if str(self.name_entry['state']) == 'disabled':
            self.name_entry.config(state=NORMAL)
            self.lname_entry.config(state=NORMAL)
            # self.gender_entry.config(state=NORMAL)
            self.birthday_date_entry.config(state=NORMAL)
            self.birthday_month_entry.config(state=NORMAL)
            self.birthday_year_entry.config(state=NORMAL)
            # self.email_entry.config(state=NORMAL)
            self.telphone_entry.config(state=NORMAL)
            self.edit_info_button.config(state=DISABLED)
            self.done_info_button.config(state=NORMAL)
            self.imageselect_info_button.config(state=NORMAL)
        else:
            self.edit_infomation_file()

    def edit_infomation_file(self):
        name_info = self.name_entry.get()
        lastname_info = self.lname_entry.get()
        email_info = self.email_entry.get()
        # gender_info = 'MALE'
        tel_info = self.telphone_entry.get()
        birthday_info = str(self.birthday_date_entry.get()) + '/' +  str(self.birthday_month_entry.get()) + '/' + str(self.birthday_year_entry.get())

        email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")

        if (name_info == ''):
            messagebox.showinfo(
                "Info", "Please Enter First Name", parent=self.shop_window)

        elif (lastname_info == ''):
            messagebox.showinfo("Info", "Please Enter Last Name",
                                parent=self.shop_window)

        # elif (self.gender1.get() == 0 and self.gender2.get() == 0):
        #     messagebox.showinfo(
        #         "Error", "Please Select Your Gender", parent=self.register_screen)

        elif (email_info == ''):
            messagebox.showinfo(
                "Info", "Please Enter Your Email", parent=self.shop_window)

        elif (email_regex.match(email_info) == None):
            messagebox.showerror("Error", "Email Invalid", parent=self.shop_window)

        elif (tel_info == ''):
            messagebox.showinfo(
                "Info", "Please Enter Phone Number", parent=self.shop_window)
        
        elif (tel_info[0] != "+" or tel_info[1] != '6' or tel_info[2] != '6' or len(tel_info) > 13):
            messagebox.showerror("Error", "Phone Number Invalid",parent=self.shop_window)
            self.telphone_entry.delete(0,END)

        else:
            if messagebox.askokcancel("Confirm", "Are you sure?"):
                self.name_entry.config(state=DISABLED)
                self.lname_entry.config(state=DISABLED)
                self.gender_entry.config(state=DISABLED)
                self.birthday_date_entry.config(state=DISABLED)
                self.birthday_month_entry.config(state=DISABLED)
                self.birthday_year_entry.config(state=DISABLED)
                self.email_entry.config(state=DISABLED)
                self.telphone_entry.config(state=DISABLED)
                self.edit_info_button.config(state=NORMAL)
                self.done_info_button.config(state=DISABLED)
                self.imageselect_info_button.config(state=DISABLED)
                self.df.loc[self.df['USER'] == self.user[0][1], 'NAME'] = str(name_info).capitalize()
                self.df.loc[self.df['USER'] == self.user[0][1], 'LNAME'] = str(lastname_info).capitalize()
                self.df.loc[self.df['USER'] == self.user[0][1], 'GENDER'] = str(self.gender_entry.get())
                self.df.loc[self.df['USER'] == self.user[0][1], 'BIRTHDAY'] = str(birthday_info)
                self.df.loc[self.df['USER'] == self.user[0][1], 'EMAIL'] = str(email_info)
                self.df.loc[self.df['USER'] == self.user[0][1], 'TEL'] = str(tel_info)
                self.df.loc[self.df['USER'] == self.user[0][1], 'PICTURE'] = str(self.user[0][1])
                self.df.to_csv("login.csv", index=False)
                if self.user_imginput != '':
                    temp_img = cv2.imread(self.user_imginput)
                    cv2.imwrite('UnknownShop\\Picture\\ShopPage\\USER_PIC\\{}.png'.format(self.user[0][1]), temp_img)
                
    # def selectItem(self,a):
    #     curItem = self.tv1.focus()
    #     self.current_book = self.tv1.item(curItem)['values']
    #     #self.current_book[0] = ลำดับที่
    #     #self.current_book[1] = code
    #     #self.current_book[2] = ชื่อหนังสือ
    #     #self.current_book[3] = ผู้แต่ง
    #     #self.current_book[4] = เรื่องย่อ
    #     #self.current_book[5] = ราคา
    #     #self.current_book[6] = จำนวนหน้า
    #     #self.current_book[7] = หมวด
    #     #self.current_book[8] = ภาษา
    #     #self.current_book[9] = จำนวนสินค้า
    #     #self.current_book[10] = rating

    #     #Update Detail Entry
    #     self.name_detail_book_entry.delete(0,END)
    #     self.author_detail_book_entry.delete(0,END)
    #     self.category_detail_book_entry.delete(0,END)
    #     self.language_detail_book_entry.delete(0,END)
    #     self.price_detail_book_entry.delete(0,END)
    #     self.code_detail_book_entry.delete(0,END)
        
    #     self.name_detail_book_entry.insert(0,self.current_book[2])
    #     self.author_detail_book_entry.insert(0,self.current_book[3])
    #     self.category_detail_book_entry.insert(0,self.current_book[7])
    #     self.language_detail_book_entry.insert(0,self.current_book[8])
    #     self.price_detail_book_entry.insert(0,self.current_book[5])
    #     self.code_detail_book_entry.insert(0,self.current_book[1])
        

        
    def selected_categoryPages(self):
        self.inner_selected_categoryPages = Canvas(self.canvas, width=1280, height=550,bd=0, highlightthickness=0)

        self.selected_frame1 = tk.LabelFrame(self.inner_selected_categoryPages, text="selected_categoryPages", bg="white" ,borderwidth=0, highlightthickness=0)
        self.selected_frame1.place(x=100, y=0,height=520, width=1050)

        # Button_frame = ttk.LabelFrame(self.selected_frame1, text="Button State")
        # Button_frame.place(x=300, y=400,height=100, width=500)

        # Nextbutton = tk.Button(Button_frame,text="Buy Books", width=15, command= self.show_categoryPage)
        # Nextbutton.grid(row=2,column=3,padx=180, pady=20)

        filename = "UnknownShop/Picture/ShopPage/BG1.png"
        self.filenameBG = ImageTk.PhotoImage(Image.open(filename))
        background_label = Label(self.inner_selected_categoryPages, image=self.filenameBG)
        background_label.place(x=641, y=207, anchor=CENTER)

        self.lbl_status = tk.Label(self.inner_selected_categoryPages, text="-- Choose type --".upper(), font=('TRACK',20) ,bg="white")
        self.lbl_status.place(relx=0.5, rely=0.07, anchor=CENTER)

        self.ll = CircularLinkedList()
        self.ls = CircularLinkedList()
        self.ls.add('orange')
        self.ls.add('blue')
        self.ls.add('green')
        self.ls.add('black')
        self.ls.add('gray')
        self.ls.add('red')
        self.ls.add('purple')
        self.ll.add('UnknownShop/Picture/ShopPage/orange.jpg')
        self.ll.add('UnknownShop/Picture/ShopPage/blue.png')
        self.ll.add('UnknownShop/Picture/ShopPage/green.jpg')
        self.ll.add('UnknownShop/Picture/ShopPage/black.png')
        self.ll.add('UnknownShop/Picture/ShopPage/gray.jpg')
        self.ll.add('UnknownShop/Picture/ShopPage/red.png')
        self.ll.add('UnknownShop/Picture/ShopPage/purple.png')


        self.login_btn = ImageTk.PhotoImage(Image.open(self.ll.head.prev.data).resize((200, 200)))
        self.lbl_value = tk.Button(master=self.inner_selected_categoryPages, image=self.login_btn, height=200, width=200, borderwidth=0)
        self.lbl_value.bind("<Enter>", lambda event: self.isL())
        self.lbl_value.bind("<Leave>", lambda event: self.rsL())
        self.lbl_value.bind("<Button-1>", lambda event: self.prev_category())
        self.lbl_value.place(relx=0.35, rely=0.5, anchor="center")

        

        self.login_btn3 = ImageTk.PhotoImage(Image.open(self.ll.head.next.data).resize((200, 200)))
        self.lbl_value3 = tk.Button(master=self.inner_selected_categoryPages, image=self.login_btn3, height=200, width=200, borderwidth=0)
        self.lbl_value3.bind("<Enter>", lambda event: self.isR())
        self.lbl_value3.bind("<Leave>", lambda event: self.rsR())
        self.lbl_value3.bind("<Button-1>", lambda event: self.next_category())
        self.lbl_value3.place(relx=0.65, rely=0.5, anchor="center")

        self.login_btn2 = ImageTk.PhotoImage(Image.open(self.ll.head.data).resize((300, 300)))
        self.lbl_value2 = tk.Button(master=self.inner_selected_categoryPages, image=self.login_btn2, height=300, width=300, borderwidth=0)
        self.lbl_value2.bind("<Enter>", lambda event: self.isM())
        self.lbl_value2.bind("<Leave>", lambda event: self.rsM())
        self.lbl_value2.bind("<Button-1>", lambda event: self.ei())
        self.lbl_value2.place(relx=0.5, rely=0.5, anchor="center")

        self.lbl_status = Label(self.inner_selected_categoryPages, text=self.ls.head.data, font=('TRACK',20))
        self.lbl_status.place(relx=0.5, rely=0.819, anchor=CENTER)

        self.sizeL = self.lbl_value['height']
        self.sizeM = self.lbl_value2['height']
        self.sizeR = self.lbl_value3['height']

    def update(self):
        self.login_btn = ImageTk.PhotoImage(Image.open(self.ll.head.prev.data).resize((200, 200)))
        self.lbl_value = tk.Button(master=self.inner_selected_categoryPages, image=self.login_btn, height=200, width=200, borderwidth=0)
        self.lbl_value.bind("<Enter>", lambda event: self.isL())
        self.lbl_value.bind("<Leave>", lambda event: self.rsL())
        self.lbl_value.bind("<Button-1>", lambda event: self.prev_category())
        self.lbl_value.place(relx=0.35, rely=0.5, anchor="center")

        self.login_btn3 = ImageTk.PhotoImage(Image.open(self.ll.head.next.data).resize((200, 200)))
        self.lbl_value3 = tk.Button(master=self.inner_selected_categoryPages, image=self.login_btn3, height=200, width=200, borderwidth=0)
        self.lbl_value3.bind("<Enter>", lambda event: self.isR())
        self.lbl_value3.bind("<Leave>", lambda event: self.rsR())
        self.lbl_value3.bind("<Button-1>", lambda event: self.next_category())
        self.lbl_value3.place(relx=0.65, rely=0.5, anchor="center")

        self.login_btn2 = ImageTk.PhotoImage(Image.open(self.ll.head.data).resize((300, 300)))
        self.lbl_value2 = tk.Button(master=self.inner_selected_categoryPages, image=self.login_btn2, height=300, width=300, borderwidth=0)
        self.lbl_value2.bind("<Enter>", lambda event: self.isM())
        self.lbl_value2.bind("<Leave>", lambda event: self.rsM())
        self.lbl_value2.bind("<Button-1>", lambda event: self.ei())
        self.lbl_value2.place(relx=0.5, rely=0.5, anchor="center")

        self.lbl_status.destroy()
    
        self.lbl_status = Label(self.inner_selected_categoryPages, text=self.ls.head.data, font=('TRACK',20))
        self.lbl_status.place(relx=0.5, rely=0.819, anchor=CENTER)

        self.sizeL = self.lbl_value['height']
        self.sizeM = self.lbl_value2['height']
        self.sizeR = self.lbl_value3['height']

    def next_category(self):
        self.ll.head = self.ll.head.next
        self.ls.head = self.ls.head.next
        self.update()

    def prev_category(self):
        self.ll.head = self.ll.head.prev
        self.ls.head = self.ls.head.prev
        self.update()

    def ei(self):
        # print(f"What da fak r u doin!{self.ls.head.data}!")
        if self.ls.head.data == 'orange':
            self.drop1.current(1)
            self.search()
        elif self.ls.head.data == 'blue':
            self.drop1.current(2)
            self.search()
        elif self.ls.head.data == 'green':
            self.drop1.current(3)
            self.search()
        elif self.ls.head.data == 'black':
            self.drop1.current(4)
            self.search()
        elif self.ls.head.data == 'gray':
            self.drop1.current(5)
            self.search()
        elif self.ls.head.data == 'red':
            self.drop1.current(6)
            self.search()
        elif self.ls.head.data == 'purple':
            self.drop1.current(7)
            self.search()

    def rsL(self):
        while self.sizeL > 200:
            self.lbl_value['height'] = self.sizeL
            self.lbl_value['width'] = self.sizeL
            self.sizeL -= 1

    def rsM(self):
        while self.sizeM > 300:
            self.lbl_value2['height'] = self.sizeM
            self.lbl_value2['width'] = self.sizeM
            self.sizeM -= 1

    def rsR(self):
        while self.sizeR > 200:
            self.lbl_value3['height'] = self.sizeR
            self.lbl_value3['width'] = self.sizeR
            self.sizeR -= 1

    def isL(self):
        while self.sizeL < 205:
            self.lbl_value['height'] = self.sizeL
            self.lbl_value['width'] = self.sizeL
            self.sizeL += 1

    def isM(self):
        while self.sizeM < 310:
            self.lbl_value2['height'] = self.sizeM
            self.lbl_value2['width'] = self.sizeM
            self.sizeM += 1

    def isR(self):
        while self.sizeR < 205:
            self.lbl_value3['height'] = self.sizeR
            self.lbl_value3['width'] = self.sizeR
            self.sizeR += 1

    def categoryPage(self):
        self.inner_category = Canvas(self.canvas,width=1280, height=550,bd=0, highlightthickness=0)
       
        Label(self.inner_category, image=self.bgg).place(x=641, y=207, anchor=CENTER)
        ##Frame for book details
        self.detail_frame = tk.LabelFrame(self.inner_category,borderwidth=0, highlightthickness=0)
        self.detail_frame.place(x=20, y=0,height=540, width=650)
        Label(self.detail_frame, image=self.bgg).place(x=641, y=207, anchor=CENTER)

        self.picbook_frame = tk.LabelFrame(self.detail_frame,borderwidth=0, highlightthickness=0)
        self.picbook_frame.place(x=20, y=20,height=330, width=230)
        Label(self.picbook_frame, image=self.bgg).place(x=641, y=207, anchor=CENTER)

        self.detail_data = tk.LabelFrame(self.detail_frame,borderwidth=0, highlightthickness=0)
        self.detail_data.place(x=310, y=50,height=250, width=300)
        Label(self.detail_data, image=self.bgg).place(x=641, y=207, anchor=CENTER)

        self.example_frame = tk.LabelFrame(self.detail_frame,borderwidth=0, highlightthickness=0)
        self.example_frame.place(x=20, y=350,height=100, width=600)
        Label(self.example_frame, image=self.bgg).place(x=641, y=207, anchor=CENTER)

        self.option_frame = tk.LabelFrame(self.detail_frame,borderwidth=0, highlightthickness=0)
        self.option_frame.place(x=120, y=450,height=50, width=360)
        Label(self.option_frame, image=self.bgg).place(x=641, y=207, anchor=CENTER)
    

        # Frame for book_TreeView
        frame1 = tk.LabelFrame(self.inner_category,borderwidth=0, highlightthickness=0)
        frame1.place(x=680, y=0, height=540, width=590)
        Label(frame1, image=self.bgg).place(x=641, y=207, anchor=CENTER)

       

        #Name Of Book
        # self.name_detail_book_entry.bind("<Key>", lambda e: "break")

        # lbl1 = Label(self.detail_frame, text="No")
        # lbl1.grid(row=0, column=0, padx=10, pady=5)
        # self.lbl1_entry = Entry(self.detail_frame, textvariable=self.No)
        # self.lbl1_entry.grid(row=0, column=1, padx=10, pady=5)


        #Author Of Book
        lbl2 = tk.Label(self.detail_data, text="Code",font = self.myfont, background="#908d8d")
        lbl2.grid(row=0, column=1, padx=10, pady=5)
        self.lbl2_entry = Entry(self.detail_data, textvariable=self.Code,font = self.myfont, width = 15)
        self.lbl2_entry.grid(row=0, column=2, padx=10, pady=10)


        #Category Of Book
        lbl3 = tk.Label(self.detail_data, text="Name",font = self.myfont,background="#908d8d")
        lbl3.grid(row=1, column=1, padx=10, pady=5)
        self.lbl3_entry = Entry(self.detail_data, textvariable=self.Name,font = self.myfont, width = 15)
        self.lbl3_entry.grid(row=1, column=2, padx=10, pady=5)

        #Language Of Book
        lbl4 = tk.Label(self.detail_data, text="Author",font = self.myfont, background="#908d8d")
        lbl4.grid(row=3, column=1, padx=10, pady=5)
        self.lbl4_entry = Entry(self.detail_data, textvariable=self.Author,font = self.myfont, width = 15)
        self.lbl4_entry.grid(row=3, column=2, padx=10, pady=5)

        #Price Of Book
        lbl5 = tk.Label(self.detail_data, text="Category",font = self.myfont, background="#908d8d")
        lbl5.grid(row=4, column=1, padx=10, pady=5)
        self.lbl5_entry = Entry(self.detail_data, textvariable=self.Category,font = self.myfont, width = 15)
        self.lbl5_entry.grid(row=4, column=2, padx=10, pady=5)

        #Code Of Book
        lbl6 = tk.Label(self.detail_data, text="Price",font = self.myfont, background="#908d8d")
        lbl6.grid(row=5, column=1, padx=10, pady=5)
        self.lbl6_entry = Entry(self.detail_data, textvariable=self.Price,font = self.myfont, width = 15)
        self.lbl6_entry.grid(row=5, column=2, padx=10, pady=5)

        # Rating Of Book
        lbl7 = tk.Label(self.detail_data, text="Rating",font = self.myfont, background="#908d8d")
        lbl7.grid(row=6, column=1, padx=10, pady=5)
        self.lbl7_entry = Entry(self.detail_data, textvariable=self.Rating,font = self.myfont, width = 15)
        self.lbl7_entry.grid(row=6, column=2, padx=10, pady=5)

        # Example Of Book
        self.commentbox = tk.Entry(self.example_frame, textvariable=self.Example, state="readonly",font = self.myfont)

        self.commentbox.place(x=10,y=0,width=550,height=70)
       

        ## number of items book
        self.spinboxvar = IntVar(self.option_frame)
        self.spinboxvar.set(1)
        self.items_book_spinbox = Spinbox(self.option_frame, from_=1, to=10,textvariable=self.spinboxvar ,state = 'readonly',width=7, font=Font(family='Helvetica', size=12, weight='bold'))
        Label(self.option_frame, text="").grid(row=7, column=0, padx=10, pady=5)
        self.items_book_spinbox.grid(row=7, column=1, padx=10, pady=5)

        # add_favbook_button = tk.Button(self.option_frame,text=' ♥ ', command=self.add_bookcart, width=15,font = self.myfont)
        # add_favbook_button.grid(row=7, column=0, padx=10, pady=5)

        self.add_bookcart_button = tk.Button(self.option_frame,text=' + ', command=self.add_bookcart,state=DISABLED,width=15)
        self.add_bookcart_button.grid(row=7, column=2, padx=10, pady=5)
        
   

        ##Book Image
        self.book_img_input = 'BookPics\\NOT_FOUND.png'
        self.book_img = ImageTk.PhotoImage(Image.open(self.book_img_input).resize((200, 300)))
        Label(self.picbook_frame, image=self.book_img).grid(row=0, column=0, padx=10, pady=5)
        self.list_img_book = os.listdir('BookPics')


        self.book_treeview = ttk.Treeview(frame1, column=(1,2,3,4,5,6), show="headings", height="23")

        self.book_treeview.place(x= 30, y=30)
        self.book_treeview.column(1, anchor='center', width=40)
        self.book_treeview.column(2, anchor='center', width=80)
        self.book_treeview.column(3, anchor='center', width=140)
        self.book_treeview.column(4, anchor='center', width=100)
        self.book_treeview.column(5, anchor='center', width=100)
        self.book_treeview.column(6, anchor='center', width=50)
        self.book_treeview.heading(1, text="No")
        self.book_treeview.heading(2, text="Code")
        self.book_treeview.heading(3, text="Name")
        self.book_treeview.heading(4, text="Author")
        self.book_treeview.heading(5, text="Category")
        self.book_treeview.heading(6, text="Price")
        

        # Book table
        for i in self.book_data:
            self.book_treeview.insert('', 'end', values = [i][0])
            # print(self.book_treeview.insert('', 'end', values = [i][0]))



        # Click on table book data
        self.book_treeview.bind("<ButtonRelease-1>", self.lookupCustomer)


        yscrollbar = ttk.Scrollbar(frame1, orient="vertical", command=self.book_treeview.yview)
        # xscrollbar = ttk.Scrollbar(frame1, orient="horizontal", command=self.book_treeview.xview)

        # self.book_treeview.config(xscrollcommand=xscrollbar.set)
        self.book_treeview.config(yscrollcommand=yscrollbar.set)

        yscrollbar.pack(side="right", fill="y")
        # xscrollbar.pack(side="bottom", fill="x")

    def lookupCustomer(self, event):
        curItem = self.book_treeview.focus()
        cur = self.book_treeview.item(curItem)['values']
        self.No.set(cur[0])
        self.Code.set(cur[1])
        self.Name.set(cur[2])
        self.Author.set(cur[3])
        self.Category.set(cur[4])
        self.Price.set(cur[5])
        self.Rating.set(cur[9])
        self.Example.set(cur[7])
        if self.confirm_order == False:
            self.add_bookcart_button.config(state=NORMAL)
        if str(self.Code.get()) +'.png' in self.list_img_book:
            self.book_img_input = 'BookPics\\{}.png'.format(self.Code.get())
            self.book_img = ImageTk.PhotoImage(Image.open(self.book_img_input).resize((200, 300)))
            Label(self.picbook_frame, image=self.book_img).grid(row=0, column=0, padx=10, pady=5)
        else:
            self.book_img_input = 'BookPics\\NOT_FOUND.png'
            self.book_img = ImageTk.PhotoImage(Image.open(self.book_img_input).resize((200, 300)))
            Label(self.picbook_frame, image=self.book_img).grid(row=0, column=0, padx=10, pady=5)
    
    def add_bookcart(self):
        self.tempprice = 0
        if self.usercart != []:
            for i in self.usercart:
                if i[0] == self.Code.get():
                    i[2] = str(int(i[2]) + int(self.items_book_spinbox.get()))
                    i[4] = str(float(i[2]) * float(i[3]))
                    # self.tempprice += float(i[4])
                    # self.tempprice += self.tempprice
                    # print('UserCart :',self.usercart)
                    # print("\n\n\n",self.tempprice)
                    return
                    
        self.usercart.append([self.Code.get(),self.Name.get(),str(self.items_book_spinbox.get()),self.Price.get(),self.Price.get()])
        # print('UserCart :',self.usercart)
        self.spinboxvar.set(1)

    def delete_bookcart(self):
        # print('current :',self.current_bookcart)
        # print('usercart :',self.usercart)
        if self.current_bookcart in self.usercart:
            self.usercart.remove(self.current_bookcart)
        else:
            print('cart is empty')
        self.Del_botton.config(state=DISABLED)
        self.cart_treeview.delete(*self.cart_treeview.get_children())
        index = 1
        for i in self.usercart:
            self.cart_treeview.insert('', 'end', values=[index,i[0],i[1],i[2],i[3],i[4]])
            index += 1
        if self.usercart == []:
            member = 0.00
            promotion = 0.00
            shipping = 0.00
        else:
            member = -15.25
            promotion = -12.50
            shipping = 40.00
        self.total_amount.set(0.0)
        def listsum(numList):
            if len(numList) == 1:
                    return float(numList[0][4])
            else:
                    return float(numList[0][4]) + listsum(numList[1:])
        if self.usercart != []:
            temp = round(listsum(self.usercart),2)
            self.total_amount.set(temp)
        temp=member + promotion + shipping +float(self.total_amount.get())
        self.total2.set(temp)
 
   
    def lookupCart(self, event):
        curItem = self.cart_treeview.focus()
        cur = self.cart_treeview.item(curItem)['values']
        self.current_bookcart = []
        if cur != '':
            if self.confirm_order == False:
                self.Del_botton.config(state=NORMAL)
            for i in cur[1:]:
                self.current_bookcart.append(str(i))

        
    def shift(self):
        x1,y1,x2,y2 = self.inner_payment_slidetext.bbox("marquee")
        if(x2<0 or y1<0): #reset the coordinates
            x1 = self.inner_payment_slidetext.winfo_width()
            y1 = self.inner_payment_slidetext.winfo_height()//2
            self.inner_payment_slidetext.coords("marquee",x1,y1)
        else:
            self.inner_payment_slidetext.move("marquee", -2, 0)
        self.inner_payment_slidetext.after(1000//self.fps,self.shift)      

    
       
    def paymentPage(self):
        self.inner_payment = Canvas(self.canvas, width=1280, height=550)  

        filename = "UnknownShop/Picture/ShopPage/BG1.png"
        self.filenameBG = ImageTk.PhotoImage(Image.open(filename))
        background_label = Label(self.inner_payment, image=self.filenameBG)
        background_label.place(x=641, y=207, anchor=CENTER)


        paymentPageFrame1 = tk.LabelFrame(self.inner_payment)
        paymentPageFrame1.place(x=50, y=0, height=50, width=1178)
        # Label(paymentPageFrame1, image=self.bgg).place(x=641, y=207, anchor=CENTER)
        
         ##Text Slide
        text_var="______|   Welcome to the land of bookS   |______" 
        self.inner_payment_slidetext = Canvas(paymentPageFrame1, width=1000, height=100) 
        self.inner_payment_slidetext.create_text(0,-2000,text=text_var,font=('Times New Roman',20,'bold'),fill='black',tags=("marquee",),anchor='w')
        x1,y1,x2,y2 = self.inner_payment_slidetext.bbox("marquee")

    
        width = x2-x1
        # height = y2-y1
        self.inner_payment_slidetext['width'] = width+500
        self.inner_payment_slidetext['height'] = 60
        self.fps=40    #Change the fps to make the animation faster/slower
        self.inner_payment_slidetext.pack()
        ############# Main program ###############
       
        ##cart table
        self.paymentPageFrame2 = tk.LabelFrame(self.inner_payment)
        self.paymentPageFrame2.place(x=50, y=55, height=500, width=1180)
        Label(self.paymentPageFrame2, image=self.bgg).place(x=641, y=207, anchor=CENTER)

        paymentPageFrame3 = tk.LabelFrame(self.paymentPageFrame2)
        paymentPageFrame3.place(x=0, y=400, height=80, width=800)
        Label(paymentPageFrame3, image=self.bgg).place(x=641, y=207, anchor=CENTER)

        ############# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        if self.usercart == []:
            member = 0.00
            promotion = 0.00
            shipping = 0.00
        else:
            member = -15.25
            promotion = -12.50
            shipping = 40.00
        self.paymentPageFrame4 = tk.LabelFrame(self.paymentPageFrame2, text="receipt".upper(), fg="blue",bg="white",font=("times new roman",14,"bold"))
        self.paymentPageFrame4.place(x=800, y=0, height=480, width=350)

        lebel1 = tk.Label(self.paymentPageFrame4, text=" Sales : ", width = 15)
        lebel1.place(x=50, y=10)
        self.total_amount.set(0.0)
        def listsum(numList):
            if len(numList) == 1:
                    return float(numList[0][4])
            else:
                    return float(numList[0][4]) + listsum(numList[1:])
        if self.usercart != []:
            temp = round(listsum(self.usercart),2)
            self.total_amount.set(temp)
            
        
        
        label1_1 = tk.Label(self.paymentPageFrame4, textvariable=self.total_amount, width = 15)
        label1_1.place(x=200, y=10)
        
        lebel2 = tk.Label(self.paymentPageFrame4, text=" Member : ", width = 15)
        lebel2.place(x=50, y=50)

        label2_1 = tk.Label(self.paymentPageFrame4, text=" {} ฿".format(member), width = 15)
        label2_1.place(x=200, y=50)

        lebel3 = tk.Label(self.paymentPageFrame4, text=" Promotion : ", width = 15)
        lebel3.place(x=50, y=90)

        label3_1 = tk.Label(self.paymentPageFrame4, text=" {} ฿".format(promotion), width = 15)
        label3_1.place(x=200, y=90)

        lebel4 = tk.Label(self.paymentPageFrame4, text=" Shipping : ", width = 15)
        lebel4.place(x=50, y=130)

        label4_1 = tk.Label(self.paymentPageFrame4, text=" {} ฿".format(shipping), width = 15)
        label4_1.place(x=200, y=130)

        
        lebel5 = tk.Label(self.paymentPageFrame4, text=" Total(s) : ", width = 15)
        lebel5.place(x=50, y=170)

        self.label5_1 = tk.Label(self.paymentPageFrame4, text=" 0.00 ฿", width = 15)
        self.label5_1.place(x=200, y=170)

        lebel5 = tk.Label(self.paymentPageFrame4, text="+ ============================================= +", font=("times new roman",10,"bold"))
        lebel5.place(x=1, y=210)

        temp=member + promotion + shipping +float(self.total_amount.get())
        self.total2.set(temp)


        lebel5 = tk.Label(self.paymentPageFrame4, text=" Total(s) : ", width = 10, font=("times new roman",15,"bold"))
        lebel5.place(x=20, y=250)

        self.label5_1 = tk.Label(self.paymentPageFrame4, textvariable=self.total2, width = 10, font=("times new roman",15,"bold"))
        self.label5_1.place(x=200, y=250)

        self.Payment_bottom = tk.Button(self.paymentPageFrame4,text="< Payment >", command = self.dummy_payment , width = 15, state=DISABLED)
        self.Payment_bottom.place(x=170, y=350,anchor="center")

        self.Cancel_bottom = tk.Button(self.paymentPageFrame4,text="< Cancel Order >", command = self.dummy_cancle , width = 15, state=DISABLED)
        self.Cancel_bottom.place(x=170, y=400,anchor="center")

        ############# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


        self.cart_treeview = ttk.Treeview(self.paymentPageFrame2, column=(1,2,3,4,5,6), show="headings", height="18")
        # yscrollbar = ttk.Scrollbar(self.paymentPageFrame2, orient="vertical", command=self.cart_treeview.yview)
        # xscrollbar = ttk.Scrollbar(paymentPageFrame1, orient="horizontal", command=self.cart_treeview.xview)

        # # self.cart_treeview.place(x= 10, y=0)
        # self.cart_treeview.config(xscrollcommand=xscrollbar.set)
        # self.cart_treeview.config(yscrollcommand=yscrollbar.set)

        # yscrollbar.pack(side="right", fill="y")
        # xscrollbar.pack(side="bottom", fill="x")
        self.cart_treeview.pack()
        self.cart_treeview.place(x=400,y=200,anchor=CENTER)
        self.cart_treeview.column(1, anchor='center', width=50)
        self.cart_treeview.column(2, anchor='center', width=100)
        self.cart_treeview.column(3, anchor='w', width=300)
        self.cart_treeview.column(4, anchor='center', width=100)
        self.cart_treeview.column(5, anchor='center', width=100)
        self.cart_treeview.column(6, anchor='center', width=100)
        self.cart_treeview.heading(1, text="no.")
        self.cart_treeview.heading(2, text="Code")
        self.cart_treeview.heading(3, text="Name")
        self.cart_treeview.heading(4, text="Item (s)")
        self.cart_treeview.heading(5, text="Price")
        self.cart_treeview.heading(6, text="Total amount")
        self.cart_treeview.bind("<ButtonRelease-1>", self.lookupCart)
        
        index = 1
        for i in self.usercart:
            self.cart_treeview.insert('', 'end', values=[index,i[0],i[1],i[2],i[3],i[4]])
            index += 1


        self.Edit_bottom = tk.Button(paymentPageFrame3,text="< Edit >", command = self.pp, width = 15)    
        # Back_bottom.pack(side = BOTTOM,anchor='')
        self.Edit_bottom.place(x=100, y=30,anchor="center")

        self.Del_botton = tk.Button(paymentPageFrame3,text="< Del >", command = self.delete_bookcart, width = 15)
        # Del_bottom.pack(side = BOTTOM)    
        self.Del_botton.place(x=300, y=30,anchor="center")

        self.Confirm_bottom = tk.Button(paymentPageFrame3,text="< Confirm Order >", command = self.confirmorder , width = 15)
        self.Confirm_bottom.place(x=500, y=30,anchor="center")
        # self.Next_botton.pack(side = BOTTOM) 

        self.Next_botton = tk.Button(paymentPageFrame3,text="< Next >", command = self.topayment,state=DISABLED , width = 15)
        self.Next_botton.place(x=700, y=30,anchor="center")
        # Seemore_bottom.pack(side = BOTTOM) 

        if self.usercart == [] or self.confirm_order == True:
            self.Edit_bottom.config(state=DISABLED)
            self.Del_botton.config(state=DISABLED)
            self.Confirm_bottom.config(state=DISABLED)
        else:
            self.Edit_bottom.config(state=NORMAL)
            self.Del_botton.config(state=NORMAL)
            self.Confirm_bottom.config(state=NORMAL)
        if self.confirm_order == True and self.confirm_next == False:
            # print('self.confirm_next :',self.confirm_next)
            self.self.Next_botton.config(state=NORMAL)
        elif self.confirm_next == True:
            self.Payment_bottom.config(state=NORMAL)
        if self.payment_check == True:
            self.Cancel_bottom.config(state=NORMAL)
            self.Payment_bottom.config(state=DISABLED)

    def confirmorder(self):
        self.Edit_bottom.config(state=DISABLED)
        self.Del_botton.config(state=DISABLED)
        self.Confirm_bottom.config(state=DISABLED)
        messagebox.showinfo(message='Your order have been confirmed',title='Confirm your Order')
        self.Cancel_bottom.config(state=DISABLED)
        self.Next_botton.config(state=NORMAL)
        self.confirm_order = True
    def pp(self):
        print("Test"*10)
    def topayment(self):
        self.confirm_next = True
        self.Next_botton.config(state=DISABLED)
        self.Payment_bottom.config(state=NORMAL)

    def dummy_payment(self):
        print("PAYMENT")
        #------------------------------    init     ------------------------------------------------------------#
        self.payment_screen = Toplevel(self.inner_payment)
        self.payment_screen.title("Payment")
        self.payment_screen.focus_set()
        self.payment_screen.grab_set()
        self.payment_screen.resizable(0, 0)
        x = (960) - (500/2)
        y = (540) - (550/2)
        self.payment_screen.geometry("500x500+%d+%d" % (x, y))
        #------------------------------    Frame     ------------------------------------------------------------#
        self.payment_frame = LabelFrame(
            self.payment_screen, text='Detail')
        Label(self.payment_frame, text="Address").grid(
            row=0, column=0, padx=10, pady=5, sticky="E")
        self.payment_address_entry = Text(self.payment_frame, width=40, height=5)
        self.payment_address_entry.insert(1.0, '')
        self.payment_address_entry.grid(row=0, column=1, padx=10, pady=5,rowspan=5,columnspan=4)
        Label(self.payment_frame,text='').grid(row=6, column=0, padx=10, pady=5)
        Label(self.payment_frame,text='Payment Method').grid(row=7, column=0, padx=10, pady=5,sticky='w')
        self.payment_method_entry = ttk.Combobox(self.payment_frame, width=20, value=["Cash On Delivery","Promptpay"])
        self.payment_method_entry.current((0))
        self.payment_method_entry.bind("<<ComboboxSelected>>", self.pay_method_state)
        self.payment_method_entry.grid(row=7, column=1, padx=10, pady=5,columnspan=2)
        self.pay_method_frame = LabelFrame(self.payment_frame, text='Upload File')
        self.pay_method_img_frame = LabelFrame(self.payment_frame, text='Preview')
        self.pay_imginput=''
        
        #------------------------------    Option Detail Plane     ------------------------------------------------------------#
        self.payment_option_frame = LabelFrame(self.payment_screen, text='')
        self.cancel_payment_button = Button(
            self.payment_option_frame, text='Cancel',command =self.close_payment)
        self.cancel_payment_button.grid(row=0, column=0, padx=12, pady=0)
        self.order_payment_button = Button(
            self.payment_option_frame, text='Place Order',command=self.place_order)
        self.order_payment_button.grid(row=0, column=1, padx=12, pady=0)


        self.payment_option_frame.place(x=290, y=440, height=50, width=200)
        self.payment_frame.place(x=10, y=10, height=420, width=480)
    def close_payment(self):
        self.payment_screen.destroy()
    def place_order(self):
        if self.payment_address_entry.get('1.0','end-1c') != '':
            if(messagebox.askokcancel("Confirmation", "Are you sure?", parent=self.payment_screen)) == True:
                self.payment_check = True
                self.Cancel_bottom.config(state=NORMAL)
                self.Payment_bottom.config(state=DISABLED)
                self.nowtime = datetime.datetime.now()
                loadorder = pandas.read_csv('UnknownShop\\database\\order.csv')
                order_temp = loadorder.values.tolist()
                now_orderid = order_temp[len(order_temp)-1][1]
                self.order_id = int(now_orderid) + 1
                Quantity = 0
                for i in self.usercart:
                    Quantity += int(i[2])
                with open('UnknownShop\\database\\order.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([self.nowtime.strftime("%Y-%m-%d %H:%M:%S"),self.order_id,self.user[0][3],self.payment_address_entry.get('1.0','end-1c'),Quantity,self.total_amount.get(),'Payment confirmed - {}'.format(self.payment_method_entry.get()),'-','-'])
                with open('UnknownShop\\database\\order_detail.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    for i in self.usercart:
                        writer.writerow([self.order_id,i[0],i[1],i[2],i[4]])
                if self.pay_imginput != '':
                    temp_img = cv2.imread(self.pay_imginput)
                    cv2.imwrite('UnknownShop\\database\\transfer_slip\\{}.png'.format(self.order_id), temp_img)
                messagebox.showinfo("Alert", "Order completed!!")
                self.close_payment()
        else:
            messagebox.showerror("Error", "Please fill out all fields required", parent=self.payment_screen)
    def pay_method_state(self,e):
        if self.payment_method_entry.get() == 'Promptpay':
            self.order_payment_button.config(state=DISABLED)
            self.pay_method_frame = LabelFrame(self.payment_frame, text='Upload File')
            Label(self.pay_method_frame,text='Promptpay').grid(row=0, column=0, padx=10, pady=5,sticky='w')
            Button(self.pay_method_frame,text='Upload',command=self.pay_openimage).grid(row=0, column=1, padx=10, pady=5,sticky='w')
            temp_path = "UnknownShop\Picture\Draf BG.png" 
            self.pay_upload_img = ImageTk.PhotoImage(Image.open(temp_path).resize((150, 200)))
            self.pay_upload_frame = Label(self.pay_method_img_frame, image=self.pay_upload_img)
            self.pay_upload_frame.pack(anchor=CENTER)
            self.pay_method_img_frame.place(x=320,y=200, height=200, width=150)
            self.pay_method_frame.place(x=10,y=200, height=100, width=300)
        else:
            self.pay_method_frame.destroy()
            self.pay_upload_frame.destroy()
            self.order_payment_button.config(state=NORMAL)
    
    def pay_upload_pic(self):
        pass
    def pay_openfunc(self):
        temp = filedialog.askopenfilename(initialdir='UnknownShop\\Picture\\ShopPage\\USER_PIC',title='open')
        return temp
    def pay_openimage(self):
        self.pay_imginput = self.pay_openfunc()
        if self.pay_imginput != '':
            self.order_payment_button.config(state=NORMAL)
            self.pay_upload_img = ImageTk.PhotoImage(Image.open(self.pay_imginput).resize((150, 200)))
            self.pay_upload_frame.destroy()
            self.pay_upload_frame = Label(self.pay_method_img_frame, image=self.pay_upload_img)
            self.pay_upload_frame.pack(anchor=CENTER)
            self.pay_method_img_frame.place(x=320,y=200, height=200, width=150)

    def dummy_cancle(self):
        MB1 = messagebox.askyesno(message='Are your sure to cancel this order ?',icon='question',title='Cancel Order')
        if MB1 == True:
            # print("CANCEL")
            self.Cancel_bottom.config(state=DISABLED)
            self.Payment_bottom.config(state=DISABLED)
            self.Next_botton.config(state=DISABLED)
            self.confirm_order = False
            self.confirm_next = False
            self.payment_check = False
            self.usercart = []

        else:
            print("...............")
    
    def deliveryPage(self):
        self.inner_delivery = Canvas(self.canvas, width=1280, height=550)   

        filename = "UnknownShop/Picture/ShopPage/BG1.png"
        self.filenameBG = ImageTk.PhotoImage(Image.open(filename))
        background_label = Label(self.inner_delivery, image=self.filenameBG)
        background_label.place(x=641, y=207, anchor=CENTER)

        deliveryPageFrame1 = ttk.LabelFrame(self.inner_delivery, text="Status")
        deliveryPageFrame1.place(x=30, y=20, height=500, width=500)
           
        deliveryPageFrame1_1 = ttk.LabelFrame(deliveryPageFrame1, text="Button Status")
        deliveryPageFrame1_1.place(x=8, y=360, height=100, width=480)
        

        self.deliveryPageFrame2 = ttk.LabelFrame(self.inner_delivery, text="Review Book")
        self.deliveryPageFrame2.place(x=550, y=20, height=500, width=700)

        self.delivery_img_frame = ttk.LabelFrame(self.deliveryPageFrame2, text="Picture")
        self.delivery_img_frame.place(x=50, y=10, height=250, width=200)

        self.deliveryPageFrame2_2 = ttk.LabelFrame(self.deliveryPageFrame2, text="Databook")
        self.deliveryPageFrame2_2.place(x=400, y=10, height=250, width=250)

        self.deliveryPageFrame2_3 = ttk.LabelFrame(self.deliveryPageFrame2, text="Review Button")
        self.deliveryPageFrame2_3.place(x=200, y=380, height=90, width=420)



        #Author Of Book
        lbl2 = Label(self.deliveryPageFrame2_2, text="Code")
        lbl2.grid(row=0, column=1, padx=10, pady=5)
        self.review_code_entry = Entry(self.deliveryPageFrame2_2, textvariable=self.review_Code,state= "readonly")
        self.review_code_entry.grid(row=0, column=2, padx=10, pady=10)


        #Category Of Book
        lbl3 = Label(self.deliveryPageFrame2_2, text="Name")
        lbl3.grid(row=1, column=1, padx=10, pady=5)
        self.review_name_entry = Entry(self.deliveryPageFrame2_2, textvariable=self.review_Name,state= "readonly")
        self.review_name_entry.grid(row=1, column=2, padx=10, pady=5)

        #Language Of Book
        lbl4 = Label(self.deliveryPageFrame2_2, text="Author")
        lbl4.grid(row=3, column=1, padx=10, pady=5)
        self.review_author_entry = Entry(self.deliveryPageFrame2_2, textvariable=self.review_Author,state= "readonly")
        self.review_author_entry.grid(row=3, column=2, padx=10, pady=5)

        #Price Of Book
        lbl5 = Label(self.deliveryPageFrame2_2, text="Category")
        lbl5.grid(row=4, column=1, padx=10, pady=5)
        self.review_category_entry = Entry(self.deliveryPageFrame2_2, textvariable=self.review_Category,state= "readonly")
        self.review_category_entry.grid(row=4, column=2, padx=10, pady=5)

        #Code Of Book
        lbl6 = Label(self.deliveryPageFrame2_2, text="Price")
        lbl6.grid(row=5, column=1, padx=10, pady=5)
        self.review_price_entry = Entry(self.deliveryPageFrame2_2, textvariable=self.review_Price,state= "readonly")
        self.review_price_entry.grid(row=5, column=2, padx=10, pady=5)

        # Rating Of Book
        lbl7 = Label(self.deliveryPageFrame2_2, text="Rating")
        lbl7.grid(row=6, column=1, padx=10, pady=5)
        listofRating = ["1","2","3","4","5"]
        self.Rating_Combobox = ttk.Combobox(self.deliveryPageFrame2_2,values=listofRating,width=18,state=DISABLED)
        self.Rating_Combobox.current(4)
        self.Rating_Combobox.grid(row=6, column=2, padx=10, pady=5)




        self.review_bottom = ttk.Button(self.deliveryPageFrame2_3,text="< Review >", command = self.review_bottomOn, state=DISABLED)    
        # self.review_bottom.place(x=500, y=400,anchor="center")
        self.review_bottom.pack(side = BOTTOM, padx=10, pady=5) 

        Back_bottom = ttk.Button(deliveryPageFrame1_1,text="< Back >", command = self.backk, width=10)    
        Back_bottom.place(x=180, y=40,anchor="center")
        # Back_bottom.pack(side = LEFT) 

        self.Next_bottonn = ttk.Button(deliveryPageFrame1_1,text="< Next >", command = self.checkDeliverySuccess, width=10)    
        self.Next_bottonn.place(x=300, y=40,anchor="center")
        # self.Next_botton.pack(side = RIGHT)



        commenttext = Label(self.deliveryPageFrame2,text="Comment : ", font=('TRACK', 12))
        commenttext.place(x=50,y=300)
        self.commentbox = tk.Text(self.deliveryPageFrame2,width=60,height=5, font=('TRACK', 8),state=DISABLED)
        self.commentbox.place(x=200,y=300)
       

        self.Comment_boutton1 = ttk.Button(self.deliveryPageFrame2_3,text="< Send >",command = self.printcomment, state=DISABLED)
        # self.Comment_boutton1.place(x=100,y=25)
        self.Comment_boutton1.pack(side = LEFT, padx=10, pady=5) 
        
        self.Comment_boutton2 = ttk.Button(self.deliveryPageFrame2_3,text="< Clear >",command = self.clearcomment, state=DISABLED)
        # self.Comment_boutton2.place(x=220,y=25)
        self.Comment_boutton2.pack(side = RIGHT, padx=10, pady=5)

        loadorder = pandas.read_csv('UnknownShop\\database\\order.csv')
        order_status = loadorder.values.tolist()
        self.Satatus_message = []
        self.loadorder_deatil = pandas.read_csv('UnknownShop\\database\\order_detail.csv')
        order_detail = self.loadorder_deatil.values.tolist()
        self.order_id_review = 0
        
        for i in reversed(order_status):
            if self.user[0][3] == i[2]: 
                self.order_id_review = i[1]
                if i[6] == 'Payment confirmed - Cash On Delivery' or i[6] == 'Payment confirmed - Promptpay':
                    self.Satatus_message.append(i[0] + ' : Payment confirmed')
                    self.Next_bottonn.config(state =  NORMAL)
                    break
                elif i[6] == 'Waiting for shipment':
                    self.Satatus_message.append(i[0] + ' : Payment confirmed')
                    self.Satatus_message.append(i[0] + ' : Waiting for shipment')
                    self.Next_bottonn.config(state =  NORMAL)
                    break
                elif i[6] == 'Shipped':
                    self.Satatus_message.append(i[0] + ' : Payment confirmed')
                    self.Satatus_message.append(i[0] + ' :  for shipment')
                    self.Satatus_message.append(i[7] + ' : Shipped')
                    self.Next_bottonn.config(state =  NORMAL)
                    break
                elif i[6] == 'Delivered':
                    self.Satatus_message.append(i[0] + ' : Payment confirmed')
                    self.Satatus_message.append(i[0] + ' : Waiting for shipment')
                    self.Satatus_message.append(i[7] + ' : Shipped')
                    self.Satatus_message.append(i[8] + ' : Delivered')
                    self.Next_bottonn.config(state = NORMAL)
                    break
                else:
                    self.Satatus_message.append('Cancelled order')
                    self.Next_bottonn.config(state = DISABLED)
                    break
        #vvvvvvvvvvvvvvvvvvvvvvv Data Structure [ Stack ] vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
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
        self.order_to_review = Stack()
        for i in reversed(order_detail):
            if str(i[0]) == str(self.order_id_review):
                self.order_to_review.push(i[1])
            if i[5] != '' or i[6] != '':
                self.Next_bottonn.config(state = NORMAL)
        #^^^^^^^^^^^^^^^^^^^^^^^^^^ Data Structure [ Stack ] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        
        y = 50
        if len(self.Satatus_message) != 0:
            for i in range(len(self.Satatus_message)):
                if self.Satatus_message[i] == 'Cancelled order':
                    tk.Button(deliveryPageFrame1, text=self.Satatus_message[4], font="BahnschriftLight 15", 
                        bg="#F2FBF9", fg="#ed67b4", activebackground="#F2FBF9", activeforeground="#8e3d6c", 
                        bd=0, width=20).place(x=125, y=240)
                else:
                    tk.Button(deliveryPageFrame1, text=self.Satatus_message[i], font="BahnschriftLight 15", 
                            bg="#F2FBF9", fg="#12CCAB", activebackground="#F2FBF9", activeforeground="#98FF98", 
                            bd=0, width=35,anchor='w').place(x=0, y=y)
                y += 40

    def ContactUSPage(self): # ข้อมูลหน้า info       #1
        self.inner_ContactUS = Canvas(self.canvas, width=1280, height=550)
        
        filename = "UnknownShop/Picture/ShopPage/BG1.png"
        self.filenameBG = ImageTk.PhotoImage(Image.open(filename))
        background_label = Label(self.inner_ContactUS, image=self.filenameBG)
        background_label.place(x=641, y=207, anchor=CENTER)

        ContactUSPageFrame1 = tk.LabelFrame(self.inner_ContactUS , text="Contact Us")
        ContactUSPageFrame1.place(x=400, y=0, height=550, width=500)

        ContactUSPageFrame1_1 = tk.LabelFrame(self.inner_ContactUS , text="Feedback")
        # ContactUSPageFrame1_1.place(x=50, y=0, height=550, width=600)

        self.ContactUSPageFrame2 = tk.LabelFrame(ContactUSPageFrame1 , text="Chat")
        self.ContactUSPageFrame2.place(x=10, y=0, height=400, width=480)

        self.ContactUSPageFrame3 = tk.LabelFrame(ContactUSPageFrame1 , text="Button option")
        self.ContactUSPageFrame3.place(x=10, y=405, height=120, width=480)

        ###############  ContactUSPageFrame1 : "Contact Us"
        ##############   ContactUSPageFrame1_1 : "Feedback" 
        FeedbackFrame1 = tk.LabelFrame( ContactUSPageFrame1_1 , text="BOX TEXT")
        FeedbackFrame1.place(x=100, y=350, height=150, width=400)

        FeedbackFrame2 = tk.LabelFrame( ContactUSPageFrame1_1 , text="Assessment")
        FeedbackFrame2.place(x=50, y=0, height=350, width=500)

        ##############   ContactUSPageFrame2 : "Chat"
        def USER_write_File (text_File):
            UpdateReadfile()
            file = open("users.txt", "a")
            user_Input = text_File.get()
            file.write("User XXX : "+user_Input+ '\n')
            the_input.delete(0, END)
            file.close()

        def ADMIN_write_File (text_File):
            UpdateReadfile()
            file = open("users.txt", "a")
            user_Input = text_File.get()
            file.write("ADMIN XXX : "+user_Input+ '\n')  
            the_input1.delete(0, END)
            file.close()
            

        def UpdateReadfile():
            text.delete('1.0', END)

            text.insert('end', open(filename,'r').read())
            text.see("end")
            text.after(100,UpdateReadfile)
        filename = "users.txt" 

        text = Pmw.ScrolledText( self.ContactUSPageFrame2,
            borderframe=5, 
            vscrollmode='dynamic', 
            hscrollmode='dynamic',
            labelpos='n', 
            label_text='file %s' % filename,
            text_width=80, 
            text_height=20,
            text_wrap='none',
            )

        text.pack()
        text.insert('end', open(filename,'r').read())




        the_input = tkinter.Entry(self.ContactUSPageFrame3)
        the_input.place(x=100, y=30)

        the_input1 = tkinter.Entry(self.ContactUSPageFrame3)
        the_input1.place(x=250, y=30)

        label1 = tkinter.Label(self.ContactUSPageFrame3, text="")
        label1.place(x=0, y=50)

        button1_Write = tkinter.Button(self.ContactUSPageFrame3, text = " U Send to file:", width = 15 ,command = lambda: USER_write_File(the_input)).place(x=105, y=60)
        button2_Write = tkinter.Button(self.ContactUSPageFrame3, text = "A Send to file:", width = 15, command = lambda: ADMIN_write_File(the_input1)).place(x=255, y=60)

        ##############   ContactUSPageFrame3 : "Button option"

    def printcomment(self):
        # self.commenttext2.config(text=self.commentbox.get(1.0,END))
        print(f"Rating is : {self.Rating_Combobox.get()}")
        print(self.commentbox.get(1.0,END),end ="")
    def clearcomment(self):
        self.commentbox.delete(1.0,END)
        print("<<< delete >>> ")

    def review_bottomOn(self):
        self.commentbox.config(state=NORMAL)
        self.review_bottom.config(state=NORMAL)
        self.Comment_boutton1.config(state=NORMAL)
        self.Comment_boutton2.config(state=NORMAL)
        self.Rating_Combobox.config(state=NORMAL)
        #vvvvvvvvvvvvvvvvvvvvvvv Data Structure [ Stack ] vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        if not self.order_to_review.isEmpty():
            self.temp_review = self.order_to_review.pop()
        #^^^^^^^^^^^^^^^^^^^^^^^^^^ Data Structure [ Stack ] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            for i in self.book_data:
                if i[1] == self.temp_review:
                    self.review_Code.set(i[1])
                    self.review_Name.set(i[2])
                    self.review_Author.set(i[3])
                    self.review_Category.set(i[4])
                    self.review_Price.set(i[5])
                    self.delivery_img_frame = ttk.LabelFrame(self.deliveryPageFrame2, text="Picture")
                    self.delivery_img_frame.place(x=50, y=10, height=250, width=200)
                    if str(self.review_Code.get()) +'.png' in self.list_img_book:
                        self.img_review_input = 'BookPics\\{}.png'.format(self.review_Code.get())
                        self.img_review_label = Label(self.delivery_img_frame)
                        self.img_review = ImageTk.PhotoImage(Image.open(self.img_review_input).resize((180, 220)))
                        self.img_review_label.destroy()
                        self.img_review_label = Label(self.delivery_img_frame, image=self.img_review)
                        self.img_review_label.pack(anchor=CENTER)
                    self.loadorder_deatil.loc[(self.loadorder_deatil['Order_ID'] == str(self.order_id_review)) & (self.loadorder_deatil['Bookcode'] == self.review_Code.get()), 'rating'] = self.Rating_Combobox.get()
                    self.loadorder_deatil.loc[(self.loadorder_deatil['Order_ID'] == str(self.order_id_review)) & (self.loadorder_deatil['Bookcode'] == self.review_Code.get()), 'review'] = self.commentbox.get('1.0','end-1c')
                    self.loadorder_deatil.to_csv("UnknownShop\\database\\order_detail.csv", index=False)
                    self.Rating_Combobox.current(4)
                    self.commentbox.delete('1.0',END)

        else:
            self.review_Code.set('')
            self.review_Name.set('')
            self.review_Author.set('')
            self.review_Category.set('')
            self.review_Price.set('')
            self.img_review_label.destroy()
            self.review_bottom.config(state=DISABLED)
            self.Next_bottonn.config(state = DISABLED)
            self.Rating_Combobox.config(state=DISABLED)

    def backk(self):
        self.commentbox.config(state=DISABLED)
        self.review_bottom.config(state=DISABLED)
        self.Comment_boutton1.config(state=DISABLED)
        self.Comment_boutton2.config(state=DISABLED)
        self.Rating_Combobox.config(state=DISABLED)

    def show_HomePage(self): 
        self.delete_canvas()
        self.HomePage()
        self.canvas.create_window(0, 150, anchor=NW, window=self.inner_HomePage) 
        self.set_banner()
        self.count = 0
        
        
        

    def checkDeliverySuccess(self):
        self.review_bottomOn()

    def show_infomationPage(self): # ุปุ่ม 1
        self.delete_canvas()
        self.infomationPage()
        self.canvas.create_window(0, 150, anchor=NW, window=self.inner_infomation)

    def show_selected_categoryPages(self): 
        self.delete_canvas()
        self.selected_categoryPages()
        self.canvas.create_window(0, 150, anchor=NW, window=self.inner_selected_categoryPages)
     
    def show_categoryPage(self):
        self.delete_canvas()
        self.categoryPage()
        self.canvas.create_window(0, 150, anchor=NW, window=self.inner_category)
        if self.confirm_order == True:
            self.add_bookcart_button.config(state=DISABLED)


    def show_paymentPage(self):
        self.delete_canvas()
        self.paymentPage()
        # self.shift()
        self.canvas.create_window(0,150, anchor=NW, window=self.inner_payment)


    def show_deliveryPage(self):
        self.delete_canvas()
        self.deliveryPage()
        self.canvas.create_window(0,150, anchor=NW, window=self.inner_delivery)

    def show_ContactUSPage(self):
        self.delete_canvas()
        self.ContactUSPage()
        self.canvas.create_window(0,150, anchor=NW, window=self.inner_ContactUS)
        
    
                
            

            
    # ลบหน้า info
    def delete_canvas(self): # ปุ่ม 2  

        self.canvas.delete(ALL)
        
        

        self.create_background()
        # self.create_logo()
        # self.search_bar()
        self.button_state()
       
        self.menuTab_logo()

        
     




    ## 1. def ข้อมูลหน้านั้น -> ใส่ใน init
    ## 2. def แสดงข้อมูลหน้านัั้น -> ใส่ delete ก่อน
    ## 3. ใน def delete เอาหน้านั้นไปใส่



def showShopPage():
    run = Shop_main_screen()

if __name__ == '__main__':
    showShopPage()
