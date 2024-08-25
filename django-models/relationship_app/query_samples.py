from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    # Retrieve the author object
    author = Author.objects.get(name=author_name)
    # Use objects.filter() to get all books by the author
    books = Book.objects.filter(author=author)
    return books

# List all books in a specific library
def get_books_in_library(library_name):
    # Retrieve the library object
    library = Library.objects.get(name=library_name)
    # Use the related name 'books' to get all books in the library
    return library.books.all()

# Retrieve the librarian for a specific library
def get_librarian_for_library(library_name):
    # Retrieve the library object
    library = Library.objects.get(name=library_name)
    # Use Librarian.objects.get() to retrieve the librarian for the specific library
    librarian = Librarian.objects.get(library=library)
    return librarian