#Sign In Page

from tkinter import *
from tkinter import ttk
import subprocess
import sqlite3

root = Tk()
root.title("Sign In Page")
root.geometry("500x250+10+10")

class SignIn:
    def __init__(self,master):

        # Database initialization
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()

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
        self.passwordEntry.config(show = "*")
        self.passwordEntry.grid(row=1,column=1)

        self.passwordMessage = ttk.Label(master)
        self.passwordMessage.config()
        self.passwordMessage.grid(row=1,column=2)

        #Sign In
        self.signIn = ttk.Button(master)
        self.signIn.config(text = "Sign In",command=lambda: [self.validate_credentials()])
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

    def validate_credentials(self):
        email = self.emailEntry.get()
        password = self.passwordEntry.get()

        # Check if the email and password match the records in the database
        self.cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        user = self.cursor.fetchone()

        if user:
            self.emailMessage.config(text="Login successful", foreground="green")
            self.passwordMessage.config(text="")
        else:
            self.emailMessage.config(text="Email or password is incorrect", foreground="red")
            self.passwordMessage.config(text="")

    def __del__(self):
        self.conn.close()


#-------------------------------------------------------------------------------------------------------------------------


app = SignIn(root)

root.mainloop()