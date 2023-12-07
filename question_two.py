#2i)
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

# Creating an instance of the class
book = Book("Mysteries of Queen Esther", "Nagawa Esther", "13")

# Displaying the information about the book
book.display_info()

#ii)
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_title_and_author(self):
        return f"Title: {self.title}, Author: {self.author}"

class EBook(Book):
    def __init__(self, title, author, format):
        super().__init__(title, author)
        self.format = format

# Displaying an instance of the EBook class
ebook = EBook("Mysteries of Queen Esther", "Nagawa Esther", "word")
print(f"Title: {ebook.title}, Author: {ebook.author}, Format: {ebook.format}")

# Creating the function on the Book class to return only the book title and its author
print(ebook.get_title_and_author())


#iv) Define the following terms:
# Class: A blueprint for creating objects that defines their attributes and behavior.
# Object: An instance of a class that combines attributes and behavior.
