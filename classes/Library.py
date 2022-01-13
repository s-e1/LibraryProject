from classes.Shelf import *
from classes.Reader import *


class Library():
    def __init__(self):
        self.shelves = [Shelf(), Shelf(), Shelf()]
        self.readers = []

    #not used
    def is_there_place_for_new_book(self):
        for shelf in self.shelves:
            if shelf.is_shelf_full:
                continue
            else:
                return True
        return False

    def add_new_book(self, book):
        for shelf in self.shelves:
            if shelf.is_shelf_full:
                continue
            else:
                shelf.add_book(book)
                return True
        return False

    def delete_book(self, title):
        for shelf in self.shelves:
            filtered_books = list(
                filter(lambda book: book.title != title, shelf.books))
            if len(filtered_books) < len(shelf.books):
                shelf.books = filtered_books
                return True
        return False

    def change_locations(self, title1, title2):
        data1 = None
        data2 = None
        for i, shelf in enumerate(self.shelves):
            for j, book in enumerate(shelf.books):
                if book.title == title1:
                    book1 = shelf.books.pop(j)
                    data1 = [i, j, book1]
                    break
        for i, shelf in enumerate(self.shelves):
            for j, book in enumerate(shelf.books):
                if book.title == title2:
                    book2 = shelf.books.pop(j)
                    data2 = [i, j, book2]
                    break
        if data1 and data2:
            self.shelves[data1[0]].books.insert(data1[1], data1[2])
            self.shelves[data2[0]].books.insert(data2[1], data2[2])
            return True
        return False

    #not used
    def change_locations_in_same_shelf(self, shelf_num, num1, num2):
        self.shelves[shelf_num].switch_books(num1, num2)

    def order_books(self):
        for shelf in self.shelves:
            shelf.order_books()

    def register_reader(self, id, name):
        r = Reader(id, name)
        self.readers.append(r)

    def remove_reader(self, name):
        for i, reader in enumerate(self.readers):
            if reader.name == name:
                self.readers.pop(i)
                return True
        return False

    def reader_read_book(self, title, name):
        for reader in self.readers:
            if reader.name == name:
                reader.read_book(title)
                return True
        return False

    def search_by_author(self, name):
        results = []
        for shelf in self.shelves:
            for book in shelf.books:
                if book.author == name:
                    results.append(book.title)
        return results
