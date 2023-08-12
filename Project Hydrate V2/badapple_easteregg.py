"""
Easter egg video page part of Project: Hydrate.

Description:
 - Completely and utterly just an easter egg, made for fun. All this does is just play a video if the user logs in with the username badapple and the password easteregg
 - This part serves no real purpose on the program but is just completely made for fun.
"""

import subprocess
from tkinter import *

from tkinter import ttk
import tkinter as tk

from pytube import YouTube
import vlc

video_url = "https://www.youtube.com/watch?v=UkgK8eUdpAo"

youtube = YouTube(video_url)
root = Tk()

root.title("Project Hydrate: Bad Apple (Easter Egg)")
root.geometry("640x480")

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
root.iconbitmap(default="assets\icon.ico")

video_file_path = "assets\\badapple.mp4"

canvas = tk.Canvas(root, width=640, height=480)
canvas.pack()

vlc_instance = vlc.Instance()
player = vlc_instance.media_player_new()
media = vlc_instance.media_new(video_file_path)
player.set_media(media)
player.set_hwnd(canvas.winfo_id())
player.play()

def stop_video():
    """
    Stop the video playback and close the window.
    """
    
    player.stop()
    root.destroy()
    subprocess.call(["python", "main.py"])

stop_button = ttk.Button(root, text="Stop", command=stop_video)
stop_button.pack()

root.mainloop()