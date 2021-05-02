# from tkinter import *
# import os
  
# # Create object 
# root = Tk()
  
# # Adjust size 
# root.geometry("400x400")
# base_folder = os.path.dirname(__file__)
# icon_path = os.path.join(base_folder, 'open-book.png')
# icon = PhotoImage(file=icon_path)
# # Add image file
# # bg = PhotoImage(file = "background.jpg")
  
# # Create Canvas
# canvas1 = Canvas( root, width = 400,
#                  height = 400)
  
# canvas1.pack(fill = "both", expand = True)
  
# # Display image
# canvas1.create_image( 0, 0, image = icon, 
#                      anchor = "nw")
  
# # Add Text
# canvas1.create_text( 200, 250, text = "Welcome")
  
# # Create Buttons
# button1 = Button( root, text = "Exit")
# button3 = Button( root, text = "Start")
# button2 = Button( root, text = "Reset")
  
# # Display Buttons
# button1_canvas = canvas1.create_window( 100, 10, 
#                                        anchor = "nw",
#                                        window = button1)
  
# button2_canvas = canvas1.create_window( 100, 40,
#                                        anchor = "nw",
#                                        window = button2)
  
# button3_canvas = canvas1.create_window( 100, 70, anchor = "nw",
#                                        window = button3)
  
# # Execute tkinter
# root.mainloop()
# from main import *

# start()
# print(variable_to())

# from tkinter import *

# class MainWindow(Frame):
#     def __init__(self):
#         super().__init__()
#         self.pack(expand=Y,fill=BOTH)

#         outercanvas = Canvas(self, width=200, height=100, bg='#00ffff')
#         outercanvas.pack(expand=Y,fill=BOTH)

#         innercanvas = Canvas(outercanvas, width=100, height=50)
#         outercanvas.create_window(50, 25, anchor=NW, window=innercanvas)

#         innercanvas.create_text(10, 10, anchor=NW, text="Hello")

# root = MainWindow()
# root.mainloop()

# from tkinter import *   # from x import * is bad practice
# # from ttk import *

# # http://tkinter.unpythonic.net/wiki/VerticalScrolledFrame

# class VerticalScrolledFrame(Frame):
#     """A pure Tkinter scrollable frame that actually works!
#     * Use the 'interior' attribute to place widgets inside the scrollable frame
#     * Construct and pack/place/grid normally
#     * This frame only allows vertical scrolling

#     """
#     def __init__(self, parent, *args, **kw):
#         Frame.__init__(self, parent, *args, **kw)            

#         # create a canvas object and a vertical scrollbar for scrolling it
#         vscrollbar = Scrollbar(self, orient=VERTICAL)
#         vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
#         canvas = Canvas(self, bd=0, highlightthickness=0,
#                         yscrollcommand=vscrollbar.set)
#         canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
#         vscrollbar.config(command=canvas.yview)

#         # reset the view
#         canvas.xview_moveto(0)
#         canvas.yview_moveto(0)

#         # create a frame inside the canvas which will be scrolled with it
#         self.interior = interior = Frame(canvas)
#         interior_id = canvas.create_window(0, 0, window=interior,
#                                            anchor=NW)

#         # track changes to the canvas and frame width and sync them,
#         # also updating the scrollbar
#         def _configure_interior(event):
#             # update the scrollbars to match the size of the inner frame
#             size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
#             canvas.config(scrollregion="0 0 %s %s" % size)
#             if interior.winfo_reqwidth() != canvas.winfo_width():
#                 # update the canvas's width to fit the inner frame
#                 canvas.config(width=interior.winfo_reqwidth())
#         interior.bind('<Configure>', _configure_interior)

#         def _configure_canvas(event):
#             if interior.winfo_reqwidth() != canvas.winfo_width():
#                 # update the inner frame's width to fill the canvas
#                 canvas.itemconfigure(interior_id, width=canvas.winfo_width())
#         canvas.bind('<Configure>', _configure_canvas)


# if __name__ == "__main__":

#     class SampleApp(Tk):
#         def __init__(self, *args, **kwargs):
#             root = Tk.__init__(self, *args, **kwargs)


#             self.frame = VerticalScrolledFrame(root)
#             self.frame.pack()
#             self.label = Label(text="Shrink the window to activate the scrollbar.")
#             self.label.pack()
#             buttons = []
#             for i in range(10):
#                 buttons.append(Button(self.frame.interior, text="Button " + str(i)))
#                 buttons[-1].pack()

#     app = SampleApp()
#     app.mainloop()