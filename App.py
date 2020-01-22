import socket
import time
import select
from src.models import *
import pymongo

logs = pymongo.MongoClient("mongodb://localhost:27017/")
logs_db = logs["mydatabase"]

logs_col = logs_db["customers"]


def login(username, password):
    if username in Member.members_list:
        member = Member.members_list[username]
        if member.password == password:
            if username in Admin.admin_list:
                return 'admin'
            else:
                member.log_status = 'logged in'
                return 'logged in'
        else:
            return 'wrong password'
    else:
        return 'wrong username'


def member_find(username):
    if username in Admin.admin_list:
        return Admin.admin_list[username]
    elif username in Member.members_list:
        return Member.members_list[username]


def book_find(bookID):
    return Book.book_list[bookID]


Admin('arash', 22, '09199931601', 'arash', '1234')

IP = ''
PORT = 8888

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))
server_socket.listen(5)

socket_list = [server_socket]

members = {}

while True:
    read_socket, write_socket, exception_socket = select.select(socket_list, [], socket_list)
    for s in read_socket:
        if s == server_socket:
            client_socket, address = server_socket.accept()
            if client_socket:
                socket_list.append(client_socket)
                print("Connection Established from {}".format(address))

        else:
            message = None
            try:
                message = s.recv(1024).decode('utf-8')
            except IOError:
                continue
            if message:
                print(message)
                if message.startswith('unpw'):
                    user_pass = message[4:].split()
                    login_return = login(username=user_pass[0], password=user_pass[1])
                    s.send(bytes(login_return, 'utf-8'))
                    members[s] = member_find(username=user_pass[0])
                    login_dict = {'action': login_return, 'user': user_pass[0], 'pass': user_pass[1]}
                    a = logs_col.insert_one(login_dict)
                    message = None

                elif message.startswith('adbk'):
                    book_info = message[4:].split()
                    members[s].addBook(book_info[0], book_info[1], book_info[2], book_info[3])
                    add_book_dict = {'book info': [book_info[0], book_info[1], book_info[2], book_info[3]]}
                    b = logs_col.insert_one(add_book_dict)

                elif message.startswith('rnbk'):
                    rn_book = message[4:].split()
                    renew_book = book_find(rn_book[0])
                    members[s].renewalBook(renew_book)

                elif message.startswith('admb'):
                    member_info = message[4:].split()
                    members[s].addMember(member_info[0], member_info[1], member_info[2], member_info[3], member_info[4])
                    add_member_dict = {
                        'member info': [member_info[0], member_info[1], member_info[2], member_info[3], member_info[4]]}
                    c = logs_col.insert_one(add_member_dict)

                elif message.startswith('rnmb'):
                    rn_member = message[4:].split()
                    renew_member = member_find(rn_member[0])
                    members[s].renewalMember(renew_member)
                    renew_member_dict = {'renewed member': rn_member[0]}
                    d = logs_col.insert_one(renew_member_dict)

                elif message.startswith('rent'):
                    rent = message[4:].split()
                    member = Member.members_list[rent[0]]
                    book = Book.book_list[rent[1]]
                    members[s].rentBook(member, book)
                    rent_dict = {'rented book': rent[1], 'member': rent[0]}
                    e = logs_col.insert_one(rent_dict)

                elif message.startswith('blst'):
                    b_list = ''
                    for book in Book.book_list.values():
                        b_list += book.name + '-' + book.category + '-' + book.edition + '-' + book.author + ' '
                    s.send(bytes(b_list, 'utf-8'))

                elif message.startswith('mybl'):
                    my_b = ''
                    for book in members[s].rentedBooks:
                        my_b += book.name + '-' + book.bookID + ' '
                    s.send(bytes(my_b, 'utf-8'))

    for s in exception_socket:
        socket_list.remove(s)

    time.sleep(1)
