from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
from future.moves.tkinter import ttk

root = Tk()
root.title("aSDASDad")
root.geometry("500x500")

def graph():
    test = np.random.normal(100000,25000,5000)
    plt.hist(test,45)
    plt.show()
# MB = ttk.Button(root, text="GGGGGGg",command=graph)
# MB.pack()
graph()
# root.mainloop()