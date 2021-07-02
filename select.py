from tkinter import *
import tkinter.font
import tkinter as tk
Font_tuple = ("Comic Sans MS", 20, "bold")


def select_seat(screen):
    global Font_tuple
    screen1 = Toplevel(screen)
    screen1.title('select seat')
    screen1.geometry('480x720+980+50')
    screen1.resizable(0, 0)


    label = Label(screen1, bg='black', fg='white', text="Screen this side", width= 30 ,height = 2)
    label.config(font= Font_tuple)
    label.place(x=0 ,y= 0)
    seat_1 = tk.Button(screen1,text='A1',width = 10 ,height = 2,bg = 'yellow')
    seat_1.place(x = 10 ,y = 100)

    seat_2 = tk.Button(screen1,text = 'A2',width = 10, height = 2,bg='yellow')
    seat_2.place(x= 140, y = 100)
    seat_3 = tk.Button(screen1,text = 'A3',width = 10, height = 2 ,bg= 'yellow')
    seat_3.place(x= 270 , y = 100)
    seat_4 = tk.Button(screen1, text='B1', width=10, height=2, bg='yellow')
    seat_4.place(x=10, y=160)
    seat_5 = tk.Button(screen1, text='B2', width=10, height=2, bg='yellow')
    seat_5.place(x=140, y=160)
    seat_6 = tk.Button(screen1, text='B3', width=10, height=2, bg='yellow')
    seat_6.place(x=270, y=160)
    seat_7 = tk.Button(screen1, text='C1', width=10, height=2, bg='yellow')
    seat_7.place(x=10, y=220)
    seat_8 = tk.Button(screen1, text='C2', width=10, height=2, bg='yellow')
    seat_8.place(x=140, y=220)
    seat_9 = tk.Button(screen1, text='C3', width=10, height=2, bg='yellow')
    seat_9.place(x=270, y=220)
    seat_10 = tk.Button(screen1,text= 'A4' , width=10, height=2, bg='yellow')
    seat_10.place(x = 390 , y=100)
    seat_11 = tk.Button(screen1,text= 'B4', width=10, height=2, bg='yellow')
    seat_11.place(x= 390 ,y = 160)
    seat_12 = tk.Button(screen1,text = 'C4', width=10, height=2, bg='yellow')
    seat_12.place(x = 390 ,y = 220)
    seat_13 = tk.Button(screen1, text = 'D1', width = 29, height = 2 , bg = 'red')
    seat_13.place(x=10 , y= 290 )
    seat_14 = tk.Button(screen1, text='D2', width=27, height=2, bg='red')
    seat_14.place(x=270 , y=290)
    screen1.mainloop()
