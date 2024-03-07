class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publication Year:", self.publication_year)


class FictionBook(Book):
    def __init__(self, title, author, publication_year, genre):
        super().__init__(title, author, publication_year)
        self.genre = genre

    def display_info(self):
        super().display_info()
        print("Genre:", self.genre)


class NonFictionBook(Book):
    def __init__(self, title, author, publication_year, topic):
        super().__init__(title, author, publication_year)
        self.topic = topic

    def display_info(self):
        super().display_info()
        print("Topic:", self.topic)


# Instantiate objects of each class
fiction_book = FictionBook("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
non_fiction_book = NonFictionBook("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", 2011, "Anthropology")

# Call display_info() for each object
fiction_book.display_info()
print()
non_fiction_book.display_info()
