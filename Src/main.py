import tkinter as tk
from tkinter import filedialog, font
import yt_dlp as youtube_dl

root = tk.Tk()
root.title("Youtube Downloader")
root.iconbitmap('188987.ico')

def status_disp(message):
    status_window = tk.Toplevel(root)
    status_window.title("Download Status")

    status_label = tk.Label(status_window,text=message)
    status_label.pack(pady=20)

    close_button = tk.Button(status_window,text="close",command=status_window.destroy)
    close_button.pack(pady=10)

def download():
    vid_url = entry.get()
    folder_path = filedialog.askdirectory()
    ydl_opts = {
        'format': 'best',  # Download the best quality available
        'outtmpl': f'{folder_path}/%(title)s.%(ext)s',  # Save as title in the specified folder
        'noplaylist': True,  # Download only a single video
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video from {vid_url}...")
            ydl.download([vid_url])
    except:
        status_disp("Download Failed")
    status_disp("Download Successful")
    entry.delete(0, tk.END)

custom_font = font.Font(family="Helvetica", size=12, weight="bold")
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label = tk.Label(frame, text="Enter your URL:", font=custom_font)
label.pack(side=tk.LEFT, padx=(0, 10))

entry = tk.Entry(frame, width=40, font=custom_font, borderwidth=2, relief="solid")
entry.pack(side=tk.LEFT) 

button = tk.Button(root, text="Submit", command=download,font=custom_font, bg="#4CAF50", fg="white", padx=20, pady=10, relief="raised")
button.pack(pady=(10, 20), padx=20)


root.mainloop()
