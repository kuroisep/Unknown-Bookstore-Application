# import tkinter as tk
 

# window = tk.Tk()
# window.title('My Window')
# window.geometry('100x100')
 
# l = tk.Label(window, bg='white', width=20, text='empty')
# l.pack()
 
# def print_selection():
#     if (var1.get() == 1) & (var2.get() == 0):
#         l.config(text='I love Python ')
#     elif (var1.get() == 0) & (var2.get() == 1):
#         l.config(text='I love C++')
#     elif (var1.get() == 0) & (var2.get() == 0):
#         l.config(text='I do not anything')
#     else:
#         l.config(text='I love both')
 
# var1 = tk.IntVar()
# var2 = tk.IntVar()
# c1 = tk.Checkbutton(window, text='Python',variable=var1, onvalue=1, offvalue=0, command=print_selection)
# c1.pack()
# c2 = tk.Checkbutton(window, text='C++',variable=var2, onvalue=1, offvalue=0, command=print_selection)
# c2.pack()
 
# window.mainloop()




# import tkinter as tk
# root=tk.Tk()

# c1=tk.BooleanVar()
# c2=tk.BooleanVar()
# c3=tk.BooleanVar()
# c4=tk.BooleanVar()

# def get_value():
#     for c in (c1,c2,c3,c4):
#         print(c.get())

# tk.Checkbutton(root,text='checkbox1',variable=c1,).pack()
# tk.Checkbutton(root,text='checkbox2',variable=c2,).pack()
# tk.Checkbutton(root,text='checkbox3',variable=c3,).pack()
# tk.Checkbutton(root,text='checkbox4',variable=c4,).pack()
# tk.Button(root,text='get value',command=get_value).pack()

# root.mainloop()


import tkinter  as tk 
my_w = tk.Tk()
my_w.geometry("400x150")
def my_upd():
    i=0
    if(c1_v.get()==1):i=i+1
    if(c2_v.get()==1):i=i+1     
    if(i>=1):
        if(c1_v.get()!=1):c1.config(state='disabled')
        if(c2_v.get()!=1):c2.config(state='disabled')
       
    else:
        c1.config(state='normal')
        c2.config(state='normal')
c1_v=tk.IntVar(my_w)    
c1=tk.Checkbutton(my_w,text='Mele',command=my_upd,variable=c1_v)
c1.grid(row=1,column=1)

c2_v=tk.IntVar(my_w)
c2=tk.Checkbutton(my_w,text='Female',command=my_upd,variable=c2_v)
c2.grid(row=1,column=2)



my_w.mainloop()



# import PySimpleGUI as psg
# #set the theme for the screen/window
# psg.theme('TealMono')
# #define layout
# layout=[[psg.Text('Choose your Bread',size=(20, 1), font='Lucida',justification='left')],
#         [psg.Radio('Whole Wheat','rd_bread', key ='Whole Wheat'), psg.Radio('Multigrain','rd_bread', key='Multigrain'),
#          psg.Radio('Normal','rd_bread', key='Normal'),psg.Radio('Stuffed','rd_bread', key='Stuffed'),psg.Radio('Healthy seeds','rd_bread', key='Healthy seeds')],
#         [psg.Text('Choose your Toppings',size=(20, 1), font='Lucida',justification='left')],
#         [psg.Checkbox('Pepperoni',key='Pepperoni'), psg.Checkbox('Mushroom',key='Mushroom'),
#          psg.Checkbox('Corn',key='Corn'),psg.Checkbox('Cherry Tomatoes',key='Cherry Tomatoes'),psg.Checkbox('Olives',key='Olives')],
#         [psg.Text('Choose your Sauces',size=(20, 1), font='Lucida',justification='left')],
#         [psg.Checkbox('Onion',key='Onion Sauce'), psg.Checkbox('Paprika',key='Paprika'),
#          psg.Checkbox('Schezwan',key='Schezwan'),psg.Checkbox('Tandoori',key='Tandoori')],
#         [psg.Button('SAVE', font=('Times New Roman',12)),psg.Button('CANCEL', font=('Times New Roman',12))]]
# #Define Window
# win =psg.Window('Make your Pizza',layout)
# #Read  values entered by user
# e,v=win.read()
# #close first window
# win.close()
# #access all the values and if selected add them to a string
# strx=""
# for val in v:
#     if win.FindElement(val).get()==True:
#         strx=strx+ " "+ val+","
# #display string in a popup         
# psg.popup('Custom Pizza',      
#             'Your chosen pizza will be made with', strx[0:len(strx)-1]) 
