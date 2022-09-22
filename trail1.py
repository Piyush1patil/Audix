

import os
import pickle
import tkinter as tk
import application
from tkinter import filedialog
from tkinter import PhotoImage
from pygame import mixer
from subprocess import call
import music_player

class Player(tk.Frame()):
    def __init__(self, master=None):
	    super().__init__(master)
	    self.master = master
	    self.create_frames()

    def create_frames(self):
        self.loadSongs = tk.Button(self.controls, bg='green', fg='white', font=10)
	    self.loadSongs['text'] = 'Load Songs'
	    self.loadSongs['command'] = self.retrieve_songs
        self.loadSongs.grid(row=0, column=0, padx=10)
        
        self.loadSongs = tk.Button(self.controls, bg='red', fg='white', font=10)
	    self.loadSongs['text'] = 'Audio run'
	    self.loadSongs['command'] = self.audio
	    self.loadSongs.grid(row=3, column=0, padx=20
    def audio(self):
        exec(open("application.py").read())

root = tk.Tk()
root.geometry('600x400')
root.wm_title('Audics')
app = Player(master=root)
app.mainloop()
