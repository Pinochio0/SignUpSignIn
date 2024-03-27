#Sign Up Page

from tkinter import *
from tkinter import ttk

root = Tk()

class SignUp:
    def __init__(self,master):

        #Email
        self.label1 = ttk.Label(master)
        self.label1.config(text = "Email: ")
        self.label1.grid(row=0,column=0)

        self.entry1 = ttk.Entry(master)
        self.entry1.config()
        self.entry1.grid(row=0,column=1)

        #Password
        self.label2 = ttk.Label(master)
        self.label2.config(text = "Password: ")
        self.label2.grid(row=1,column=0)

        self.entry2 = ttk.Entry(master)
        self.entry2.config()
        self.entry2.grid(row=1,column=1)

        #confirm password
        self.label3 = ttk.Label(master)
        self.label3.config(text = "Confirm Password: ")
        self.label3.grid(row=2,column=0)

        self.entry3 = ttk.Entry(master)
        self.entry3.config()
        self.entry3.grid(row=2,column=1)

        #Sign Up Button
        self.button1 = ttk.Button(master)
        self.button1.config(text = "Sign Up", command=lambda: [self.emailVerification(),self.password(),self.passwordVerification()])
        self.button1.grid(row=3,column=1)

        #Already Have An Account
        self.button2 = ttk.Button(master)
        self.button2.config(text = "Already Have An Account?")
        self.button2.grid(row=4,column=1)

    def emailVerification(self):
        email = self.entry1.get()
        print(email)
        
        if '@' not in email:
            print("Error", "Invalid email format: '@' symbol is missing")
        else:
            print("Email is valid.")

    def password(self):
        password = self.entry2.get()
        print(password)

        if password == "":
            print("Error, no password provided")

    def passwordVerification(self):
        password2 = self.entry3.get()
        print(password2)

        if password2 == "":
            print("Error, no confirmation password provided")

        if self.entry2.get() == self.entry3.get():
            print("Both password match.")
        else:
            print("Passwords do not match.")
        





app = SignUp(root)

root.mainloop()