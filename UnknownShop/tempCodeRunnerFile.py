username_info = self.username.get()
        password_info = self.password.get()
        confpassword_info = self.confpassword.get()
        name_info = self.name.get()
        lastname_info = self.lastname.get()
        email_info = self.email.get()
        gender_info = 'MALE'
        tel_info = self.telphone.get()
        birthday_info = str(self.birth_date_entry.get()) + '/' +  str(self.birth_month_entry.get()) + '/' + str(self.birth_year_entry.get())

        email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")

        df = pandas.read_csv('login.csv')
        checkuser = df['USER'].tolist()
        if username_info in checkuser:
            messagebox.showinfo("Info", "This Username Already Exists",
                                parent=self.register_screen)

        elif (username_info == ''):
            messagebox.showinfo("Info", "Please Enter Username",
                                parent=self.register_screen)

        elif (password_info == ''):
            messagebox.showinfo("Info", "Please Enter Password",
                                parent=self.register_screen)
        elif (len(password_info) < 8):
            messagebox.showinfo("Info", "Password Must Habe At Least 8 Characters",
                                parent=self.register_screen)

        elif (confpassword_info == ''):
            messagebox.showinfo(
                "Info", "Please Enter Confirm Password", parent=self.register_screen)

        elif (password_info != confpassword_info):
            messagebox.showerror("Error", "Password Not Match",
                                parent=self.register_screen)
            self.password_entry.delete(0, END)
            self.confpassword_entry.delete(0, END)

        elif (name_info == ''):
            messagebox.showinfo(
                "Info", "Please Enter First Name", parent=self.register_screen)

        elif (lastname_info == ''):
            messagebox.showinfo("Info", "Please Enter Last Name",
                                parent=self.register_screen)

        elif (self.gender1.get() == 0 and self.gender2.get() == 0):
            messagebox.showinfo(
                "Error", "Please Select Your Gender", parent=self.register_screen)

        elif (email_info == ''):
            messagebox.showinfo(
                "Info", "Please Enter Your Email", parent=self.register_screen)

        elif (email_regex.match(email_info) == None):
            messagebox.showerror("Error", "Email Invalid", parent=self.register_screen)

        elif (tel_info == ''):
            messagebox.showinfo(
                "Info", "Please Enter Phone Number", parent=self.register_screen)
        
        elif (tel_info.isdigit() == False or len(tel_info) != 10):
            messagebox.showerror("Error", "Phone Number Invalid",parent=self.register_screen)
            self.telphone_entry.delete(0,END)
            