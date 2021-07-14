import tkinter as tk
from tkinter import *
import tkinter.font
from tkcalendar import *
from select import *
from time import sleep

Font_tuple = ("Comic Sans MS", 20, "bold")
Font1 = font=("Comic Sans MS", 15, "bold")

def Close(screen1,screen,n, movie_name, Lastname, Firstname, phone):

    sleep(1)
    screen.destroy()
    select_seat(str(n.get()), screen, movie_name, Lastname, Firstname, phone)


def entry_func(screen,movie_name):

    screen1 = Toplevel(screen)
    screen1.title('select movie')
    screen1.geometry('450x480')
    screen1.resizable(0, 0)
    entryframe = Frame(screen1, bg='blue')
    entryframe.pack(side=TOP, padx=10, pady=10)
    textframe = Frame(screen1)
    textframe.pack(side=TOP, padx=20)

    global Lastname
    global Firstname
    global phone
    global Firstname_entry
    global Lastname_entry
    Lastname = StringVar()
    Firstname = StringVar()
    phone = StringVar()

    fname = Label(entryframe, text="FirstName ",font = Font1).grid(column = 0 ,row = 1,padx= 5 ,pady =5)
    Firstname_entry = Entry(entryframe,textvariable=Firstname,width = 20,borderwidth="4")
    Firstname_entry.grid(column = 3 ,row = 1,padx= 5 ,pady =5)
    Firstname_entry.config(borderwidth="2",relief=GROOVE,font= ("Comic Sans MS", 15, "bold"))

    lname = Label(entryframe, text='LastName',font = Font1).grid(column = 0,row = 2,padx= 5 ,pady =5)
    Lastname_entry = Entry(entryframe,textvariable = Lastname,width = 20 ,borderwidth='4')
    Lastname_entry.grid(column=3, row=2,padx= 5 ,pady =5)
    Lastname_entry.config(borderwidth="2", relief=GROOVE, font=("Comic Sans MS", 15, "bold"))

    phone_label= Label(entryframe,text="Phone",font = Font1).grid(column = 0,row= 3,padx= 5 ,pady =5)
    phone_entry = Entry(entryframe,textvariable = phone,width = 20, borderwidth='4')
    phone_entry.grid(column=3, row=3,padx= 5 ,pady =5)
    phone_entry.config(borderwidth="2", relief=GROOVE, font=("Comic Sans MS", 15, "bold"))

    ok = tk.Button(entryframe,text='ok',width = 4 ,height = 1,command = lambda :chk_fname(T))
    ok.grid(column= 4 ,row = 1)
    ok_1 = tk.Button(entryframe,text='ok',width = 4,height= 1,command = lambda :chk_lname(T))
    ok_1.grid(column = 4 ,row=2)
    ok_2 = tk.Button(entryframe, text='ok', width=4, height=1,command = lambda : chk_num(T))
    ok_2.grid(column=4, row=3)
    get_datetime(screen,screen1,textframe,movie_name)
    T = Text(textframe, height=5, width=52)
    T.pack(side=TOP, padx=5, pady=5)
    return textframe,T,Lastname,Firstname,phone,entryframe,screen1


def get_date(cal):
    date = cal.get_date()
    print(date)
    return date

def get_datetime(screen1,screen, textframe, movie_name):
    cal = DateEntry(textframe, dateformat=3, width=12, background='darkblue',
                    foreground='white', borderwidth=4, Calendar=2021)
    cal.pack(side =TOP,pady=10)
    dates = cal.get_date()
    Button(textframe, text="Confirm Date", command=lambda: get_date(cal)).pack(side = TOP,pady=10)

    n = StringVar(textframe, "1")

    values = {"10:00 - 11:20": "10:00",
              "11:40 - 13:00": "11:40",
              "13:20 - 14:40": "13:20"}

    # Loop is used to create multiple Radiobuttons
    # rather than creating each button separately
    for (text, value) in values.items():
        Radiobutton(textframe, text=text, variable=n, value=value, indicator=1,
                    background="light blue").pack(side=TOP, fill='x', ipady=2, pady=5)
    cfmtime = Button(textframe, text='Confirm Time', command=lambda:  select_seat(str(n.get()), screen, movie_name, Lastname, Firstname, phone)  )
    cfmtime.pack(side = TOP)



    return cal,n

def chk_fname(T):
    global Firstname
    global Firstname_entry
    first_n = Firstname.get()
    a = first_n.isdigit()
    if len(first_n) != 0 and a != True:
        T.insert(INSERT, 'firstname has been inputed''\n')
        print(first_n)
    else:
        T.insert(INSERT, "invalid input please input a valid name""\n")


def chk_lname(T):
    global Lastname
    last_n = Lastname.get()
    a = last_n.isdigit()
    if len(last_n) !=0 and a != True:
        T.insert(INSERT, 'Lastname has been inputed''\n')

    else:
        T.insert(INSERT, "invalid input please input a valid name""\n")


def chk_num(T):
    global phone
    Phone_num = phone.get()
    if Phone_num.isdigit() == True and len(Phone_num) != 0 and len(Phone_num) == 10:
        T.insert(INSERT, "mobile number has been inputed""\n")
    else:
        T.insert(INSERT, "invalid input please input a valid mobile number""\n")



