from django.forms import ModelForm
from django import forms

from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "publication_date", "quantity",
                  "summary", "cover", "publisher", "genre", "language",
                  "isbn", "pages", "format", "author"]
