import tkinter as tk
from tkinter import *
import tkinter.font

Font_tuple = ("Comic Sans MS", 20, "bold")
Font1 = font=("Comic Sans MS", 15, "bold")
id =100
button_identities = []
price = []

def exit_program():
   exit()

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

def onClickcomfirm(time,allseat,Lastname, Firstname, phone,movie_name,ticket_fr,message_fr):
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
    total = len(gold)*250 + len(silver)*150 + len(sofar)*350
    price.append(total)
    pr_ticket(time,Lastname,Firstname,phone,movie_name,allseat,ticket_fr,message_fr)
    print(selectedseat)
    return selectedseat,total


def select_seat(time,screen, movie_name ,Lastname, Firstname, phone):
    button_identities = []
    global Font_tuple
    global Font1

    screen2 = Toplevel(screen)
    screen2.title('select seat')
    screen2.geometry('500x750')
    screen2.resizable(0, 0)
    frame = Frame(screen2)
    frame.pack(side = TOP)
    seatframe = Frame(screen2,bg='#AB432D')
    seatframe.pack(side = TOP,padx= 10 ,pady=10)

    ticket_fr = Frame(screen2)
    ticket_fr.pack(side=TOP)
    message_fr = Frame(screen2)
    message_fr.pack(side=TOP)

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

    confirm = tk.Button(seatframe, text = 'confirm' ,width = 10,height =2 ,command = lambda :onClickcomfirm(time,button_identities,Lastname, Firstname, phone,movie_name,ticket_fr,message_fr))
    confirm.grid(row = 4 ,column = 1,columnspan=2)

    out = tk.Button(seatframe,text ='exit',width = 4 ,height = 2,command = lambda :exit()).grid(row = 4 ,column = 3)
    return button_identities ,ticket_fr,message_fr



def pr_ticket(time,Lastname,Firstname,phone,movie_name,allseat,ticket_fr,message_fr):

    global id
    sum = 0


    selectedseat = get_select(allseat)

    print(phone.get())
    ticket = tk.Label(ticket_fr,text='MOVIE TICKET',width = 10 ,height = 2)
    ticket.pack()
    book_id = tk.Label(message_fr, text='Booking ID :',font = Font1)
    book_id2 = tk.Label(message_fr, text=id, font=Font1 )
    id+=1
    name = tk.Label(message_fr, text="Firstname :",font = Font1)
    first = tk.Label(message_fr,text='Lastname :',font = Font1)
    namel = tk.Label(message_fr,textvariable = Firstname,font = Font1)
    namef = tk.Label(message_fr,textvariable = Lastname,font = Font1)
    number = tk.Label(message_fr, text='Number :',font = Font1)
    numbers = tk.Label(message_fr, textvariable=phone,font = Font1)
    movie = tk.Label(message_fr,text = 'Movie :',font = Font1)
    movie_n = tk.Label(message_fr,text  = movie_name ,font = Font1)
    seat = tk.Label(message_fr, text='Seat Number :',font = Font1)
    seats = tk.Label(message_fr, text=selectedseat,font = Font1)
    pr = tk.Label(message_fr,text = 'Price :',font= Font1)
    pr1 = tk.Label(message_fr,text = price, font= Font1)
    pr2 = tk.Label(message_fr,text ='Baht', font=Font1)

    time1 = tk.Label(message_fr,text = 'time :',font = Font1)
    times = tk.Label(message_fr,text = time , font = Font1)


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
    time1.grid(row = 6 ,column = 0)
    times.grid(row = 6,column = 1)
    pr2.grid(row=7, column=2)
    pr.grid(row=7, column=0)
    pr1.grid(row=7, column=1)



