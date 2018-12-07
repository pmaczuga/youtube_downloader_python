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

        self.download_frame = tk.Frame(self, bg='white', bd=10, height=15)
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

        self.mp4_button = tk.Button(button_frame, text='MP4', width=10, height=2, command=self.handle_mp4_button)
        self.mp4_button.pack(side='left', padx=5)

        self.mp3_button = tk.Button(button_frame, text='MP3', width=10, height=2, command=self.handle_mp3_button)
        self.mp3_button.pack(side='left', padx=5)

    def init_download(self):
        title, status, progress_bar = self.add_download()
        title.set('...')
        status.set('DOWNLOADING...')
        url = self.url_entry.get()
        return url, title, status, progress_bar

    def handle_mp4_button(self):
        url, title, status, progress_bar = self.init_download()
        Thread(
            target=ytd.download_mp4,
            args=(url,
            self.change_label_wrapper(title),
            self.update_progress_bar_wrapper(progress_bar),
            self.change_label_wrapper(status, 'COMPLETE!'),
            self.change_label_wrapper(status, 'ERROR!'),
            )).start()

    def handle_mp3_button(self):
        url, title, status, progress_bar = self.init_download()
        Thread(
            target=ytd.download_mp3,
            args=(url,
            self.change_label_wrapper(title),
            self.update_progress_bar_wrapper(progress_bar),
            self.change_label_wrapper(status, 'CONVERTING...'),
            self.change_label_wrapper(status, 'COMPLETE!'),
            self.change_label_wrapper(status, 'ERROR!'),
            )).start()

    def update_progress_bar_wrapper(self,progress_bar):
        def cb(value, maximum):
            progress_bar['maximum'] = maximum
            progress_bar['value'] = value
            self.download_frame.update_idletasks()
        return cb

    def change_label_wrapper(self, textvar, value=None):
        def cb(sth=None):
            if value:
                textvar.set(value)
            else:
                textvar.set(sth)
        return cb

    def fill_download_frame(self):
        self.download_list = []
        pass

    def add_download(self):
        frame = tk.Frame(self.download_frame)
        frame.pack()

        title_var = tk.StringVar()
        status_var = tk.StringVar()

        title = tk.Label(frame, padx=3, pady=5, width=30, anchor='w', textvariable=title_var)
        title.pack(side='left')

        progress_bar = ttk.Progressbar(frame)
        progress_bar.pack(side='left', padx=3, pady=5)

        status = tk.Label(frame, width=15, padx=3, pady=5, textvariable=status_var)
        status.pack(side='left')

        self.download_list.append((title, status, progress_bar))

        return title_var, status_var, progress_bar


def main():
    root = tk.Tk()
    root.resizable(False, False)
    app = Application(master=root)
    app.mainloop()

if __name__ == '__main__':
    main()