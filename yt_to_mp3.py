from tkinter import *
from tkinter import ttk
from pytubefix import YouTube
from tkinter.messagebox import showinfo, showerror, askokcancel
import threading
import os
# function to download mp3

def download_mp3():
    url = url_entry.get()
    if not url:
        showerror("Error", "Please enter a valid YouTube URL.")
        return

    try:
        video = YouTube(url, on_progress_callback=progress_function)
        output = video.streams.get_audio_only().download()
        base, ext = os.path.splitext(output)
        video_to_mp3 = base + '.mp3'
        os.rename(output, video_to_mp3)
        showinfo("Success", f"Download completed: {video_to_mp3}")
        progress_label.config(text="") # Clear progress label for next download
        progress_bar['value'] = 0
        
        

    except Exception as e:
        showerror("Error", f"An error occurred: {str(e)}")
        progress_label.config(text="")
        progress_bar['value'] = 0

def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize_approx
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    progress_bar['value'] = percentage_of_completion
    progress_label.config(text=f"Downloaded: {int(percentage_of_completion)}%")
    window.update()

def start_download_thread():
    download_thread = threading.Thread(target=download_mp3)
    download_thread.start()

# create GUI
# creates the window using Tk() function
window = Tk()
window.title('MP3 Downloader')
window.geometry('500x400+430+180')
window.configure(background="antiquewhite")
window.resizable(height=FALSE, width=FALSE) # not rezisable so that the widgets dont look weird


# canvas for widget
canvas = Canvas(window, width=500, height=400)
canvas.pack()

"""Styles for the widgets"""
#title
title_style = ttk.Style()
title_style.configure('Title.TLabel', foreground='#000000', font=('Dotum', 25))
#label
label_style = ttk.Style()
label_style.configure('TLabel', foreground='#000000', font=('Dotum', 15))

# entry
entry_style = ttk.Style()
entry_style.configure('TEntry', font=('Dotum', 15))
# btn
button_style = ttk.Style()
button_style.configure('TButton', foreground='#000000', font='DotumChe')

 #Create GUI and windows
mp3_label = ttk.Label(window, text='MP3 Downloader', style='Title.TLabel')
url_label = ttk.Label(window, text='Enter MP3 URL:', style='TLabel')
url_entry = ttk.Entry(window, width=72, style='TEntry')
download_button = ttk.Button(window, text='Download MP3', style='TButton', command=start_download_thread)
canvas.create_window(145, 45, window=mp3_label)
canvas.create_window(114, 200, window=url_label)
canvas.create_window(250, 230, window=url_entry)
canvas.create_window(125, 330, window=download_button)

#progress bar and empty label
progress_label = Label(window, text='')
canvas.create_window(240, 280, window=progress_label)
progress_bar = ttk.Progressbar(window, orient=HORIZONTAL, length=450, mode='determinate')
canvas.create_window(250, 300, window=progress_bar)

window.mainloop()
