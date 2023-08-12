"""
Main page part of Project: Hydrate (first page that will open).

Description:
 - This part of the program is the first thing the user will see when opening the app, it is the part that will give
   the user the option to either sign up or log in.
"""

# Imports.
import subprocess
from tkinter import *

from tkinter import ttk
from PIL import Image, ImageTk, ImageFont

# Create the main window.
root = Tk()
root.geometry("495x595")
root.iconbitmap(default="assets\icon.ico")  # Set the window icon.

root.resizable(width=False, height=False)
root.title("Project Hydrate")  # Set the window title.

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

# Function to navigate to the login window.
def goto_login_window():
    """
    Close the current window and navigate to the login window.
    """

    root.destroy()
    subprocess.call(["python", "login.py"])

# Function to navigate to the signup window.
def goto_signup_window():
    """
    Close the current window and navigate to the signup window.
    """
    
    root.destroy()
    subprocess.call(["python", "signup.py"])

# Load and resize images for the GUI elements.
menu_icon = Image.open("assets\iconmain.png")
waves_bottom = Image.open("assets\wavesfullcropped.png")
title_text_icon = Image.open("assets\\titletext.png")
button_image = Image.open("assets\\buttonimage.png")

menu_icon = menu_icon.resize((108, 141))
waves_bottom = waves_bottom.resize((495, 395))
title_text_icon = title_text_icon.resize((182, 70))
button_image = button_image.resize((200, 30), resample=Image.BICUBIC)

# Convert images to Tkinter-compatible format.
menu_icon_tk = ImageTk.PhotoImage(menu_icon)
waves_bottom_tk = ImageTk.PhotoImage(waves_bottom)
title_text_icon_tk = ImageTk.PhotoImage(title_text_icon)
button_image_tk = ImageTk.PhotoImage(button_image)

# Create labels and buttons with the corresponding images.
menu_icon_label = Label(root, image=menu_icon_tk)
waves_bottom_label = Label(root, image=waves_bottom_tk)
title_text_label = Label(root, image=title_text_icon_tk)
login_button = ttk.Button(root, text="L O G  I N", image=button_image_tk, compound="center", command=goto_login_window)
signup_button = ttk.Button(root, text="S I G N  U P", image=button_image_tk, compound="center", command=goto_signup_window)
signin_options_label = Label(root, text="S I G N  I N  O P T I O N S", fg="darkgray", font=("Arial", 14))

# Configure button styles.
style = ttk.Style()
style.configure("TButton", foreground="gray")
style.configure("TButton", font=("Arial", 16))

# Position the GUI elements on the window.
waves_bottom_label.place(x=-2, y=210)
menu_icon_label.place(x=191, y=40)
title_text_label.place(x=153, y=200)
login_button.place(x=140, y=350)
signup_button.place(x=140, y=400)
signin_options_label.place(x=130, y=310)

# Order the labels in the desired stacking order.
title_text_label.lower(login_button)
menu_icon_label.lower(title_text_label)
waves_bottom_label.lower(menu_icon_label)

root.mainloop()  # Start the main event loop.