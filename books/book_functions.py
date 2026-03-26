"""
Book functions
"""

from Book import Book
from Book import load_books

def get_genres(books:list[Book])->list[str]:
    """Return a list of unique genres from the list of books"""
    genres = set()
    for book in books:
        genres.add(book.genre)
    return sorted(genres)

def create_author_dictionary(books:list[Book])->dict[str, list[Book]]:
    """Return a dictionary with authors as keys and a list of their books as values"""
    author_dict = {}
    for book in books:
        if book.author.lower() not in author_dict:
            author_dict[book.author.lower()] = []
        author_dict[book.author.lower()].append(book)
        author_names = book.author.lower().split(" ")
        if len(author_names) >= 2:
            for name in author_names:
                if name not in author_dict:
                    author_dict[name] = []
                author_dict[name].append(book)
    return author_dict

def create_book_dictionary(book_list:list)->dict[int, Book]:
    """Return a dictionary with book id as keys and book objects as values"""
    book_dict = {}
    for book in book_list:
        book_dict[book.id] = book
    return book_dict

if __name__ == "__main__":
    # Load books from csv file
    books = load_books("booklist2000.csv")
    print(get_genres(books))
    author_dict = create_author_dictionary(books)
    print(author_dict["sandra"][0])