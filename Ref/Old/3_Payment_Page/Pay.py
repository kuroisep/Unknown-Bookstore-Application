import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import font as tkFont
import pandas
from PIL import ImageTk, Image
import re
import os
import csv

class Payment_screen:
    def __init__(self):
        self.payment_window = tk.Tk()
        self.payment_window.title("Unknown Book Store // Payment")
        x = (700) - (750/2)
        y = (420) - (500/2)
        self.payment_window.geometry("1280x720+%d+%d" % (x, y))
        bg_path = "3_Payment_Page\PICTURE\Infobook_BG.png"
        bg = ImageTk.PhotoImage(Image.open(bg_path).resize((1280, 720)))
        canvas = Canvas(self.payment_window, width=1280, height=720)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor="nw")

        self.payment_window.resizable(0, 0)
        self.payment_window.mainloop()
RunMain = Payment_screen()