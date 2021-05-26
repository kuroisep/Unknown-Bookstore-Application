from tkinter import *
from tkinter import ttk
import tkinter as tk



root = Tk()
frame = Frame(root)
frame.pack()

s = ttk.Style(root)
root.tk.call('source', 'UnknownShop/azure.tcl')
s.theme_use('azure')

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="Red",background = 'red', foreground = 'white')
redbutton.pack( side = LEFT )

greenbutton = ttk.Button(frame, text="Brown", )
greenbutton.pack( side = LEFT )

bluebutton = ttk.Button(frame, text="Blue", )
bluebutton.pack( side = LEFT )

checkframe = ttk.LabelFrame(root, text='Checkbuttons', width=210, height=200)
checkframe.place(x=20, y=12)
bluebutton1 = ttk.Button(checkframe, text="Blue", )
bluebutton1.pack()




blackbutton = ttk.Button(bottomframe, text="Black", )
blackbutton.pack( side = BOTTOM )

root.mainloop()

