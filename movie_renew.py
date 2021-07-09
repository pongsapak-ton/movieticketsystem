import tkinter as tk
from tkinter import *
import tkinter.font
from tkinter.ttk import *
from select import *
def Movie_page(screen,movie_name):
    screen1 = Toplevel(screen)
    screen1.title('picture')
    screen1.resizable(0, 0)
    photo = tk.PhotoImage(file='images/'+movie_name +'.png')
    image_label = tk.Button(screen1,text='Jumanji',image = photo,command=lambda: select_seat(screen, movie_name))
    image_label.pack()
    screen1.mainloop()


