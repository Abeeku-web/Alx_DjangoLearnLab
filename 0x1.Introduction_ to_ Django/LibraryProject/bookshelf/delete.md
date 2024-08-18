# Delete Operation
from bookshelf.models import Book


```python
# Delete the book instance
book.delete()

# Confirm deletion
books = Book.objects.all()
print(books)