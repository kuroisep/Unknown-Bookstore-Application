import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Create a style
style = ttk.Style(root)

# Import the tcl file
root.tk.call('source', 'azure.tcl')

# Set the theme with the theme_use method
style.theme_use('azure')

# A themed button
button = ttk.Button(root, text='I\'m a themed button')
button.pack(pady=20)

root.mainloop()