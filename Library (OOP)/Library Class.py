class Library:
   def __init__(self):
      self.books = []
      self.no_of_books = 0

   def show_books(self):
      print(f'The books in your library are', ', '.join(self.books))
      
   def add_books(self, book):
      self.books.append(book)
      self.no_of_books = len(self.books)
   
   def show_count(self):
      print(f'Total number of books in your library is: {self.no_of_books}')

lib = Library()

lib.add_books('Harry Potter')
lib.add_books('The Hobbit')
lib.add_books('1984')
lib.show_books()
lib.show_count()