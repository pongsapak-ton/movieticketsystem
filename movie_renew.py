import movie
import tkinter as tk
from tkinter import *
import tkinter.font
from tkinter.ttk import *
from entry import *



def Movie_page(screen,movie_name):

    screen2 = Toplevel(screen)
    screen2.title('picture')
    screen2.resizable(0, 0)
    photo = tk.PhotoImage(file='images/'+movie_name +'.png')
    image_label = tk.Button(screen2,text='Jumanji',image = photo,command=lambda: entry_func(screen,movie_name))
    image_label.pack()
    screen2.mainloop()


