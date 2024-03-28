#Sign In Page

from tkinter import *
from tkinter import ttk
import subprocess

root = Tk()
root.title("Sign In Page")
root.geometry("350x250+10+10")

class SignIn:
    def __init__(self,master):

        #EMail
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

        #Sign In
        self.button1 = ttk.Button(master)
        self.button1.config(text = "Sign In")
        self.button1.grid(row=2,column=1)

    #Already Have An Account
        self.button2 = ttk.Button(master)
        self.button2.config(text = "Don't Have An Account?",command = self.openSignUpPage)
        self.button2.grid(row=3,column=1)

    #allows transfer to sign up page
    def openSignUpPage(self):
        subprocess.Popen(['python', 'SignUp.py'])
        root.destroy()



app = SignIn(root)

root.mainloop()