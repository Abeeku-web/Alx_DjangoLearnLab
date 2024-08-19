from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    #Customize the list display
    list_display = ('title','author','publication_year')

    #Add search fields
    search_fields = ('title','author')

    #Add list filters
    list_filter = ('publication_year',)