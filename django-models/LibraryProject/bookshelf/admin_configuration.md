# Django Admin Configuration for Book Model

## Registering the Book Model

```python
from django.contrib import admin
from .models import Book

admin.site.register(Book)