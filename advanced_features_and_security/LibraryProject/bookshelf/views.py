from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
       form = BookForm(request.POST)
        if form.is_valid():
            # Safe handling of form data
            form.save()
            # Redirect or respond after saving
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # handle book update
        pass
    return render(request, 'bookshelf/edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # handle book deletion
        book.delete()
        # redirect after deletion
    return render(request, 'bookshelf/delete_book.html', {'book': book})
