"""
Loading screen part of Project: Hydrate.

Description:
 - This part of the program is purely aesthetical, as there really isn't a reason to have a loading bar, but I thought it would
   just make the program look a bit neater to have a custom loading bar. This just switches between numerous images to give
   the impression that the loading bar is completing
"""

# Imports.
import subprocess
import sys

import threading
from tkinter import *

from tkinter import ttk
from PIL import Image, ImageTk

# Create the main window.
root = Tk()
root.geometry("495x595")

# Create the username variable.
recieved_username = ""

# Check if a username is provided.
if len(sys.argv) > 1:
    recieved_username = sys.argv[1]
    print(recieved_username)

# If no username is received, set it to "Guest".
if recieved_username == "":
    recieved_username = "Guest"

# Set the window icon and title.
root.iconbitmap(default="assets\icon.ico")
root.resizable(width=False, height=False)
root.title("Project Hydrate")

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

# Center the main window.
center_window(root)

# Load images and create image objects.
menu_icon = Image.open("assets\\iconmain.png")
waves_bottom = Image.open("assets\waveshalf.png")
title_text_icon = Image.open("assets\\titletext.png")
button_image = Image.open("assets\\buttonimage.png")
progress_bar_image_1 = Image.open("assets\loadingbar1percentage.png")
progress_bar_image_2 = Image.open("assets\loadingbar2percentage.png")
progress_bar_image_3 = Image.open("assets\loadingbar3percentage.png")
progress_bar_image_4 = Image.open("assets\loadingbar4percentage.png")
progress_bar_image_5 = Image.open("assets\loadingbar5percentage.png")
progress_bar_image_6 = Image.open("assets\loadingbar6percentage.png")

# Resize the images.
menu_icon = menu_icon.resize((108, 141))
waves_bottom = waves_bottom.resize((495, 395))
title_text_icon = title_text_icon.resize((182, 70))
progress_bar_image_1 = progress_bar_image_1.resize((270, 20))
progress_bar_image_2 = progress_bar_image_2.resize((270, 20))
progress_bar_image_3 = progress_bar_image_3.resize((270, 20))
progress_bar_image_4 = progress_bar_image_4.resize((270, 20))
progress_bar_image_5 = progress_bar_image_5.resize((270, 20))
progress_bar_image_6 = progress_bar_image_6.resize((270, 20))

# Create Tkinter image objects from the resized images.
menu_icon_tk = ImageTk.PhotoImage(menu_icon)
waves_bottom_tk = ImageTk.PhotoImage(waves_bottom)
title_text_icon_tk = ImageTk.PhotoImage(title_text_icon)
progress_bar_image_1_tk = ImageTk.PhotoImage(progress_bar_image_1)
progress_bar_image_2_tk = ImageTk.PhotoImage(progress_bar_image_2)
progress_bar_image_3_tk = ImageTk.PhotoImage(progress_bar_image_3)
progress_bar_image_4_tk = ImageTk.PhotoImage(progress_bar_image_4)
progress_bar_image_5_tk = ImageTk.PhotoImage(progress_bar_image_5)
progress_bar_image_6_tk = ImageTk.PhotoImage(progress_bar_image_6)

# Create labels with images.
menu_icon_label = Label(root, image=menu_icon_tk)
waves_bottom_label = Label(root, image=waves_bottom_tk)
title_text_label = Label(root, image=title_text_icon_tk)

# Create a string variable for loading message and label to display it.
loading_message = StringVar()
loading_message.set("LOADING ASSETS")
loading_message_label = Label(root, textvariable=loading_message, fg="darkgray", font=("Arial", 14))

# Create labels for progress bars.
progressbar_1_label = Label(root, image=progress_bar_image_1_tk)
progressbar_2_label = Label(root, image=progress_bar_image_2_tk)
progressbar_3_label = Label(root, image=progress_bar_image_3_tk)
progressbar_4_label = Label(root, image=progress_bar_image_4_tk)
progressbar_5_label = Label(root, image=progress_bar_image_5_tk)
progressbar_6_label = Label(root, image=progress_bar_image_6_tk)

# Function to navigate to the home page.
def goto_home_page():
    """
    Close the current window and navigate to the home page.
    """
     
    root.destroy()
    subprocess.call(["python", "home.py", recieved_username])

# Function to handle the loading bar animation and message updates.
def handle_loading_bar():
    """
    Handle the loading bar animation and update loading messages.
    """

    # Show and hide progress bars and update loading message at specific intervals.
    root.after(200, lambda: progressbar_1_label.place(x=110, y=380))
    root.after(600, lambda: progressbar_1_label.place_forget())
    root.after(600, lambda: progressbar_2_label.place(x=110, y=380))
    root.after(750, lambda: loading_message.set("CLEANING UP THINGS"))
    root.after(750, lambda: loading_message_label.place(x=140, y=330))
    root.after(900, lambda: progressbar_2_label.place_forget())
    root.after(900, lambda: progressbar_3_label.place(x=110, y=380))
    root.after(1000, lambda: progressbar_3_label.place_forget())
    root.after(1000, lambda: progressbar_4_label.place(x=110, y=380))
    root.after(1100, lambda: loading_message.set("LOADING USER DATA"))
    root.after(1300, lambda: progressbar_4_label.place_forget())
    root.after(1300, lambda: progressbar_5_label.place(x=110, y=380))
    root.after(2000, lambda: loading_message.set("FINISHING UP"))
    root.after(2000, lambda: loading_message_label.place(x=175, y=330))
    root.after(2500, lambda: progressbar_5_label.place_forget())
    root.after(2500, lambda: progressbar_6_label.place(x=110, y=380))
    root.after(2500, lambda: loading_message.set("LOADED!"))
    root.after(2500, lambda: loading_message_label.place(x=195, y=330))
    root.after(3000, goto_home_page)

# Configure the style for themed buttons.
style = ttk.Style()
style.configure("TButton", foreground="gray")
style.configure("TButton", font=("Arial", 16))

# Place labels in the window.
waves_bottom_label.place(x=-2, y=210)
menu_icon_label.place(x=191, y=40)
title_text_label.place(x=153, y=200)
loading_message_label.place(x=155, y=330)
progressbar_1_label.place(x=110, y=380)

# Start a new thread to handle the loading bar animation.
loading_bar_thread = threading.Thread(target=handle_loading_bar)
loading_bar_thread.start()

# Lower the labels to control their overlapping order.
menu_icon_label.lower(title_text_label)
waves_bottom_label.lower(menu_icon_label)

# Run the main event loop.
root.mainloop()