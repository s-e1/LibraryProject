from pymongo import MongoClient
from classes.Library import *
from utilities.login import login
from utilities.print_options import print_options
from utilities.input_functions import *


client = MongoClient(port=27017)
db = client["libraryDB"]
books_collection = db["books"]
data = list(books_collection.find({}, {"_id": 0}))

libr = Library()
libr.add_new_book(data[0])
libr.add_new_book(data[1])
libr.shelves[1].add_book(data[2])
libr.shelves[1].add_book(data[3])
libr.shelves[2].add_book(data[4])
libr.shelves[2].add_book(data[5])

login()

while True:
    # display the options
    print_options()

    num = int(input())

    if num == 1:
        add_book(libr)
    elif num == 2:
        delete_book(libr)
    elif num == 3:
        switch_book(libr)
    elif num == 4:
        add_reader(libr)
    elif num == 5:
        remove_reader(libr)
    elif num == 6:
        search_author(libr)
    elif num == 7:
        read_book(libr)
    elif num == 8:
        sort_books(libr)
    elif num == 9:
        save_data(libr)
    elif num == 10:
        res = load_data()
        libr = res
    elif num == 11:
        break
