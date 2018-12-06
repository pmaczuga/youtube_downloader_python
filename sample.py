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
        master.title("ABC")
        self.master = master
        self.pack(fill=tk.BOTH, expand=1)
        self.create_widgets()

    def create_widgets(self):
        title_frame = tk.Frame(self, bg='green', bd=5)
        title_frame.grid(row=0, column=0, columnspan=2, sticky=tk.E+tk.E)

        control_frame = tk.Frame(self, bg='yellow', bd=5)
        control_frame.grid(row=1, column=0, sticky=tk.N+tk.W+tk.E+tk.S)

        list_frame = tk.Frame(self, bg='red', bd=5)
        list_frame.grid(row=1, column=1, sticky=tk.N+tk.W+tk.E+tk.S)

        title_label = tk.Label(title_frame, text='TITLE').pack()
        
        control_button1 = tk.Button(control_frame, text='BUTTON1').pack(fill=tk.X)
        control_button2 = tk.Button(control_frame, text='BUTTON2').pack(fill=tk.X)
        control_button3 = tk.Button(control_frame, text='BUTTON3').pack(fill=tk.X)

        list_label1 = tk.Label(list_frame, text='Label1').grid(row=0, column=0)
        list_label2 = tk.Label(list_frame, text='Label2').grid(row=1, column=0)
        list_label3 = tk.Label(list_frame, text='Label3').grid(row=2, column=0)
        list_label4 = tk.Label(list_frame, text='Label4').grid(row=3, column=0)
        list_button1 = tk.Button(list_frame, text='L_BUTTON1').grid(row=0, column=1)
        list_button2 = tk.Button(list_frame, text='L_BUTTON2').grid(row=1, column=1)
        list_button3 = tk.Button(list_frame, text='L_BUTTON3').grid(row=2, column=1)
        list_button4 = tk.Button(list_frame, text='L_BUTTON4').grid(row=3, column=1)


def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == '__main__':
    main()