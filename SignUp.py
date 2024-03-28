#Sign Up Page

from tkinter import *
from tkinter import ttk
import subprocess
import sqlite3
import os

root = Tk()
root.title("Sign Up Page")
root.geometry("500x250+10+10")

class SignUp:
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
        self.button1.config(text = "Sign Up", command=lambda: [self.emailVerification(),self.password(),self.passwordVerification(),self.create_table(),self.sign_up(),self.check_database()])
        self.button1.grid(row=3,column=1)

        #Already Have An Account
        self.button2 = ttk.Button(master)
        self.button2.config(text = "Already Have An Account?",command = self.openSignInPage)
        self.button2.grid(row=4,column=1)

#-------------------------------------------------------------------------------------------------------------------------

    #verifies email is properly entered
    def emailVerification(self):
        email = self.emailEntry.get()

        if '@' not in email:
            self.emailMessage.config(text = "Invalid email format: '@' symbol is missing")
        else:
            self.emailMessage.config(text = "Email is valid")

    #verifies password is properly entered
    def password(self):
        password = self.passwordEntry.get()

        if password == "":
            self.passwordMessage.config(text = "Error, no password provided")
        else:
            self.passwordMessage.config(text = "Password is valid")

    #verifies confirmation password is properly entered
    def passwordVerification(self):
        password2 = self.passwordConfEntry.get()

        if self.passwordEntry.get() != self.passwordConfEntry.get():
            self.passwordConfMessage.config(text = "Passwords do not match")
        else:
            self.passwordConfMessage.config(text = "Passwords match")

        if password2 == "":
            self.passwordConfMessage.config(text = "Error, no confirmation password provided")

    #allows transfer to sign in page
    def openSignInPage(self):
        subprocess.Popen(['python', 'SignIn.py'])
        root.destroy()

    def create_table(self):
        conn = sqlite3.connect('user_database.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, email TEXT, password TEXT)''')
        conn.commit()
        conn.close()

    def insert_data(self, email, password):
        conn = sqlite3.connect('user_database.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
        conn.commit()
        conn.close()

    def sign_up(self):
        email = self.emailEntry.get()
        password = self.passwordEntry.get()
        self.insert_data(email, password)
        print("User signed up successfully.")

    def check_database(self):
        if os.path.exists('user_database.db'):
            conn = sqlite3.connect('user_database.db')
            c = conn.cursor()
            c.execute("SELECT COUNT(*) FROM users")
            count = c.fetchone()[0]
            conn.close()
            if count > 0:
                print("Database exists and has been populated.")
            else:
                print("Database exists but has not been populated yet.")
        else:
            print("Database does not exist.")
        
#-------------------------------------------------------------------------------------------------------------------------

app = SignUp(root)

root.mainloop()