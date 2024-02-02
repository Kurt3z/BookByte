from django.forms import ModelForm
from django import forms

from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "genre", "publisher", "publication_date", "summary",
                  "isbn", "cover", "pages", "quantity", "language",
                  "format"]

        labels = {
            "title": "Título",
            "author": "Autor",
            "genre": "Géneros",
            "publisher": "Editora",
            "publication_date": "Data de Publicação",
            "summary": "Sinopse",
            "isbn": "ISBN",
            "cover": "Capa",
            "pages": "Páginas",
            "quantity": "Quantidade",
            "language": "Linguagem",
            "format": "Formato"
        }

        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
        }
