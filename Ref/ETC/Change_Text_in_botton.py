from tkinter import *  # Note: lower case "t" in tkinter
from tkinter import font as tkFont  # for convenience

# using grid
# +------+-------------+
# | btn1 |    btn2     |
# +------+------+------+
# | btn3 | btn3 | btn4 |
# +-------------+------+

root = Tk()
# tkFont.BOLD == 'bold'
helv36 = tkFont.Font(family='Helvetica', size=36, weight=tkFont.BOLD)
btn1 = Button(text='btn1', font=helv36)
btn2 = Button(text='btn2', font=helv36)
btn3 = Button(text='btn3', font=helv36)
btn4 = Button(text='btn4', font=helv36)
btn5 = Button(text='btn5', font=helv36)
root.rowconfigure((0,1), weight=1)  # make buttons stretch when
root.columnconfigure((0,2), weight=1)  # when window is resized
btn1.grid(row=0, column=0, columnspan=1, sticky='EWNS')
btn2.grid(row=0, column=1, columnspan=2, sticky='EWNS')
btn3.grid(row=1, column=0, columnspan=1, sticky='EWNS')
btn4.grid(row=1, column=1, columnspan=1, sticky='EWNS')
btn5.grid(row=1, column=2, columnspan=1, sticky='EWNS')

root.mainloop()