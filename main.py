import tkinter as tk
from tkinter import *
import tkinter.font
Font_tuple = ("Comic Sans MS", 20, "bold")
def exit_program():
   exit()

def admin(screen):
    screen2 = Toplevel(screen)
    screen2.title('admin')

def movie(screen):
    global Font_tuple

    screen1 = Toplevel(screen)
    screen1.title('select movie')
    screen1.geometry('410x480+540+200')
    screen1.resizable(0,0)

    label = tk.Label(screen1, text='movieTicketBookingSystem', bg='blue', fg='white', width=25, height=2)
    label.place(x=0, y=0)
    label.config(font=Font_tuple)

    buttton_1 = tk.Button(screen1, text= 'JUMANJI',bg = 'red',width=15 ,height = 1)
    buttton_1.place(x=80 , y = 110)
    buttton_1.config(font = Font_tuple)

    buttton_2 = tk.Button(screen1,text='Ready Player One', bg='red', width=15, height=1)
    buttton_2.place(x=80, y=210)
    buttton_2.config(font=Font_tuple)

    buttton_3 = tk.Button(screen1, text='FREE GUY', bg='red', width=15, height=1)
    buttton_3.place(x=80, y=310)
    buttton_3.config(font=Font_tuple)
    screen1.mainloop()


def main_p():
    global screen
    global Font_tuple
    screen = tk.Tk()
    screen.title('movie ticket')
    screen.geometry('410x480+90+200')
    screen.resizable(0,0)

    label = tk.Label(screen, text = 'movieTicketBookingSystem',bg = 'blue', fg = 'white',width = 25, height = 2)
    label.place(x = 0 , y= 0)
    label.config(font = Font_tuple)
    button_admin = tk.Button(screen, text = 'admin',command = lambda:admin(screen),bg='red',width = 15 ,height = 1 )
    button_admin.config(font = Font_tuple)
    button_admin.place(x=60, y =110)

    button_1 = tk.Button(screen, text='purchase ticket',command = lambda:movie(screen),bg= 'red',width = 15 ,height = 1)
    button_1.place(x=60, y =200)
    button_1.config(font = Font_tuple)

    button_exit = tk.Button(screen, text='exit',command = lambda:exit_program(),bg= 'black',fg= 'white',width= 5 ,height = 2)
    button_exit.place(x= 310 , y = 370)
    button_exit.config(font = Font_tuple)

    button_cancel = tk.Button(screen, text = 'cancel booking',bg = 'red' ,fg = 'white', width = 15 , height = 1)
    button_cancel.place(x = 60 , y = 290)
    button_cancel.config(font = Font_tuple)

    print(screen.winfo_screenwidth())
    print(screen.winfo_screenheight())

    screen.mainloop()



main_p()