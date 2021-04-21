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
