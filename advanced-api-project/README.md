# views.py

"""
BookListView: Handles GET requests to list all books and POST requests to create a new book.
Permission: Authenticated users can create books, while others can only view.
"""

"""
BookDetailView: Handles GET, PUT, DELETE requests to retrieve, update, or delete a book by its ID.
Permission: Only authenticated users can update or delete books.
"""

### Running Unit Tests for API Endpoints

1. To run the tests, use the following command:
   ```bash
   python manage.py test api