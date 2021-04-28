from tkinter import Tk,Button,Label,IntVar,ttk
from tkinter.ttk import Progressbar


class ProgressApp(Tk):

    def __init__(self):
        super().__init__()
        self.value = IntVar()
        self.value.set(0)
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("blue.Horizontal.TProgressbar", background='light green')
        self.progress_bar = Progressbar(self, orient="horizontal", mode="determinate", style="blue.Horizontal.TProgressbar",maximum=100,variable=self.value)
        # stop_button = Button(self, text='Stop', command=self.stop_progress_bar)
        # start_button = Button(self, text='Start', command=self.start_progress_bar)
        # increment_button = Button(self, text='Increment', command=self.increment)
        self.start_progress_bar()
        label = Label(self, text="Progess Bar")

        label.grid(row=0, column=0)
        self.progress_bar.grid(row=0, column=1)

        label2 = Label(self, font=20)
        label2.config(text = self.value.get())
        label2.grid(row=1, column=1)



        # start_button.grid(row=1,column=0)
        # stop_button.grid(row=1,column=1)
        # increment_button.grid(row=2,column=0)

    def stop_progress_bar(self):
        self.progress_bar.stop()

    def start_progress_bar(self):
        self.progress_bar.start()
        self.progress_bar.step(100)
        

    def increment(self):
        self.value.set(self.value.get()+5)



progressApp = ProgressApp()
progressApp.mainloop()




# import tkinter as tk
# from tkinter.ttk import Progressbar
# from tkinter import ttk
# canv = tk.Tk()
# canv.title("Tkinter Progressbar")
# canv.geometry('250x100')
# style = ttk.Style()
# style.theme_use('default')
# style.configure("grey.Horizontal.TProgressbar", background='light green')
# bar = Progressbar(canv, length=180, style='grey.Horizontal.TProgressbar')
# bar['value'] = 200
# bar.grid(column=0, row=0)
# canv.mainloop()