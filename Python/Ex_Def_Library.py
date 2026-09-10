'''
Library:
You need to create two classes: book and library

Create a method that:
If the book is available, change available to False and return True.
If its already borrowed, return False.

And:

Create a add_book method and a find_book method 


'''


class Book:
    def __init__(self, title:str, author: str):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self) -> bool:
        if self.available:
            self.available = False
            return True
        return False


class Library:
    def __init__(self):
        self.books = {}


    def add_book(self, title: str, author: str) -> None:
        if title not in self.books:
            book = Book(title,author)
            self.books[title] = book

    def find_book(self,title: str) -> Book | None:
        if title in self.books:
            return self.books[title]
        return None

        

livraria = Library()

livraria.add_book("Little prince", "John Pork")

book = livraria.find_book("Little prince")
print(book.available)
book.borrow()
print(book.available)
    
                

            
