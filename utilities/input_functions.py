import json
import os
import sys
from classes.Library import *


def add_book(libr):
    author = input("Enter the author's name: ")
    title = input("Enter the book's title: ")
    num_of_pages = int(input("Enter the number of pages: "))
    res = libr.add_new_book({"author": author, "title": title,
                             "num_of_pages": num_of_pages})
    print(f"The book was {'' if res else 'not'} added")


def delete_book(libr):
    title = input("Enter the book's title: ")
    res = libr.delete_book(title)
    print(f"The book was {'' if res else 'not'} deleted")


def switch_book(libr):
    title1 = input("Enter the first book's title: ")
    title2 = input("Enter the second book's title: ")
    res = libr.change_locations(title1, title2)
    print(f"The books were {'' if res else 'not'} switched")


def add_reader(libr):
    id = input("Enter the reader's id: ")
    name = input("Enter the reader's name: ")
    libr.register_reader(id, name)
    print("The reader was registered")


def remove_reader(libr):
    name = input("Enter the reader's name: ")
    res = libr.remove_reader(name)
    print(f"The reader was {'' if res else 'not'} deleted")


def search_author(libr):
    name = input("Enter the author's name: ")
    results = libr.search_by_author(name)
    print(results)


def read_book(libr):
    title = input("Enter the book's title: ")
    name = input("Enter the reader's name: ")
    res = libr.reader_read_book(title, name)
    print(
        f"The book was {'' if res else 'not'} added to the reader's read list")


def sort_books(libr):
    libr.order_books()
    print("The books were sorted")


def save_data(libr):
    with open('data.json', 'w') as f:
        obj = {"shelves": [], "readers": []}
        for shelf in libr.shelves:
            sh = {}
            sh["is_shelf_full"] = shelf.is_shelf_full
            sh["books"] = [book.__dict__ for book in shelf.books]
            obj["shelves"].append(sh)
        for reader in libr.readers:
            rdr = {}
            rdr["id"] = reader.id
            rdr["name"] = reader.name
            rdr["books"] = reader.books
            obj["readers"].append(rdr)
        json.dump(obj, f, indent=4)
    print("The data was saved")


def load_data():
    with open(os.path.join(sys.path[0], "data.json"), "r") as f:
        data = json.load(f)
        # print(data)

        libr = Library()
        for i, shelf in enumerate(data["shelves"]):
            libr.shelves[i].is_shelf_full = shelf["is_shelf_full"]
            libr.shelves[i].books = []
            for book in shelf["books"]:
                libr.shelves[i].add_book(book)
        for reader in data["readers"]:
            libr.register_reader(reader["id"], reader["name"])
            for i, book in enumerate(reader["books"]):
                libr.reader_read_book(
                    reader["books"][i]["title"], reader["name"])
    print("The data was loaded")
    return libr
