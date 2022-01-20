from datetime import date


class Reader():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.books = []

    def read_book(self, title):
        today = str(date.today())
        self.books.append({"title": title, "date_read": today})
