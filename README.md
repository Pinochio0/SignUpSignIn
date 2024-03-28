User Authentication System

Description:
This Python program implements a simple user authentication system utilizing the Tkinter library for creating graphical user interfaces. The system consists of two main components: a sign-up page and a sign-in page. Users are prompted to enter their email and password to either create a new account or log in to an existing one.

Files:

signup.py: This file contains the code for the sign-up page. Users input their email and password to create a new account.
signin.py: This file contains the code for the sign-in page. Users input their email and password to log in to their account.
user.db: This file stores the registered users' credentials. Each line represents a user with their email and hashed password.
Dependencies:

Python 3.x
Tkinter library (usually comes pre-installed with Python)
Setup:

Ensure you have Python installed on your system. If not, download and install Python from the official website: Python.org.
Clone or download the project files from the repository.
Open a terminal or command prompt and navigate to the directory containing the project files.
Run the following commands to execute the sign-up and sign-in pages:
Copy code
python signup.py
python signin.py
Usage:

Sign-Up Page:
Enter your email and password.
Click the "Sign Up" button to create a new account.
If the email is already registered or the password is not strong enough, appropriate error messages will be displayed.
Sign-In Page:
Enter your registered email and password.
Click the "Sign In" button to log in to your account.
If the credentials are correct, you will be logged in. Otherwise, an error message will be displayed.

Author:

Skyler Emery

This project is developed for educational and demonstration purposes. It may not be suitable for production environments without further enhancements and security considerations.