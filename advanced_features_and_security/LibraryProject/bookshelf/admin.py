from django.contrib import admin
from .models import Book

# Register your models here.
admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    #Customize the list display
    list_display = ('title','author','publication_year')

    #Add search fields
    search_fields = ('title','author')

    #Add list filters
    list_filter = ('publication_year',)

# Register the Book model with the customized admin class
admin.site.register(Book, BookAdmin)