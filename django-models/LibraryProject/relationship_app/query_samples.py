from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author (e.g., author with ID 1)
def get_books_by_author(author_id):
    author = Author.objects.get(id=author_id)
    books = Book.objects.filter(author=author)
    return books

# 2. List all books in a specific library (e.g., library with ID 1)
def get_books_in_library(library_id):
    library = Library.objects.get(id=library_id)
    books = library.books.all()
    return books

# 3. Retrieve the librarian for a specific library (e.g., library with ID 1)
def get_librarian_for_library(library_id):
    library = Library.objects.get(id=library_id)
    librarian = Librarian.objects.get(library=library)
    return librarian