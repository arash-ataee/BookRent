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

cur.execute("CREATE TABLE IF NOT EXIST ")


class Book:

    def __init__(self, name, category, edition, author, language='persian', translator=None):
        self.name = name
        self.category = category
        self.edition = edition
        self.author = author
        self.language = language
        self.translator = translator
        self.bookID = Book.ID
        self.status = True
        self.rent = None
        self.rentedDate = None
        Book.book_list[self.bookID] = self
        Book.ID += 1


class Member:

    def __init__(self, name, age, phone, username, password):
        self.name = name
        self.age = age
        self.phone = phone
        self.username = username
        self.password = password
        self.rentedBooks = []
        self.date = datetime.datetime.now()
        self.status = 1
        self.log_status = 'logged out'
        self.is_admin = False

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

