from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> print(book)
1984

>>> retrieved_book = Book.objects.get(id=book.id)
>>> #Display book details
>>> print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)
1984 George Orwell 1949

>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> print(book.title)
Nineteen Eighty-Four

>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> books = Book.objects.all()
>>> print(books)
<QuerySet []>