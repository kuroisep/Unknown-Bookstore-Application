from tkinter import *

root = Tk()
root.title('Codemy.com - Auto Select/Search')
# root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x300")

# Update the listbox
def update(data):
	# Clear the listbox
	my_list.delete(0, END)

	# Add toppings to listbox
	for item in data:
		my_list.insert(END, item)

# Update entry box with listbox clicked
def fillout(e):
	# Delete whatever is in the entry box
	my_entry.delete(0, END)

	# Add clicked list item to entry box
	my_entry.insert(0, my_list.get(ANCHOR))

# Create function to check entry vs listbox
def check(e):
	# grab what was typed
	typed = my_entry.get()

	if typed == '':
		data = toppings
	else:
		data = []
		for item in toppings:
			if typed.lower() in item.lower():
				data.append(item)

	# update our listbox with selected items
	update(data)				


# Create a label
my_label = Label(root, text="Start Typing...",
	font=("Helvetica", 14), fg="grey")

my_label.pack(pady=20)

# Create an entry box
my_entry = Entry(root, font=("Helvetica", 20))
my_entry.pack()

# Create a listbox
my_list = Listbox(root, width=50)
my_list.pack(pady=40)

# Create a list of pizza toppings
toppings = ["Pepperoni", "Peppers", "Mushrooms",
	"Cheese", "Onions", "Ham", "Taco"]

# Add the toppings to our list
update(toppings)

# Create a binding on the listbox onclick
my_list.bind("<<ListboxSelect>>", fillout)

# Create a binding on the entry box
my_entry.bind("<KeyRelease>", check)

root.mainloop()

# from tkinter import *

# # First create application class


# class Application(Frame):

#     def __init__(self, master=None):
#         Frame.__init__(self, master)

#         self.lbox_list = [('Adam', 'Mitric' ),
#                            ('Lucy', 'Devic'  ), 
#                            ('Bob' , 'Freamen'), 
#                            ('Amanda', 'Ling' ), 
#                            ('Susan', 'Cascov')]
#         self.pack()
#         self.create_widgets()

#     # Create main GUI window
#     def create_widgets(self):
#         self.search_var = StringVar()
#         self.search_var.trace("w", lambda name, index, mode: self.update_list())
#         self.entry = Entry(self, textvariable=self.search_var, width=13)
#         self.lbox1 = Listbox(self, width=20, height=15)
#         self.lbox2 = Listbox(self, width=20, height=15)         # Second List Box. Maybe you can use treeview ? 

#         self.entry.grid(row=0, column=0, padx=10, pady=3)
#         self.lbox1.grid(row=1, column=0, padx=10, pady=5)
#         self.lbox2.grid(row=1, column=1, padx=10, pady=5)

#         # Function for updating the list/doing the search.
#         # It needs to be called here to populate the listbox.
#         self.update_list()

#     def update_list(self):
#         search_term = self.search_var.get()

#         # Just a generic list to populate the listbox

#         self.lbox1.delete(0, END)
#         self.lbox2.delete(0, END)       # Deletng from second listbox

#         passed = []                     # Need this to check for colisions

#         for item in self.lbox_list:
#             if search_term.lower() in item[0].lower():
#                 self.lbox1.insert(END, item[0])
#                 self.lbox2.insert(END, item[1])
#                 passed.append(item)

#         for item in self.lbox_list:
#             if search_term.lower() in item[1].lower() and item not in passed:
#                 self.lbox1.insert(END, item[0])
#                 self.lbox2.insert(END, item[1])


# root = Tk()
# root.title('Filter Listbox Test')
# app = Application(master=root)
# app.mainloop()