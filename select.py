import tkinter as tk
from tkinter import *
import tkinter.font
from bill import *
Font_tuple = ("Comic Sans MS", 20, "bold")
Font1 = font=("Comic Sans MS", 15, "bold")

button_identities = []

def select_seat(screen, movie_name):
    button_identities = []
    global Font_tuple
    global Font1

    screen1 = Toplevel(screen)
    screen1.title('select seat')
    screen1.geometry('500x750+980+50')
    screen1.resizable(0, 0)
    frame = Frame(screen1)
    frame.pack(side = TOP)
    seatframe = Frame(screen1,bg='#AB432D')
    seatframe.pack(side = TOP,padx= 10 ,pady=10)
    entryframe = Frame(screen1, bg='blue')
    entryframe.pack(side = TOP,padx= 10 ,pady =10)
    textframe = Frame(screen1)
    textframe.pack(side = TOP,padx = 20 )
    label = Label(frame, bg='black', fg='white', text="Screen this side", width= 30 ,height = 2)
    label.config(font= Font_tuple)
    label.pack(side = BOTTOM)


    seat_1 = tk.Button(seatframe,text='A1',width = 10 ,height = 2,bg = 'yellow',command = lambda : onClickseat(seat_1))
    seat_1.grid(column=0,row= 0 ,padx= 5 ,pady =5)
    button_identities.append(seat_1)

    seat_2 = tk.Button(seatframe,text = 'A2',width = 10, height = 2,bg='yellow',command = lambda : onClickseat(seat_2))
    seat_2.grid(column=1 ,row=0 ,padx= 5 ,pady =5)
    button_identities.append(seat_2)

    seat_3 = tk.Button(seatframe,text = 'A3',width = 10, height = 2 ,bg= 'yellow',command = lambda : onClickseat(seat_3))
    seat_3.grid(row=0 ,column=2 ,padx= 5 ,pady =5)
    button_identities.append(seat_3)

    seat_4 = tk.Button(seatframe, text='B1', width=10, height=2, bg='yellow',command = lambda : onClickseat(seat_4))
    seat_4.grid(row=1 ,column=0 ,padx= 5 ,pady =5)
    button_identities.append(seat_4)

    seat_5 = tk.Button(seatframe, text='B2', width=10, height=2, bg='yellow',command = lambda : onClickseat(seat_5))
    seat_5.grid(row=1 ,column=1 ,padx= 5 ,pady =5)
    button_identities.append(seat_5)

    seat_6 = tk.Button(seatframe, text='B3', width=10, height=2, bg='yellow',command = lambda : onClickseat(seat_6))
    seat_6.grid(row=1 ,column=2 ,padx= 5 ,pady =5)
    button_identities.append(seat_6)

    seat_7 = tk.Button(seatframe, text='C1', width=10, height=2, bg='yellow',command = lambda : onClickseat(seat_7))
    seat_7.grid(row=2 ,column=0  ,padx= 5 ,pady =5)
    button_identities.append(seat_7)

    seat_8 = tk.Button(seatframe, text='C2', width=10, height=2, bg='yellow',command = lambda : onClickseat(seat_8))
    seat_8.grid(row=2 ,column= 1,padx= 5 ,pady =5)
    button_identities.append(seat_8)

    seat_9 = tk.Button(seatframe, text='C3', width=10, height=2, bg='yellow',command = lambda : onClickseat(seat_9))
    seat_9.grid(row=2 ,column=2 ,padx= 5 ,pady =5)
    button_identities.append(seat_9)

    seat_10 = tk.Button(seatframe,text= 'A4' , width=10, height=2, bg='yellow',command = lambda : onClickseat(seat_10))
    seat_10.grid(row=0 ,column=3 ,padx= 5 ,pady =5)
    button_identities.append(seat_10)

    seat_11 = tk.Button(seatframe,text= 'B4', width=10, height=2, bg='yellow',command = lambda : onClickseat(seat_11))
    seat_11.grid(row=1 ,column= 3,padx= 5 ,pady =5)
    button_identities.append(seat_11)

    seat_12 = tk.Button(seatframe,text = 'C4', width=10, height=2, bg='yellow',command = lambda : onClickseat(seat_12))
    seat_12.grid(row=2 ,column=3 ,padx= 5 ,pady =5)
    button_identities.append(seat_12)

    seat_13 = tk.Button(seatframe, text = 'D1', width = 25, height = 2 , bg = 'red',command = lambda : onClickseat(seat_13))
    seat_13.grid(row=3 ,column=0 ,columnspan=2  ,padx= 5 ,pady =5)
    button_identities.append(seat_13)

    seat_14 = tk.Button(seatframe, text='D2', width=25, height=2, bg='red',command = lambda : onClickseat(seat_14))
    seat_14.grid(column = 2 ,row =3,columnspan=2 ,padx= 5 ,pady =5)
    button_identities.append(seat_14)

    confirm = tk.Button(seatframe, text = 'confirm' ,width = 10,height =2 ,command = lambda :onClickcomfirm(button_identities))
    confirm.grid(row = 4 ,column = 1,columnspan=2)
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

    T = Text(textframe, height=8, width=52)
    T.pack(side = TOP,padx= 5 ,pady = 5)

    show_re = tk.Button(textframe,text='PrintTicket',command = lambda :pr_ticket(screen,Lastname,Firstname,phone,movie_name,button_identities,id),font=Font_tuple,width = 20,height = 3)
    show_re.pack(pady = 20)
    return T

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


def onClickseat(Button):
    try:
        Button.configure(state=tk.DISABLED)
    except:
        Button.configure(state="disabled")

def get_select(row):
    selected = []
    for botton in row :
        if (botton['state'] == 'disabled'):
            print(botton, 'selected')
            seatNum = botton.cget('text')
            selected.append(seatNum)
    return selected

def onClickcomfirm(allseat):
    selectedseat = get_select(allseat)
    gold = []
    silver = []
    sofar = []
    for Seat in selectedseat :
        if(Seat[0] in ['A', 'B']):
            print('Seat[0]:', Seat[0])
            print('gold:', Seat)
            gold.append(Seat)
        elif (Seat[0] in ['C']):
            print('Seat[0]:', Seat[0])
            print('silver :', Seat)
            silver.append(Seat)
        elif (Seat[0] in ['D']):
            print('Seat[0]',Seat[0])
            print('sofar :',Seat)
            sofar.append(Seat)
    return selectedseat


def pr_ticket(screen,Lastname,Firstname,phone,movie_name,allseat,id):

    screen1 = Toplevel(screen)
    screen1.title('select seat')
    screen1.geometry('500x750+980+50')
    screen1.resizable(0, 0)
    id = range(1, 101)
    sum  = 0
    a = 0
    selectedseat = get_select(allseat)

    ticket_fr = Frame(screen1)
    ticket_fr.pack(side = TOP)
    message_fr = Frame(screen1)
    message_fr.pack(side = TOP)
    ticket = tk.Label(ticket_fr,text='MOVIE TICKET',width = 10 ,height = 2)
    ticket.pack()
    book_id = tk.Label(message_fr, text='Booking ID :',font = Font1)
    book_id2 = tk.Label(message_fr, text=id[a], font=Font1)
    name = tk.Label(message_fr, text="Firstname :",font = Font1)
    first = tk.Label(message_fr,text='Lastname :',font = Font1)
    namel = tk.Label(message_fr,textvariable = Firstname,font = Font1)
    namef = tk.Label(message_fr,textvariable = Lastname,font = Font1)
    number = tk.Label(message_fr, text='Number :',font = Font1)
    numbers = tk.Label(message_fr, textvariable=number,font = Font1)
    movie = tk.Label(message_fr,text = 'Movie :',font = Font1)
    movie_n = tk.Label(message_fr,text  = movie_name ,font = Font1)
    seat = tk.Label(message_fr, text='Seat Number :',font = Font1)
    seats = tk.Label(message_fr, text=selectedseat,font = Font1)
    book_id.grid(row = 0,column = 0)
    book_id2.grid(row=0,column =1)
    name.grid(row = 1 ,column = 0)
    namel.grid(row = 1 ,column =1)
    first.grid(row =2 ,column = 0)
    namef.grid(row =2 ,column =1 )
    number.grid(row =3 ,column =0)
    numbers.grid(row = 3 ,column = 1)
    movie.grid(row = 4 ,column = 0)
    movie_n.grid(row =4 ,column = 1)
    seat.grid(row = 5 ,column =0)
    seats.grid(row = 5,column= 1)
    while a < len(id):
            sum = sum +id[a]
            a = a+1


