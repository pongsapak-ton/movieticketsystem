from tkinter import *
import tkinter as tk
m = Tk()
m.option_add("*font", "consolas 30")

def guide(m):
    photo = tk.PhotoImage(file='Avatar.png')
    image_label = tk.Label(m,text='Avatar',image = photo)
    image_label.pack()

m.mainloop()

def Jumanji1(n):
    photo = tk.PhotoImage(file='jumanji1.png')
    image_label = tk.Label(m,text='Jumanji',image = photo)
    image_label.pack()

m.mainloop()

def ReadyPlayerOne(m):
    photo = tk.PhotoImage(file='Ready Player One.png')
    image_label = tk.Label(m,text='Ready Player One',image = photo)
    image_label.pack()

m.mainloop()

def FreeGuy(m):
    photo = tk.PhotoImage(file='Free Guy.png')
    image_label = tk.Label(m,text='FreeGuy',image = photo)
    image_label.pack()

m.mainloop()