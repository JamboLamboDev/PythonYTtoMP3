from tkinter import *
from tkinter import ttk
from pytube import YouTube
from tkinter.messagebox import showinfo, showerror, askokcancel
import threading
import os
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
title_style.configure('Title.TLabel', foreground='#000000', font=('OCR A Extended', 25))
#label
label_style = ttk.Style()
label_style.configure('TLabel', foreground='#000000', font=('OCR A Extended', 15))

# entry
entry_style = ttk.Style()
entry_style.configure('TEntry', font=('Dotum', 15))
# btn
button_style = ttk.Style()
button_style.configure('TButton', foreground='#000000', font='DotumChe')

 #Create title
mp3_label = ttk.Label(window, text='MP3 Downloader', style='Title.TLabel')
canvas.create_window(180, 125, window=mp3_label)

# creating a ttk label
url_label = ttk.Label(window, text='Enter MP3 URL:', style='TLabel')
# creating a ttk entry
url_entry = ttk.Entry(window, width=72, style='TEntry')
# adding the label to the canvas
canvas.create_window(114, 200, window=url_label)
# adding the entry to the canvas
canvas.create_window(250, 230, window=url_entry)

window.mainloop()