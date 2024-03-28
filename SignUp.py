#Sign Up Page

from tkinter import *
from tkinter import ttk
import subprocess
import sqlite3

root = Tk()
root.title("Sign Up Page")
root.geometry("500x250+10+10")

class SignUp:
    def __init__(self,master):

        # Database initialization
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()
        self.create_table()

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

        #confirm password
        self.passwordConfLabel = ttk.Label(master)
        self.passwordConfLabel.config(text = "Confirm Password: ")
        self.passwordConfLabel.grid(row=2,column=0)

        self.passwordConfEntry = ttk.Entry(master)
        self.passwordConfEntry.config()
        self.passwordConfEntry.grid(row=2,column=1)

        self.passwordConfMessage = ttk.Label(master)
        self.passwordConfMessage.config()
        self.passwordConfMessage.grid(row=2,column=2)

        #Sign Up Button
        self.button1 = ttk.Button(master)
        self.button1.config(text = "Sign Up", command=lambda: [self.create_table(),self.signup()])
        self.button1.grid(row=3,column=1)

        #Already Have An Account
        self.button2 = ttk.Button(master)
        self.button2.config(text = "Already Have An Account?",command = self.openSignInPage)
        self.button2.grid(row=4,column=1)

#-------------------------------------------------------------------------------------------------------------------------

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                email TEXT NOT NULL,
                                password TEXT NOT NULL)''')
        self.conn.commit()

    def signup(self):
        email = self.emailEntry.get()
        password = self.passwordEntry.get()
        password_conf = self.passwordConfEntry.get()

        if '@' not in email:
            self.emailMessage.config(text="Invalid email format: '@' symbol is missing")
        elif not password:
            self.passwordMessage.config(text="Error, no password provided")
        elif password != password_conf:
            self.passwordConfMessage.config(text="Passwords do not match")
        else:
            self.cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
            self.conn.commit()
            self.emailMessage.config(text="User signed up successfully")
            self.passwordMessage.config(text="")
            self.passwordConfMessage.config(text="")

    #allows transfer to sign in page
    def openSignInPage(self):
        subprocess.Popen(['python', 'SignIn.py'])
        root.destroy()

        
#-------------------------------------------------------------------------------------------------------------------------

app = SignUp(root)

root.mainloop()