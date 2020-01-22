from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import socket
import time

IP = 'localhost'
PORT = 8888
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.connect((IP, PORT))
server_socket.setblocking(0)

socket_list = [server_socket]

root = Tk()
root.title('library')
root.resizable(False, False)


def admin_win():
    def add_book_win():
        def add_book_def():
            b_name = book_name_var.get()
            b_category = book_category_var.get()
            b_edition = book_edition_var.get()
            b_author = book_author_var.get()
            server_socket.send(bytes('adbk' + b_name + ' ' + b_category + ' ' + b_edition + ' ' + b_author, 'utf-8'))

        add_book_frame = ttk.Frame(root, padding=(50, 50, 62, 62))
        add_book_frame.grid(column=0, row=0)
        add_book_label = Label(add_book_frame, font=('tahoma', 20), text='add book ')
        add_book_label.grid(column=1, row=1)
        book_name_var = StringVar()
        book_category_var = StringVar()
        book_edition_var = StringVar()
        book_author_var = StringVar()
        book_name_label = Label(add_book_frame, font=('tahoma', 15), text='book name: ')
        book_name_label.grid(column=1, row=2)
        book_name = Entry(add_book_frame, font=('tahoma', 15), width=20, textvariable=book_name_var)
        book_name.grid(column=2, row=2)
        book_category_label = Label(add_book_frame, font=('tahoma', 15), text='book category: ')
        book_category_label.grid(column=1, row=3)
        book_category = Entry(add_book_frame, font=('tahoma', 15), width=20, textvariable=book_category_var)
        book_category.grid(column=2, row=3)
        book_edition_label = Label(add_book_frame, font=('tahoma', 15), text='book edition: ')
        book_edition_label.grid(column=1, row=4)
        book_edition = Entry(add_book_frame, font=('tahoma', 15), width=20, textvariable=book_edition_var)
        book_edition.grid(column=2, row=4)
        book_author_label = Label(add_book_frame, font=('tahoma', 15), text='book author: ')
        book_author_label.grid(column=1, row=5)
        book_author = Entry(add_book_frame, font=('tahoma', 15), width=20, textvariable=book_author_var)
        book_author.grid(column=2, row=5)
        add_book_btn = Button(add_book_frame, font=('tahoma', 15), text='add book', command=add_book_def)
        add_book_btn.grid(column=2, row=6)
        back_btn = Button(add_book_frame, font=('tahoma', 15), text='back', command=admin_win)
        back_btn.grid(column=2, row=7)

    def renew_book_win():
        def renew_book_def():
            rn_book = renew_book_var.get()
            server_socket.send(bytes('rnbk' + rn_book, 'utf-8'))

        renew_book_frame = ttk.Frame(root, padding=(50, 50, 62, 62))
        renew_book_frame.grid(column=0, row=0)
        renew_book_label = Label(renew_book_frame, font=('tahoma', 20), text='renewal book: ')
        renew_book_label.grid(column=1, row=1)
        renew_book_var = StringVar()
        renew_book_label = Label(renew_book_frame, font=('tahoma', 15), text='book ID: ')
        renew_book_label.grid(column=1, row=2)
        renew_book_name = Entry(renew_book_frame, font=('tahoma', 15), width=20, textvariable=renew_book_var)
        renew_book_name.grid(column=2, row=2)
        renew_book_btn = Button(renew_book_frame, font=('tahoma', 15), text='renewal book', command=renew_book_def)
        renew_book_btn.grid(column=2, row=3)
        back_btn = Button(renew_book_frame, font=('tahoma', 15), text='back', command=admin_win)
        back_btn.grid(column=2, row=4)

    def add_member_win():
        def add_member_def():
            m_name = member_name_var.get()
            m_age = member_age_var.get()
            m_phone = member_phone_var.get()
            m_username = member_username_var.get()
            m_password = member_password_var.get()
            server_socket.send(
                bytes('admb' + m_name + ' ' + m_age + ' ' + m_phone + ' ' + m_username + ' ' + m_password, 'utf-8'))

        add_member_frame = ttk.Frame(root, padding=(50, 50, 62, 62))
        add_member_frame.grid(column=0, row=0)
        add_member_label = Label(add_member_frame, font=('tahoma', 20), text='add member ')
        add_member_label.grid(column=1, row=1)
        member_name_var = StringVar()
        member_age_var = StringVar()
        member_phone_var = StringVar()
        member_username_var = StringVar()
        member_password_var = StringVar()
        member_name_label = Label(add_member_frame, font=('tahoma', 15), text='member name: ')
        member_name_label.grid(column=1, row=2)
        member_name = Entry(add_member_frame, font=('tahoma', 15), width=20, textvariable=member_name_var)
        member_name.grid(column=2, row=2)
        member_age_label = Label(add_member_frame, font=('tahoma', 15), text='member age: ')
        member_age_label.grid(column=1, row=3)
        member_age = Entry(add_member_frame, font=('tahoma', 15), width=20, textvariable=member_age_var)
        member_age.grid(column=2, row=3)
        member_phone_label = Label(add_member_frame, font=('tahoma', 15), text='member phone: ')
        member_phone_label.grid(column=1, row=4)
        member_phone = Entry(add_member_frame, font=('tahoma', 15), width=20, textvariable=member_phone_var)
        member_phone.grid(column=2, row=4)
        member_username_label = Label(add_member_frame, font=('tahoma', 15), text='member username: ')
        member_username_label.grid(column=1, row=5)
        member_username = Entry(add_member_frame, font=('tahoma', 15), width=20, textvariable=member_username_var)
        member_username.grid(column=2, row=5)
        member_password_label = Label(add_member_frame, font=('tahoma', 15), text='member password: ')
        member_password_label.grid(column=1, row=6)
        member_password = Entry(add_member_frame, font=('tahoma', 15), show='*', width=20, textvariable=member_password_var)
        member_password.grid(column=2, row=6)
        add_member_btn = Button(add_member_frame, font=('tahoma', 15), text='add member', command=add_member_def)
        add_member_btn.grid(column=2, row=7)
        back_btn = Button(add_member_frame, font=('tahoma', 15), text='back', command=admin_win)
        back_btn.grid(column=2, row=8)

    def renew_member_win():
        def renew_member_def():
            rn_member = renew_member_var.get()
            server_socket.send(bytes('rnmb' + rn_member, 'utf-8'))

        renew_member_frame = ttk.Frame(root, padding=(50, 50, 62, 62))
        renew_member_frame.grid(column=0, row=0)
        renew_member_label = Label(renew_member_frame, font=('tahoma', 20), text='renewal member: ')
        renew_member_label.grid(column=1, row=1)
        renew_member_var = StringVar()
        renew_member_label = Label(renew_member_frame, font=('tahoma', 15), text='member ID: ')
        renew_member_label.grid(column=1, row=2)
        renew_member_name = Entry(renew_member_frame, font=('tahoma', 15), width=20, textvariable=renew_member_var)
        renew_member_name.grid(column=2, row=2)
        renew_member_btn = Button(renew_member_frame, font=('tahoma', 15), text='renewal member',
                                  command=renew_member_def)
        renew_member_btn.grid(column=2, row=3)
        back_btn = Button(renew_member_frame, font=('tahoma', 15), text='back', command=admin_win)
        back_btn.grid(column=2, row=4)

    def rent_win():
        def rent_def():
            m_username = member_var.get()
            b_id = book_var.get()
            server_socket.send(bytes('rent' + m_username + ' ' + b_id, 'utf-8'))

        rent_frame = ttk.Frame(root, padding=(50, 50, 62, 62))
        rent_frame.grid(column=0, row=0)
        rent_label = Label(rent_frame, font=('tahoma', 20), text='rent book ')
        rent_label.grid(column=1, row=1)
        member_var = StringVar()
        book_var = StringVar()
        member_label = Label(rent_frame, font=('tahoma', 15), text='member username: ')
        member_label.grid(column=1, row=2)
        member = Entry(rent_frame, font=('tahoma', 15), width=20, textvariable=member_var)
        member.grid(column=2, row=2)
        book_label = Label(rent_frame, font=('tahoma', 15), text='book ID: ')
        book_label.grid(column=1, row=3)
        book = Entry(rent_frame, font=('tahoma', 15), width=20, textvariable=book_var)
        book.grid(column=2, row=3)
        rent_btn = Button(rent_frame, font=('tahoma', 15), text='add member', command=rent_def)
        rent_btn.grid(column=2, row=4)
        back_btn = Button(rent_frame, font=('tahoma', 15), text='back', command=admin_win)
        back_btn.grid(column=2, row=5)

    admin_frame = ttk.Frame(root, padding=(50, 50, 62, 62))
    admin_frame.grid(column=0, row=0)
    admin_label = Label(admin_frame, font=('tahoma', 20), text='logged in as admin. ')
    admin_label.grid(column=1, row=1)
    add_book = Button(admin_frame, font=('tahoma', 15), text='add book', command=add_book_win)
    add_book.grid(column=1, row=2)
    renew_book = Button(admin_frame, font=('tahoma', 15), text='renewal book', command=renew_book_win)
    renew_book.grid(column=2, row=2)
    add_member = Button(admin_frame, font=('tahoma', 15), text='add member', command=add_member_win)
    add_member.grid(column=1, row=3)
    renew_member = Button(admin_frame, font=('tahoma', 15), text='renewal member', command=renew_member_win)
    renew_member.grid(column=2, row=3)
    rent = Button(admin_frame, font=('tahoma', 15), text='rent book', command=rent_win)
    rent.grid(column=1, row=4)
    logout = Button(admin_frame, font=('tahoma', 15), text='logout', command=login_win)
    logout.grid(column=2, row=4)


def member_win():
    def book_list_win():
        server_socket.send(bytes('blst', 'utf-8'))
        b_list = None
        while not b_list:
            time.sleep(1)
            try:
                b_list = server_socket.recv(1024).decode('utf-8')
                print(b_list)
            except IOError as e:
                continue
        book_list = b_list.split()
        show_list.delete(0, 'end')
        for book in book_list:
            show_list.insert('end', book)

    def my_book_win():
        server_socket.send(bytes('mybl', 'utf-8'))
        my_b = None
        while not my_b:
            time.sleep(1)
            try:
                my_b = server_socket.recv(1024).decode('utf-8')
                print(my_b)
            except IOError as e:
                continue
        my_book = my_b.split()
        show_list.delete(0, 'end')
        for book in my_book:
            show_list.insert('end', book)

    member_frame = ttk.Frame(root, padding=(50, 50, 62, 62))
    member_frame.grid(column=0, row=0)
    username_label = Label(member_frame, font=('tahoma', 20), text='logged in as member: ')
    username_label.grid(column=1, row=1)
    show_book_list = Button(member_frame, font=('tahoma', 15), text='library book list', command=book_list_win)
    show_book_list.grid(column=1, row=2)
    show_my_book = Button(member_frame, font=('tahoma', 15), text='my book list', command=my_book_win)
    show_my_book.grid(column=1, row=3)
    show_list = Listbox(member_frame, height=10, font=('tahoma', 15))
    show_list.grid(column=1, row=4)
    sy_show_list = ttk.Scrollbar(member_frame, orient=VERTICAL, command=show_list.yview)
    sx_show_list = ttk.Scrollbar(member_frame, orient=HORIZONTAL, command=show_list.xview)
    sy_show_list.grid(column=2, row=4)
    sx_show_list.grid(column=1, row=5)
    logout = Button(member_frame, font=('tahoma', 15), text='logout', command=login_win)
    logout.grid(column=1, row=6)


def login_win():
    def login():
        user_name = username_var.get()
        pass_word = password_var.get()
        server_socket.send(bytes('unpw' + ' ' + user_name + ' ' + pass_word, 'utf-8'))
        login_return = None
        while not login_return:
            time.sleep(1)
            try:
                login_return = server_socket.recv(1024).decode('utf-8')
                print(login_return)
            except IOError as e:
                continue

        return login_return

    def login_check():
        user_name = username.get()
        if ' ' not in user_name:
            login_command = login()
            if login_command == 'admin':
                admin_win()
            elif login_command == 'logged in':
                member_win()
            elif login_command == 'wrong password':
                messagebox.showinfo(message="wrong password! ", title='username error')
            elif login_command == 'wrong username':
                messagebox.showinfo(message="wrong username! ", title='username error')
        else:
            messagebox.showinfo(message='do not use space in your username', title='username error')

    login_frame = ttk.Frame(root, padding=(50, 50, 62, 62))
    login_frame.grid(column=0, row=0)
    username_label = Label(login_frame, font=('tahoma', 15), text='username: ')
    username_label.grid(column=1, row=1)
    password_label = Label(login_frame, font=('tahoma', 15), text='password: ')
    password_label.grid(column=1, row=2)
    username_var = StringVar()
    password_var = StringVar()
    username = Entry(login_frame, font=('tahoma', 15), width=20, textvariable=username_var)
    username.grid(column=2, row=1)
    password = Entry(login_frame, font=('tahoma', 15), width=20, show='*', textvariable=password_var)
    password.grid(column=2, row=2)
    set_name = Button(login_frame, font=('tahoma', 15), text='set username', command=login_check)
    set_name.grid(column=2, row=3)


login_win()

root.mainloop()
#    time.sleep(5)
