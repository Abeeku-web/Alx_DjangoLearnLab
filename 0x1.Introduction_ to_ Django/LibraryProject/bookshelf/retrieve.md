# Retrieve Operation

```python
# Retrieve the book instance
retrieved_book = Book.objects.get(id=book.id)

# Display book details
print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)

#Expected Output
"1984"