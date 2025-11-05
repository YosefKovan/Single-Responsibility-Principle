

class BookToFile:

    def __init__(self, book):
        self.book = book

    def save_to_file(self):
        with open(f"{self.book.title}.txt", "w") as f:
            f.write(self.book.content)