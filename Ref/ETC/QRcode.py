# from tkinter import *
# # pip install Pillow qrcode
# import qrcode  # https://pypi.python.org/pypi/qrcode
# from PIL import Image, ImageTk


# def create_qrcode(text):
#     qr = qrcode.QRCode()
#     qr.add_data(text)
#     qr.make(fit=True)
#     img = qr.make_image(fill_color="white", back_color="black")
#     return img


# def demo():
#     def on_click(e):
#         input_text = txt.get("0.0", "end-1c") # "0.0" get text from the beginning (from first line, first character
#         print(input_text)
#         img = create_qrcode(input_text).resize((250, 250))
#         imgTk = ImageTk.PhotoImage(img)
#         qr.configure(image=imgTk)
#         qr.image = imgTk

#     root = Tk()
#     root.title("QR code generator")
#     root.option_add("*Font", "consolas 20")
#     Label(root, text="enter text").grid(row=0, column=0)
#     txt = Text(root, height=4, width=30, fg="green")
#     txt.insert(END, "lily")
#     txt.grid(row=1, column=0)
#     btn = Button(root, text="create QR Code", bg="gold")
#     btn.grid(row=2, column=0)
#     btn.bind("<Button-1>", on_click)
#     qr = Label(root) # QR Code placeholder
#     qr.grid(row=0, column=1, rowspan=3)
#     root.mainloop()


# if __name__ == '__main__':
#     # create_qrcode("lily").show()
#     demo()



#BAr code
import barcode
from barcode.writer import ImageWriter
from PIL import ImageTk
import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter barcode test")
        
        self.label = tk.Label(self, text="Input code128:")
        self.label.grid(row=0, column=0)
        self.barcode = tk.StringVar()
        self.barcode.set('Python tkiner')
        self.entry = tk.Entry(self, textvariable=self.barcode,width=50)
        self.entry.grid(row=0, column=1, columnspan=2)
        self.show_button = tk.Button(self, text="Show a barcode")
        self.show_button.bind("<Button-1>", self.create_image)
        self.show_button.grid(row=1,column=1)
        self.save_button = tk.Button(self, text="Save a barcode image")
        self.save_button.bind("<Button-1>", self.save_image)
        self.save_button.grid(row=1,column=0)
        self.canvas = tk.Canvas(self, background="white")
        self.canvas.grid(row=2,columnspan=3,sticky=tk.NSEW)
        self.update()
        self.create_image(None)
        
    def create_image(self, event):
        data = self.barcode.get()
        if not data:
            return
        try:
            code128 = barcode.get('code128', data, writer=ImageWriter())
        except barcode.errors.IllegalCharacterError as e:
            mb.showerror("Error", e)
            return
        image = code128.render()
        photo = ImageTk.PhotoImage(image)

        self.canvas.delete(tk.ALL)
        self.canvas.create_image(self.canvas.winfo_width()//2,self.canvas.winfo_height()//2,image=photo)
        self.image = photo
        
    def save_image(self, event):
        data = self.barcode.get()
        if not data:
            return
        try:
            code128 = barcode.get('code128', data, writer=ImageWriter())
        except barcode.errors.IllegalCharacterError as e:
            mb.showerror("Error", e)
            self.update_idletasks()
            return
        filename = fd.asksaveasfilename()
        if filename:
            code128.save(filename)
        

if __name__ == '__main__':
    application = Application()
    application.mainloop()