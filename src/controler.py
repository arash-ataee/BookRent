import datetime
import functools

from .models import *


def login_required(func):
    @functools.wraps(func)
    def wrapper_login(request, *args, **kwargs)
        if request.user:
            return func(request, *args, **kwargs)
        else:
            pass

    return wrapper_login


def is_staff_required(func):
    @functools.wraps(func)
    def wrapper_is_staff(request, *args, **kwargs):
        if request.user.is_staff is True:
            return func(request, *args, **kwargs)
        else:
            pass
    return wrapper_is_staff



def addBook(name, category, edition, author, language='persian', translator=None):
    Book(name=name, category=category, edition=edition, author=author, language=language, translator=translator)


def addMember(name, age, phone, username, password):
    if username in Member.members_list:
        return False
    else:
        Member(name=name, age=age, phone=phone, username=username, password=password)
        return True


def adminMaker(member):
    member.is_admin = True


def renewalMember(member):
    member.date = datetime.datetime.now()


def rentBook(member, book_list):
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


def renewalBook(book):
    if not book.status:
        book.rentedDate = datetime.datetime.now()