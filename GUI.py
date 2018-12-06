import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pytube as pt
import pydub
from pydub import AudioSegment
import os
import yt_downloader as ytd
from threading import Thread

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.title("YouTube Downloader")
        self.master = master
        self.pack()
        self.create_frames()

    def create_frames(self):
        self.title_frame = tk.Frame(self, bd=10)
        self.title_frame.pack()
        self.fill_title_frame()

        self.control_frame = tk.Frame(self, bd=10)
        self.control_frame.pack()
        self.fill_control_frame()

        self.download_frame = tk.Frame(self, bg='white', bd=10, height=200)
        self.download_frame.pack(pady=10, padx=100, fill='x', expand=True)
        self.fill_download_frame()

    def fill_title_frame(self):
        self.title_label = tk.Label(self.title_frame, text='YouTube Downloader', font=("Times", 15, "bold"))
        self.title_label.pack()

    def fill_control_frame(self):
        url_frame = tk.Frame(self.control_frame, bd=5)
        url_frame.pack()

        self.url_label = tk.Label(url_frame, text='URL: ')
        self.url_label.pack(side='left')

        self.url_entry = tk.Entry(url_frame, width=100)
        self.url_entry.pack(side='left')

        button_frame = tk.Frame(self.control_frame, bd=5)
        button_frame.pack()

        self.mp4_button = tk.Button(button_frame, text='MP4', width=10, height=2)
        self.mp4_button.pack(side='left', padx=5)

        self.mp3_button = tk.Button(button_frame, text='MP3', width=10, height=2)
        self.mp3_button.pack(side='left', padx=5)

    def fill_download_frame(self):
        pass

    def add_download(self, url):
        frame = tk.Frame(self.download_frame)
        frame.pack()

        title = tk.Label(frame width=)
        title.pack()




def main():
    root = tk.Tk()
    root.resizable(False, False)
    app = Application(master=root)
    app.mainloop()

if __name__ == '__main__':
    main()