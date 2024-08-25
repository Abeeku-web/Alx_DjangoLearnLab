from django import forms
from .models import Book  # Ensure this import matches your model

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        widgets = {
            'publication_year': forms.NumberInput(attrs={'type': 'number'}),
        }

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    date_created = forms.DateField(widget=forms.SelectDateWidget)