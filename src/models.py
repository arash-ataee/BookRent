import datetime
from abc import ABC
import mysql.connector


conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "123212",
    database = "bookRent"
)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXIST book (
ID INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255) NOT NULL,
category VARCHAR(255) NOT NULL,
edition VARCHAR(255) NOT NULL,
author VARCHAR(255) NOT NULL,
language VARCHAR(255) NOT NULL,
translator VARCHAR(255),
status BOOLEAN NOT NULL,
rent INT,
FOREIGN KEY (rent) REFERENCES member(ID),
rented_date DATE
)""")
conn.commit()

cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXIST member(
ID INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255) NOT NULL,
birth_date DATE NOT NULL,
phone VARCHAR(11),
username VARCHAR(255) NOT NULL,
password VARCHAR(255) NOT NULL,
join_date DATE NOT NULL,
status BOOLEAN NOT NULL,
is_admin BOOLEAN NOT NULL
)""")
conn.commit()

cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXIST rent(
member_id INT NOT NULL,
FOREIGN KEY (member_id) REFERENCES member(ID),
book_id INT NOT NULL,
FOREIGN KEY (book_id) REFERENCES book(ID)
)""")



conn.commit()
conn.close()


class Book:

    def __init__(self, name, category, edition, author, language='persian', translator=None):
        self.name = name
        self.category = category
        self.edition = edition
        self.author = author
        self.language = language
        self.translator = translator
        self.status = True
        self.rent = None
        self.rentedDate = None

    def save(self):
        co = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123212",
            database="bookRent"
        )
        cu = co.cursor()
        sql = "INSERT INTO book (name, category, edition, author, language, translator, status, rent, rented_date) VALUES (?,?,?,?,?,?,?,?,?)"
        val = (
            self.name,
            self.category,
            self.edition,
            self.author,
            self.language,
            self.translator,
            self.status,
            self.rent,
            self.rentedDate
        )
        cu.execute(sql, val)


class Member:

    def __init__(self, name, birth_date, phone, username, password):
        self.name = name
        self.birth_date = birth_date
        self.phone = phone
        self.username = username
        self.password = password
        self.rentedBooks = []
        self.join_date = datetime.datetime.now()
        self.status = 1
        self.log_status = 'logged out'
        self.is_admin = False

    def save(self):
        co = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123212",
            database="bookRent"
        )
        cu = co.cursor()
        sql = "INSERT INTO member (name, birth_date, phone, username, password, join_date, status, is_admin) VALUES (?,?,?,?,?,?,?,?)"
        val = (
            self.name,
            self.birth_date,
            self.phone,
            self.username,
            self.password,
            self.join_date,
            self.status,
            self.is_admin
        )
        cu.execute(sql, val)

    def is_staff(self):
        return self.is_admin

    @property
    def expireCheck(self):
        year1 = datetime.timedelta(days=365)
        if datetime.datetime.now() - self.date > year1:
            self.status = 0
        if len(self.rentedBooks) > 0:
            for book in self.rentedBooks:
                month1 = datetime.timedelta(days=30)
                if datetime.datetime.now() - book.rentedDate > month1:
                    self.status = 2
        else:
            self.status = 1

        return self.status

    def getRentedList(self):
        for book in self.rentedBooks:
            print('(name: %s)' % book.name, '(ID: %s)' % book.bookID, '(rent date: %s)' % book.rentedDate, sep=' - ')


class Request:

    def __init__(self):
        self.user = None

    @property
    def logged_in(self):
        if self.user:
            return True
        else:
            return False

