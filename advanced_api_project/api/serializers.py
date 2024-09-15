from rest_framework import serializers
from .models import Author, Book
import datetime

"""
BookSerializer serializes the Book model and includes validation for the publication year.
AuthorSerializer includes the name field and a nested representation of the related books using BookSerializer.
"""

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        if value > datetime.date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
