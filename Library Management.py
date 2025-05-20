# by qrvnix

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.genre = []
    
    def __str__(self):
        return f"{self.title} by {self.author} | Genres: {self.genre}"
        
class Library:
    def __init__(self):
        self.catalog = {}
        self.books = []
        self.unique_genres = set()
    
    def add_book(self, book):
        self.books.append(book)
        self.catalog[book.title] = book
        self.unique_genres.update(book.genre)
    
    def display_book(self):
        for items in self.books:
            print(items)
    
    def display_unique_genres(self):
        print("Unique Genres:")
        for items in self.unique_genres:
            print(f"- {items}")
    
    def menu(self):
        while True:
            print("-----LIBRARY MANAGEMENT-----")
            print(" 1. Add book\n 2. Display all books\n 3. Display unique genres\n 4. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                title = str(input("\nEnter book title: "))
                author = str(input("Enter book author: "))
                book_info = Book(title, author)

                genre_amount = int(input("How many genres: "))
                for amount in range(genre_amount):
                    genre = str(input(f"Enter genre {amount + 1}: "))
                    book_info.genre.append(genre)

                library.add_book(book_info)
                print(f"Book {book_info.title} added successfully.\n")
            
            elif choice == 2:
                print("\n-----DISPLAY BOOK-----")
                library.display_book()
                print('')

            elif choice == 3:
                print("\n-----DISPLAY UNIQUE GENRES-----")
                library.display_unique_genres()
                print('')

            elif choice == 4:
                break

library = Library()
library.menu()