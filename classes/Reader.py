# Class : Reader
# Data Members:
# - id (int)
# - books (a list of dictionaries with titles of the books he read and the dates he took
# them from the library)
# Functions
# - read_book – receives a book title and adds it + the current date to the books list

from datetime import date


class Reader():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.books = []

    def read_book(self, title):
        today = str(date.today())
        self.books.append({"title": title, "date_read": today})
