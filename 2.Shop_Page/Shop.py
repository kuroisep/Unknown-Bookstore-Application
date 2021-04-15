# import tkinter as tk

# shop_window = tk.Tk()
# shop_window.title("Register")
# x = (700) - (750/2)
# y = (420) - (500/2)
# shop_window.geometry("1280x720+%d+%d" % (x, y))




from tkinter import *
import webbrowser

def callback(url):
    webbrowser.open_new(url)

root = Tk()
link1 = Label(root, text="Google Hyperlink", fg="blue", cursor="hand2")
link1.pack()
link1.bind("<Button-1>", lambda e: callback("http://www.google.com"))

link2 = Label(root, text="Ecosia Hyperlink", fg="blue", cursor="hand2")
link2.pack()
link2.bind("<Button-1>", lambda e: callback("http://www.ecosia.org"))

root.mainloop()






















# shop_window.mainloop()