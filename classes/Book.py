class Book():
    def __init__(self, book):
        self.author = book["author"]
        self.title = book["title"]
        self.num_of_pages = book["num_of_pages"]
