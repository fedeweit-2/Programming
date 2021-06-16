from listNode import *


class Book:

    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = int(year)
        self.genre = genre if (genre in ["horror", "fantasy", "thriller", "fiction"]) else None

    def __eq__(self, other_book):
        return self.title == other_book.title and \
               self.author == other_book.author and \
               self.year == other_book.year and \
               self.genre == other_book.genre


    def __str__(self):
        return f"{self.title} - {self.author}, {self.year}, {self.genre}"

class Library:
    def __init__(self, books):
        self.linkedBooks = SinglyLinkedList(ListNode(books[0]))
        for book in books[1:]:
            self.linkedBooks.add_node(book)

    def __str__(self):
        toPrint = []
        for book in self.linkedBooks:
            toPrint.append(book.__str__())
        return str(toPrint)

    def add_book(self, book):
        self.linkedBooks.add_node(book)

    # I'm not sure you wanted this kind of input for the books,
    # I could have put the index of the books for the library but it
    # didn't seem appropriate in order to recognize the books.

    def _compare_by_title(self, book1, book2):
        return book1.title > book2.title

    def _compare_by_author(self, book1, book2):
        return book1.author > book2.author

    def _compare_by_genre(self, book1, book2):
        return book1.genre > book2.genre

    def _compare_by_year(self, book1, book2):
        return book1.year > book2.year

    def bubbleSort(self, custom_sort):
        n = len(self.linkedBooks)

        for i in range(n - 1):
            for j in range(n - i - 1):
                if custom_sort(self.linkedBooks[j], self.linkedBooks[j + 1]):
                    self.linkedBooks.swap(j, j + 1)
                else:
                    continue

    def sort_books_by_title(self):
        self.bubbleSort(self._compare_by_title)

    def sort_books_by_author(self):
        self.bubbleSort(self._compare_by_author)

    def sort_books_by_year(self):
        self.bubbleSort(self._compare_by_year)

    def sort_books_by_genre(self):
        self.bubbleSort(self._compare_by_genre)


if __name__ == '__main__':

    # list of books without the last one, will be added later
    books = [Book('Dagon', 'H.P.Lovecraft', 1919, 'horror'),
             Book('The Call of Cthulhu', 'H.P.Lovecraft', 1928, 'horror'),
             Book('At the Mountains of Madness', 'H.P.Lovecraft', 1928, 'horror'),
             Book('Jurassic Park', 'Michael Crichton', 1987, 'fiction'),
             Book('Sphere', 'Michael Crichton', 1987, 'fiction'),
             Book('Prey', 'Michael Crichton', 2002, 'fiction'),
             Book('The Hobbit', 'J.R.R.Tolkien', 1937, 'fantasy'),
             Book('The Lord of the Rings', 'J.R.R.Tolkien', 1954, 'fantasy'),
             Book('Animal Farm', 'George Orwell', 1945, 'fiction'),
             Book('Nineteen Eighty-Four', 'George Orwell', 1949, 'fiction'),
             Book('It', 'Stephen King', 1986, 'thriller'),
             Book('Pet Sematary', 'Stephen King', 1983, 'thriller')]

    # test the __str__ method
    print("book 1: ", books[0])
    print("book 2: ", books[1])
    print('-' * 100)

    # test the __eq__ method
    print("\nAre book[0] and book[1] equal?", books[0] == books[1])
    print('-' * 100)

    # test and set up the Library linked list
    library_1 = Library(books)

    # adding the last book
    library_1.add_book(Book('Horus Rising', 'Dan Abnett', 2006, 'fantasy'))

    # testing out the sorting methods

    print("\nNot sorted list:")
    print(library_1)
    print('-' * 100)

    print("\nsorted by title list:")
    library_1.sort_books_by_title()
    print(library_1)

    print("\nsorted by year list:")
    library_1.sort_books_by_year()
    print(library_1)

    print("\nsorted by genre list:")
    library_1.sort_books_by_genre()
    print(library_1)


