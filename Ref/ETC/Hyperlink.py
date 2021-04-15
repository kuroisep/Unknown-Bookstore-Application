# from tkinter import *
# import webbrowser

# def callback(url):
#     webbrowser.open_new(url)

# root = Tk()
# link1 = Label(root, text="Google Hyperlink", fg="blue", cursor="hand2")
# link1.pack()
# link1.bind("<Button-1>", lambda e: callback("http://www.google.com"))

# link2 = Label(root, text="Ecosia Hyperlink", fg="blue", cursor="hand2")
# link2.pack()
# link2.bind("<Button-1>", lambda e: callback("http://www.ecosia.org"))

# root.mainloop()


import tkinter as t
import webbrowser


class Link(t.Label):
    
    def __init__(self, master=None, link=None, fg='grey', font=('Arial', 10), *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.default_color = fg # keeping track of the default color 
        self.color = 'blue'   # the color of the link after hovering over it 
        self.default_font = font    # keeping track of the default font
        self.link = link 

        """ setting the fonts as assigned by the user or by the init function  """
        self['fg'] = fg
        self['font'] = font 

        """ Assigning the events to private functions of the class """

        self.bind('<Enter>', self._mouse_on)    # hovering over 
        self.bind('<Leave>', self._mouse_out)   # away from the link
        self.bind('<Button-1>', self._callback) # clicking the link

    def _mouse_on(self, *args):
        """ 
            if mouse on the link then we must give it the blue color and an 
            underline font to look like a normal link
        """
        self['fg'] = self.color
        self['font'] = self.default_font + ('underline', )

    def _mouse_out(self, *args):
        """ 
            if mouse goes away from our link we must reassign 
            the default color and font we kept track of   
        """
        self['fg'] = self.default_color
        self['font'] = self.default_font

    def _callback(self, *args):
        webbrowser.open_new(self.link)  


root = t.Tk()
root.title('Tkinter Links !')
root.geometry('300x200')
root.configure(background='LightBlue')

URL = 'www.python.org'

link = Link(root, URL, font=('sans-serif', 20), text='Python', bg='LightBlue')
link.pack(pady=50)

root.mainloop()