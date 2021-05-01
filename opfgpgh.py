import tkinter as tk
from tkinter import ttk
   
  
Num_Vertical = ("\nA\nB\nC\nD\nE\nF\nG\n\
H\nI\nJ\nK\nL\nM\nN\nO\nP\nQ\nR\nS\nT\n\
U\nV\nW\nX\nY\nZ")
Num_Horizontal = ("A  B  C  D  E  F  G  H \
I  J  K  L  M  N  O  P  Q  R  S  T  U  V \
W  X  Y  Z")
   
window = tk.Tk()
window.geometry("250x200+800+400")
window.overrideredirect(1)


style = ttk.Style(window)
# Import the tcl file
window.tk.call('source', 'UnknownShop/azure-dark.tcl')

# Set the theme with the theme_use method
style.theme_use('azure-dark')
style.configure('flat.TButton', borderwidth=0)


SVBar = ttk.Scrollbar(window)
SVBar.pack (side = tk.RIGHT, 
            fill = "y")
   
SHBar = ttk.Scrollbar(window, 
                     orient = tk.HORIZONTAL)
SHBar.pack (side = tk.BOTTOM, 
            fill = "x")
   
TBox = tk.Text(window, 
               height = 500, 
               width = 500,
               yscrollcommand = SVBar.set,
               xscrollcommand = SHBar.set, 
               wrap = "none")
  
TBox = tk.Text(window,
               height = 500,
               width = 500,
               yscrollcommand = SVBar.set, 
               xscrollcommand = SHBar.set, 
               wrap = "none")
  
TBox.pack(expand = 0, fill = tk.BOTH)
   
TBox.insert(tk.END, Num_Horizontal)
TBox.insert(tk.END, Num_Vertical)
   
SHBar.config(command = TBox.xview)
SVBar.config(command = TBox.yview)
   
window.mainloop()