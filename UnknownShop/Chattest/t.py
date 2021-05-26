#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from tkinter import *
import time

'''
Define the message sending function:
 1. Add time in the text control of <Message List Partition> in real time;
 2. Get the text content of <Send Message Partition> and add it to the text of the list partition;
 3. Clear the text content of <Send Message Partition>.
'''


def msgsend():
         msg = ' '+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+'\n'
         txt_msglist.insert(END, msg, 'green')  # Add time
         # Get the sent message, add text to the message list
         txt_msglist.insert(END, txt_msgsend.get('0.0', END))
         txt_msgsend.delete('0.0', END)  # Empty send message

'''Define the function to cancel sending the message'''
def cancel():
         txt_msgsend.delete('0.0',END) #Cancel sending message, that is, empty sending message
 
'''Binding up key'''
def msgsendEvent(event):
    if event.keysym == 'Up':
        msgsend()
 
tk = Tk()
tk.title('Chat window')
 
'''Create partition'''
f_msglist = Frame(height = 300, width = 300) #Create <Message List Partition>  
f_msgsend = Frame(height = 300, width = 300) #Create <Send Message Partition>
f_floor = Frame(height = 100, width = 300) #Create <button partition>
f_right = Frame(height = 700, width = 100) #Create <picture partition>
'''Create control'''
txt_msglist = Text(f_msglist) #Create a text control in the message list partition
txt_msglist.tag_config('green',foreground ='blue') #Create a tag in the message list partition
txt_msgsend = Text(f_msgsend) #Create a text control in the message section
txt_msgsend.bind('<KeyPress-Up>',msgsendEvent) #In the message sending section, bind the ‘UP’ key to send the message.
'''txt_right = Text(f_right) #Picture display partition to create text control'''
button_send = Button(f_floor,text ='Send',command = msgsend) #Create a button in the button partition and bind the send message function
button_cancel = Button(f_floor,text ='Cancel',command = cancel) #Create a cancel button in the partition and bind the cancel function
photo = PhotoImage(file = r'P:\62011019\2D\SEMESTER_2\DATA_STRUCTURE\Proj_2563\Ref\open-book.png')
label = Label(f_right,image = photo) #Add label to the right partition (bind picture)
label.image = photo
 
'''Partition layout'''
f_msglist.grid(row = 0,column = 0) #Message list partition
f_msgsend.grid(row = 1,column = 0) #Send message partition
f_floor.grid(row = 2,column = 0) #button partition
f_right.grid(row = 0,column = 1,rowspan = 3) #Picture shows the partition
txt_msglist.grid() #Message list text control loading
txt_msgsend.grid() #Message sending text control loading
button_send.grid(row = 0,column = 0,sticky = W) #Send button control loading
button_cancel.grid(row = 0,column = 1,sticky = W) #Cancel button control loading
label.grid() #The right partition loads the label control
 
tk.mainloop()
