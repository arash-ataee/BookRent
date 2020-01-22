import datetime
from abc import ABC


class Book:
    ID = 44332211
    book_list = {}

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
    ID = 332211
    members_list = {}

    def __init__(self, name, age, phone, username, password):
        self.name = name
        self.age = age
        self.phone = phone
        self.username = username
        self.password = password
        self.ID = Member.ID
        self.rentedBooks = []
        self.date = datetime.datetime.now()
        self.status = 1
        self.log_status = 'logged out'
        Member.members_list[self.username] = self
        Member.ID += 1

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


class Admin(Member):
    admin_list = {}

    def __init__(self, name, age, phone, username, password):
        super().__init__(name=name, age=age, phone=phone, username=username, password=password)
        self.log_status = 'admin'
        Admin.admin_list[self.username] = self

    def addBook(self, name, category, edition, author, language='persian', translator=None):
        Book(name=name, category=category, edition=edition, author=author, language=language, translator=translator)

    def addMember(self, name, age, phone, username, password):
        if username in Member.members_list:
            return False
        else:
            Member(name=name, age=age, phone=phone, username=username, password=password)
            return True

    def adminMaker(self, member):
        name = member.name
        age = member.age
        phone = member.phone
        username = member.username
        password = member.password
        Admin(name, age, phone, username, password)
        del member

    def renewalMember(self, member):
        member.date = datetime.datetime.now()

    def rentBook(self, member, book_list):
        for book in book_list:
            member.expireCheck()
            if member.status == 1 and book.status:
                member.rentedBooks.append(book)
                book.status = False
                book.rent = member.ID
                book.rentedDate = datetime.datetime.now()
            else:
                print('you can rent %s by bookID %d' % (book.name, book.bookID))

    def giveBackBook(self, member, book_list):
        for book in book_list:
            if not book.status and book.rent == member.ID:
                member.rentedBooks.remove(book)
                book.status = True
                book.rent = None
                book.rentedDate = None

    def renewalBook(self, book):
        if not book.status:
            book.rentedDate = datetime.datetime.now()
