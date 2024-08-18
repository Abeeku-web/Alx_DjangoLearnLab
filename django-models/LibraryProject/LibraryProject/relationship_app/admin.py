from django.contrib import admin
from .models import Author, Book, Library, Librarian

# Registering the models with the admin site
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)

