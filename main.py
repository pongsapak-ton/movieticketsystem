import tkinter as tk
from tkinter import *
import tkinter.font
from tkinter.ttk import *
from select import *
from login import *
from movie_renew import *
import contextvars



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
    label_frame = Frame(screen1)
    label_frame.pack(side=TOP)
    radio_frame = Frame(screen1)
    radio_frame.pack(side = TOP,pady = 20)

    label = tk.Label(label_frame, text='movieTicketBookingSystem', bg='blue', fg='white', width=25, height=2)
    label.pack(side=TOP)
    label.config(font=Font_tuple)

    v = StringVar(radio_frame, "1")



    # Dictionary to create multiple buttons
    values = {"JUMANJI": "JUMANJI",
              "Ready Player One": "Ready Player One",
              "FREE GUY": "FREE GUY"}

    # Loop is used to create multiple Radiobuttons
    # rather than creating each button separately
    for (text, value) in values.items():

        Radiobutton(radio_frame, text=text, variable=v, value=value,font=Font_tuple, indicator = 0,
                background = "light blue").pack(side=TOP, ipady=5,fill='x',pady =10 )

    CnfrmBtn = Button(radio_frame, text="CONFIRM",font= Font_tuple,command = lambda :Movie_page(screen, str(v.get())))
    CnfrmBtn.pack(side=BOTTOM,ipady=5,pady = 10)
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
    button_admin = tk.Button(screen, text = 'admin',command = lambda:login_screen(screen),bg='red',width = 15 ,height = 1 )
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