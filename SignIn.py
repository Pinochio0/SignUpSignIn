#Sign In Page

from tkinter import *
from tkinter import ttk
import subprocess

root = Tk()
root.title("Sign In Page")
root.geometry("500x250+10+10")

class SignIn:
    def __init__(self,master):

        #Email
        self.emailLabel = ttk.Label(master)
        self.emailLabel.config(text = "Email: ")
        self.emailLabel.grid(row=0,column=0)

        self.emailEntry = ttk.Entry(master)
        self.emailEntry.config()
        self.emailEntry.grid(row=0,column=1)

        self.emailMessage = ttk.Label(master)
        self.emailMessage.config()
        self.emailMessage.grid(row=0,column=2)

        #Password
        self.passwordLabel = ttk.Label(master)
        self.passwordLabel.config(text = "Password: ")
        self.passwordLabel.grid(row=1,column=0)

        self.passwordEntry = ttk.Entry(master)
        self.passwordEntry.config()
        self.passwordEntry.grid(row=1,column=1)

        self.passwordMessage = ttk.Label(master)
        self.passwordMessage.config()
        self.passwordMessage.grid(row=1,column=2)

        #Sign In
        self.signIn = ttk.Button(master)
        self.signIn.config(text = "Sign In",command=lambda: [self.emailGrab(),self.passwordGrab()])
        self.signIn.grid(row=2,column=1)

        #Already Have An Account
        self.button2 = ttk.Button(master)
        self.button2.config(text = "Don't Have An Account?",command = self.openSignUpPage)
        self.button2.grid(row=3,column=1)

#-------------------------------------------------------------------------------------------------------------------------
    #allows transfer to sign up page
    def openSignUpPage(self):
        subprocess.Popen(['python', 'SignUp.py'])
        root.destroy()

    #grabs email
    def emailGrab(self):
        email = self.emailEntry.get()

        if '@' not in email:
            self.emailMessage.config(text = "Invalid email format: '@' symbol is missing")
        else:
            self.emailMessage.config(text = "Email is valid")

    #grabs password
    def passwordGrab(self):
        password = self.passwordEntry.get()

        if password == "":
            self.passwordMessage.config(text = "Error, no password provided")
        else:
            self.passwordMessage.config(text = "")


#-------------------------------------------------------------------------------------------------------------------------


app = SignIn(root)

root.mainloop()