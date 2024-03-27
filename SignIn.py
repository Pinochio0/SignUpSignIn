#Sign In Page

from tkinter import *
from tkinter import ttk

root = Tk()

class SignIn:
    def __init__(self,master):
        self.label1 = ttk.Label(master)
        self.label1.config(text = "Email: ")
        self.label1.grid(row=0,column=0)

        self.entry1 = ttk.Entry(master)
        self.entry1.config()
        self.entry1.grid(row=0,column=1)

        self.label2 = ttk.Label(master)
        self.label2.config(text = "Password: ")
        self.label2.grid(row=1,column=0)

        self.entry2 = ttk.Entry(master)
        self.entry2.config()
        self.entry2.grid(row=1,column=1)

        self.button1 = ttk.Button(master)
        self.button1.config(text = "Sign In")
        self.button1.grid(row=2,column=1)



app = SignIn(root)

root.mainloop()