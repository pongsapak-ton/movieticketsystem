from tkinter import *
# from functools import partial


def login_user(screen):
    username_info = username.get()
    password_info = password.get()
    a = '1223'
    print(password_info)
    print(password)


    if password_info in a :        # messagebox.showinfo('CONGRATULATIONS','Login successful')
        Label(screen1, text="LOGIN sucess", fg="green", font=("calibri", 11)).pack()







    else:
        username_entry.delete(0, END)
        password_entry.delete(0, END)


def login_screen(screen):
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("LOGIN PAGE")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()

    Label(screen1, text="Username").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    # Entry(screen1,textvariable=username).pack()

    Label(screen1, text="Password").pack()
    # password_entry=Entry(screen1,textvariable=password)
    password_entry = Entry(screen1, textvariable=password, show='*')
    password_entry.pack()
    Label(screen1, text="").pack()

    Button(screen1, text="LOGIN", width=10, height=1, command=lambda: login_user(screen1)).pack()


