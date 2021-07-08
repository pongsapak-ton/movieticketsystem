from tkinter import *
import tkinter.font
import tkinter as tk
Font_tuple = ("Comic Sans MS", 20, "bold")
Font1 = font=("Comic Sans MS", 15, "bold")

button_identities = []

def select_seat(screen):
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
    seatframe.pack(side = TOP,padx= 10 ,pady=30)
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



