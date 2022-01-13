from classes.Book import Book


class Shelf():
    def __init__(self):
        self.is_shelf_full = False
        self.books = []

    def add_book(self, book):
        if not self.is_shelf_full:
            b = Book(book)
            self.books.append(b)
            if len(self.books) == 5:
                self.is_shelf_full = True
        else:
            print("The shelf is full")

    def switch_books(self, num1, num2):
        if not self.books[num1-1]:
            print("No books in space " + str(num1))
        elif not self.books[num2-1]:
            print("No books in space " + str(num2))
        else:
            self.books[num1-1], self.books[num2 -
                                           1] = self.books[num2-1], self.books[num1-1]

    def order_books(self):
        self.books.sort(key=lambda x: x.num_of_pages)
        # print([book.__dict__ for book in self.books])
