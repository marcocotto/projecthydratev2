"""
Leaderboard page part of Project: Hydrate.

Description:
 - Reads the leaderboard_data file and creates a table to sort all usernames in descending order
"""

# Imports
import subprocess
import sys

from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk

root = Tk()
root.geometry("495x595")

# Create the username variable.
logged_in_username = ""

# Check if a username is provided.
if len(sys.argv) > 1:
    logged_in_username = sys.argv[1]

if logged_in_username == "":
    logged_in_username = "Guest"

root.iconbitmap(default="assets\icon.ico")
user_data_file = "db\\user_data.txt"

root.resizable(width=False, height=False)
root.title("Project Hydrate: Hydration Leaderboard")

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


center_window(root)

# Function to navigate back to the home window.
def goto_home_window():
    """
    Close the current window and open the home window.
    """

    root.destroy()
    subprocess.call(["python", "home.py", logged_in_username])

# Creating the back button and its functionality.
back_button_image = Image.open("assets\\backbutton.png")
back_button_image = back_button_image.resize((30, 30), resample=Image.BICUBIC)

back_button_image_tk = ImageTk.PhotoImage(back_button_image)
back_button = ttk.Button(root, image=back_button_image_tk, compound="center", width=0, command=goto_home_window)
back_button.place(x=20, y=20)

background_waves = Image.open("assets\leaderboardwaves.png")
background_waves_tk = ImageTk.PhotoImage(background_waves)

waves_bottom_label = Label(root, image=background_waves_tk)
waves_bottom_label.place(x=-2, y=0)

# Function to create the leaderboard table.
def create_table(parent_frame):
    """
    Create a leaderboard table within the specified parent frame.
    """

    # Create a frame for the table.
    table_frame = ttk.Frame(parent_frame)
    table_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Create a style for the scrollbar to make it appear disabled.
    style = ttk.Style()
    style.configure("Disabled.Vertical.TScrollbar", troughcolor="disabled")

    # Create a frame for the labels.
    labels_frame = ttk.Frame(table_frame)
    labels_frame.pack(side="top", fill="x")

    # Create the name and rank labels.
    rank_label = ttk.Label(labels_frame, text="Rank", width=5, anchor="center")
    rank_label.pack(side="left", padx=(0, 15))
    name_label = ttk.Label(labels_frame, text="Name", width=15, anchor="w")
    name_label.pack(side="left")
    score_label = ttk.Label(labels_frame, text="Hydration Score", width=15, anchor="e")
    score_label.pack(side="right")

    # Create a scrollbar.
    scrollbar = ttk.Scrollbar(table_frame, orient="vertical", style="Disabled.Vertical.TScrollbar")
    scrollbar.pack(side="right", fill="y")

    # Create a treeview widget (table).
    table = ttk.Treeview(table_frame, yscrollcommand=scrollbar.set)
    table.pack(fill="both")

    # Configure the scrollbar.
    scrollbar.configure(command=table.yview)

    # Disable selection and clickability of the table and scrollbar.
    table.configure(selectmode="none", show="tree")
    table.bind("<Button-1>", lambda e: "break")

    # Define the table columns.
    table["columns"] = ("Rank", "Name", "Score")

    # Format the table columns.
    table.column("#0", width=0, stretch="no")  # Hidden column.
    table.column("Rank", width=50, anchor="center")
    table.column("Name", width=150, anchor="w")
    table.column("Score", width=100, anchor="e")

    # Create table headers.
    table.heading("#0", text="", anchor="w")
    table.heading("Rank", text="Rank", anchor="center")
    table.heading("Name", text="Name", anchor="w")
    table.heading("Score", text="Score", anchor="e")

    # Read the leaderboard data from the text file.
    leaderboard_data = []
    with open("db\\leaderboard_data.txt", "r") as file:
        for line in file:
            line = line.strip()
            if (line):
                username, score = line.split("=")
                leaderboard_data.append((username, int(score)))

    # Sort the leaderboard data in descending order based on the score.
    leaderboard_data.sort(key=lambda x: x[1], reverse=True)

    # Limit the number of rows to 25 or the available data.
    leaderboard_data = leaderboard_data[:25]

    # Add table rows.
    for index, (username, score) in enumerate(leaderboard_data, start=1):
        if (index == 1):
            tag = "gold"
        elif (index == 2):
            tag = "silver"
        elif (index == 3):
            tag = "orange"
        else:
            tag = "white"
        table.insert("", "end", text="", values=(index, username, score), tags=tag)

    # Define the row tags and configure their colors.
    table.tag_configure("gold", background="gold", font=("Simplifica", 15, "bold"))
    table.tag_configure("silver", background="silver", font=("Simplifica", 15, "bold"))
    table.tag_configure("orange", background="orange", font=("Simplifica", 15, "bold"))
    table.tag_configure("white", background="white", font=("Simplifica", 15, "bold"))

    return table_frame


# Create a frame for the leaderboard table.
table_frame = create_table(root)
waves_bottom_label.lower(back_button)

root.mainloop()  # Start the main event loop.