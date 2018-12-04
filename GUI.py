import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pytube as pt
import pydub
from pydub import AudioSegment
import os
import yt_downloader as ytd

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.title("YouTube Downloader")
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.status_label = tk.Label(self,
            text='DONE!')
        self.status_label.pack(side='bottom')

        self.progress_bar = ttk.Progressbar(self,
            orient='horizontal',
            length='200',
            mode='determinate')
        self.progress_bar.pack(side="bottom")

        self.mp4_button = tk.Button(self, 
            text='MP4', 
            command=self.download_mp4,
            height=2,
            width=10)
        self.mp4_button.pack(side="bottom")

        self.mp3_button = tk.Button(self, 
            text='MP3', 
            command=self.download_mp3,
            height=2,
            width=10)
        self.mp3_button.pack(side="bottom")

        self.url_label = tk.Label(self, 
            text = "URL: ")
        self.url_label.pack(side="left")

        self.url_entry = tk.Entry(self,
            width=100)
        self.url_entry.pack(side="top")

    def download_mp4(self):
        try:
            self.status_label['text'] = "DOWNLOADING..."
            ytd.download_mp4(self.url_entry.get(), self.update_progress_bar_download())
        except Exception as e:
            self.status_label['text'] = "ERROR!"
            print(e)
            messagebox.showerror("Error", "Something went wrong!")
        else:
            self.status_label['text'] = "DONE!"
            messagebox.showinfo("Message", "Complete!")

    def download_mp3(self):
        try:
            self.status_label['text'] = "DOWNLOADING..."
            ytd.download_mp3(self.url_entry.get(), 
                self.update_progress_bar_download(),
                self.update_status_wrapper("CONVERTING..."),
                self.update_progress_var_convert())
        except Exception as e:
            self.status_label['text'] = "ERROR!"
            print(e)
            messagebox.showerror("Error", "Something went wrong!")
        else:
            self.status_label['text'] = "DONE!"
            messagebox.showinfo("Message", "Complete!")

    def update_status_wrapper(self, new):
        def wrapper():
            self.status_label["text"] = new
            root.update()

        return wrapper


    def update_progress_bar_download(self):
        def callback(stream, chunk, file_handle, bytes_remaining):
            self.progress_bar["maximum"] = stream.filesize
            self.progress_bar["value"] = stream.filesize - bytes_remaining
            root.update_idletasks()
        return callback

    def update_progress_var_convert(self):
        def callback(i, size):
            self.progress_bar["maximum"] = size
            self.progress_bar["value"] = i
            root.update_idletasks()
        return callback

root = tk.Tk()
app = Application(master=root)
app.mainloop()
