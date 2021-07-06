from tkinter import *
import tkinter.font
import tkinter as tk
Font_tuple = ("Comic Sans MS", 20, "bold")
Font1 = font=("Comic Sans MS", 15, "bold")

def select_seat(screen):
    global Font_tuple
    global Font1
    screen1 = Toplevel(screen)
    screen1.title('select seat')
    screen1.geometry('500x750+980+50')
    screen1.resizable(0, 0)
    frame = Frame(screen1)
    frame.pack(side = TOP)
    seatframe = Frame(screen1,bg='#AB432D')
    seatframe.pack(side = TOP,padx= 10 ,pady=20)
    entryframe = Frame(screen1, bg='blue')
    entryframe.pack(side = TOP,padx= 10 ,pady =10)
    label = Label(frame, bg='black', fg='white', text="Screen this side", width= 30 ,height = 2)
    label.config(font= Font_tuple)
    label.pack(side = BOTTOM)



    seat_1 = tk.Button(seatframe,text='A1',width = 10 ,height = 2,bg = 'yellow')
    seat_1.grid(column=0,row= 0 ,padx= 5 ,pady =5)
    seat_2 = tk.Button(seatframe,text = 'A2',width = 10, height = 2,bg='yellow')
    seat_2.grid(column=1 ,row=0 ,padx= 5 ,pady =5)
    seat_3 = tk.Button(seatframe,text = 'A3',width = 10, height = 2 ,bg= 'yellow')
    seat_3.grid(row=0 ,column=2 ,padx= 5 ,pady =5)
    seat_4 = tk.Button(seatframe, text='B1', width=10, height=2, bg='yellow')
    seat_4.grid(row=1 ,column=0 ,padx= 5 ,pady =5)
    seat_5 = tk.Button(seatframe, text='B2', width=10, height=2, bg='yellow')
    seat_5.grid(row=1 ,column=1 ,padx= 5 ,pady =5)
    seat_6 = tk.Button(seatframe, text='B3', width=10, height=2, bg='yellow')
    seat_6.grid(row=1 ,column=2 ,padx= 5 ,pady =5)
    seat_7 = tk.Button(seatframe, text='C1', width=10, height=2, bg='yellow')
    seat_7.grid(row=2 ,column=0  ,padx= 5 ,pady =5)
    seat_8 = tk.Button(seatframe, text='C2', width=10, height=2, bg='yellow')
    seat_8.grid(row=2 ,column= 1,padx= 5 ,pady =5)
    seat_9 = tk.Button(seatframe, text='C3', width=10, height=2, bg='yellow')
    seat_9.grid(row=2 ,column=2 ,padx= 5 ,pady =5)
    seat_10 = tk.Button(seatframe,text= 'A4' , width=10, height=2, bg='yellow')
    seat_10.grid(row=0 ,column=3 ,padx= 5 ,pady =5)
    seat_11 = tk.Button(seatframe,text= 'B4', width=10, height=2, bg='yellow')
    seat_11.grid(row=1 ,column= 3,padx= 5 ,pady =5)
    seat_12 = tk.Button(seatframe,text = 'C4', width=10, height=2, bg='yellow')
    seat_12.grid(row=2 ,column=3 ,padx= 5 ,pady =5)
    seat_13 = tk.Button(seatframe, text = 'D1', width = 25, height = 2 , bg = 'red')
    seat_13.grid(row=3 ,column=0 ,columnspan=2  ,padx= 5 ,pady =5)
    seat_14 = tk.Button(seatframe, text='D2', width=25, height=2, bg='red')
    seat_14.grid(column = 2 ,row =3,columnspan=2 ,padx= 5 ,pady =5)

    Lastname = StringVar()
    Firstname = StringVar()
    phone = StringVar()

    fname = Label(entryframe, text="FirstName ",font = Font1).grid(column = 0 ,row = 1,padx= 5 ,pady =5)
    Firsrtname_entry = Entry(entryframe,textvariable=Firstname,width = 20,borderwidth="4")
    Firsrtname_entry.grid(column = 3 ,row = 1,padx= 5 ,pady =5)
    Firsrtname_entry.config(borderwidth="2",relief=GROOVE,font= ("Comic Sans MS", 15, "bold"))
    lname = Label(entryframe, text='LastName',font = Font1).grid(column = 0,row = 2,padx= 5 ,pady =5)
    Lastname_entry = Entry(entryframe,textvariable = Lastname,width = 20 ,borderwidth='4')
    Lastname_entry.grid(column=3, row=2,padx= 5 ,pady =5)
    Lastname_entry.config(borderwidth="2", relief=GROOVE, font=("Comic Sans MS", 15, "bold"))
    phone_label= Label(entryframe,text="Phone",font = Font1).grid(column = 0,row= 3,padx= 5 ,pady =5)
    phone_entry = Entry(entryframe,textvariable = phone,width = 20, borderwidth='4')
    phone_entry.grid(column=3, row=3,padx= 5 ,pady =5)
    phone_entry.config(borderwidth="2", relief=GROOVE, font=("Comic Sans MS", 15, "bold"))


    screen1.mainloop()