"""
Sign-up page part of Project: Hydrate.

Description:
 - Records user input for username and password, then various checks are done to make sure the account is unique
   and all password validation checks are passed
"""

# Imports.
import re
import subprocess

import time
import threading

from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk
import tkinter as tk

# Create the main window
root = Tk()
root.geometry("495x595")
user_signups_file = "db\\user_logins.txt"
root.iconbitmap(default="assets\icon.ico")  # Set the window icon.

root.resizable(width=False, height=False)
root.title("Project Hydrate Sign-Up")  # Set the window title.

# Function to center the window on the screen.
def center_window(window):
    """
    Center the given window on the screen.
    
    Parameters:
    - window: The Tkinter window to be centered.
    """

    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    
    window.geometry(f"{width}x{height}+{x}+{y}")

# Center the main window on the screen
center_window(root)

# Function to navigate to the main window.
def goto_main_window():
    """
    Close the current window and open the main window.
    """
    
    root.destroy()
    subprocess.call(["python", "main.py"])

# Load and resize images for the GUI elements.
menu_icon = Image.open("assets\iconmain.png")
waves_bottom = Image.open("assets\wavesfullcropped.png")
title_text_icon = Image.open("assets\\titletext.png")
button_image = Image.open("assets\\buttonimage.png")
back_button_image = Image.open("assets\\backbutton.png")

menu_icon = menu_icon.resize((108, 141))
waves_bottom = waves_bottom.resize((495, 395))
title_text_icon = title_text_icon.resize((182, 70))
button_image = button_image.resize((200, 30), resample=Image.BICUBIC)
back_button_image = back_button_image.resize((30, 30), resample=Image.BICUBIC)

# Convert images to Tkinter-compatible format.
menu_icon_tk = ImageTk.PhotoImage(menu_icon)
waves_bottom_tk = ImageTk.PhotoImage(waves_bottom)
title_text_icon_tk = ImageTk.PhotoImage(title_text_icon)
button_image_tk = ImageTk.PhotoImage(button_image)
back_button_image_tk = ImageTk.PhotoImage(back_button_image)

# Create labels and buttons with the corresponding images.
menu_icon_label = Label(root, image=menu_icon_tk)
waves_bottom_label = Label(root, image=waves_bottom_tk)
title_text_label = Label(root, image=title_text_icon_tk)
back_button = ttk.Button(root, image=back_button_image_tk, compound="center", width=0, command=goto_main_window)

# Set up variables and labels for user input and warnings.
username_variable = StringVar()
username_variable.set("")

password_variable = StringVar()
password_variable.set("")

username_changed = BooleanVar()
username_changed.set(False)

password_changed = BooleanVar()
password_changed.set(False)

username_warning_showing = BooleanVar()
username_warning_showing.set(False)

password_warning_showing = BooleanVar()
password_warning_showing.set(False)

account_created_text = BooleanVar()
account_created_text.set(False)

# Function to display a warning if the username already exists.
def username_exists_warning():
    """
    Display a warning if the username already exists.
    """

    if not username_warning_showing.get():
        account_created_text.set(True)
        
        if username_warning_variable.get() == "Username already exists":
            username_exists_label.place(x=170, y=370)
        else:
            username_exists_label.place(x=135, y=370)            
        
        time.sleep(2)
        username_exists_label.place_forget()
        account_created_text.set(False)

# Function to display a success message after creating an account.
def account_created_success():
    """
    Display a success message after successfully creating an account.
    """

    if not account_created_text.get():
        account_created_text.set(True)
        account_created_label.place(x=151, y=370)
        
        time.sleep(3)
        account_created_label.place_forget()
        account_created_text.set(False)

# Function to display a warning for invalid passwords.
def invalid_password_warning():
    """
    Display a warning for invalid passwords.
    """

    password_warning_label.place(relx=0.5, y=420, anchor=tk.CENTER)
    
    time.sleep(2)
    password_warning_label.place_forget()

# Function to handle the sign-up process.
def send_signup_request():
    """
    Handle the sign-up process by validating inputs and creating accounts.
    """
    
    if username_changed.get() and password_changed.get():
        password = password_variable.get()
        
        # Check password length
        if len(password) < 8:
            password_warning_variable.set("Password should be at least 8 characters long")
            password_warning_thread = threading.Thread(target=invalid_password_warning)
            password_warning_thread.start()
            return

        # Check for a capital letter
        if not re.search(r'[A-Z]', password):
            password_warning_variable.set("Password should contain at least one capital letter")
            password_warning_thread = threading.Thread(target=invalid_password_warning)
            password_warning_thread.start()
            return

        # Check for a number
        if not re.search(r'\d', password):
            password_warning_variable.set("Password should contain at least one number")
            password_warning_thread = threading.Thread(target=invalid_password_warning)
            password_warning_thread.start()
            return
        
        # Rest of the code for signing up the user
        user_signups = open(user_signups_file, "r")
        user_signups_lines = user_signups.readlines()

        for user_signup in user_signups_lines:
            signup_info = user_signup.split("=")
            user = signup_info[1]

            if user.upper().strip() == username_variable.get().upper().strip():
                if not username_warning_showing.get():
                    username_warning_variable.set("Username already exists")
                    username_warning_thread = threading.Thread(target=username_exists_warning)
                    username_warning_thread.start()
                    return

        if not re.match("^[a-zA-Z0-9_]+$", username_variable.get()):
            username_warning_variable.set("Username contains invalid characters")
            username_warning_thread = threading.Thread(target=username_exists_warning)
            username_warning_thread.start()
            return

        if not username_variable.get().upper().strip() == user.strip():
            user_id = len(user_signups_lines) + 1
            user_signups.close()
            user_signup_string = (
                str(user_id)
                + "="
                + username_variable.get().upper()
                + "="
                + password_variable.get()
                + "="
                + username_variable.get()
                + "\n"
            )

            user_logins = open(user_signups_file, "a")
            user_logins.write(user_signup_string)
            user_logins.close()

            if not account_created_text.get():
                account_created_success_thread = threading.Thread(target=account_created_success)
                account_created_success_thread.start()
    else:
        password_warning_variable.set("Sign-up rejected as one or both inputs were left blank")
        password_warning_thread = threading.Thread(target=invalid_password_warning)
        password_warning_thread.start()
        return

# Create the sign-up button and labels.
signup_button = ttk.Button(root, text="S I G N  U P", image=button_image_tk, compound="center", command=send_signup_request)
signup_label = Label(root, text="A C C O U N T  S I G N  U P", fg="darkgray", font=("Arial", 14))
username_warning_variable = StringVar()
username_warning_variable.set("Username already exists")

password_warning_variable = StringVar()
password_warning_variable.set("Password must include at least 8 characters, a capital letter and a number")

password_warning_label = ttk.Label(root, textvariable=password_warning_variable, foreground="red", font=("Arial", 10))
username_exists_label = ttk.Label(root, textvariable=username_warning_variable, foreground="red", font=("Arial", 10))
account_created_label = ttk.Label(root, text="Account successfully created!", foreground="#00ad12", font=("Arial", 10, "bold"))

style = ttk.Style()
style.configure("TButton", foreground="gray")
style.configure("TButton", font=("Arial", 16))

# Place the GUI elements in the window.
waves_bottom_label.place(x=-2, y=210)
menu_icon_label.place(x=191, y=40)
title_text_label.place(x=153, y=200)
back_button.place(x=20, y=20)

# Event handling for username and password fields.
def username_focus(event):
    """
    Event handler when username field gains focus.
    """

    if username_box.get() == "Username":
        if not username_changed.get():
            username_changed.set(True)
            username_box.delete(0, len(username_box.get()))
            username_box.configure(foreground="black")

def username_leave(event):
    """
    Event handler when username field loses focus.
    """

    if username_box.get() == "":
        if username_changed.get():
            username_changed.set(False)
            username_box.insert(0, "Username")
            username_box.configure(foreground="gray")

def password_focus(event):
    """
    Event handler when password field gains focus.
    """

    if password_box.get() == "Password":
        if not password_changed.get():
            password_changed.set(True)
            password_box.delete(0, len(password_box.get()))
            password_box.configure(foreground="black", show="*")

def password_leave(event):
    """
    Event handler when password field loses focus.
    """

    if password_box.get() == "":
        if password_changed.get():
            password_changed.set(False)
            password_box.insert(0, "Password")
            password_box.configure(foreground="gray", show="")

username_box = ttk.Entry(root, textvariable=username_variable, width=34, foreground="gray")
password_box = ttk.Entry(root, textvariable=password_variable, width=34, foreground="gray")

username_box.insert(0, "Username")
username_box.bind("<FocusIn>", username_focus)
username_box.bind("<FocusOut>", username_leave)

password_box.insert(0, "Password")
password_box.bind("<FocusIn>", password_focus)
password_box.bind("<FocusOut>", password_leave)

signup_label.place(x=122, y=310)
username_box.place(x=140, y=350)
password_box.place(x=140, y=390)

signup_button.place(x=140, y=430)

title_text_label.lower(signup_button)
menu_icon_label.lower(title_text_label)
waves_bottom_label.lower(menu_icon_label)

root.mainloop() # Start the main event loop.