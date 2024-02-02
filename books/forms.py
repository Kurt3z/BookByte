from django.forms import ModelForm
from django import forms

from .models import Book, Author


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


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ["first_name", "last_name", "birthdate",
                  "country", "biography", "personal_website", "picture"]

        labels = {
            "first_name": "Nome",
            "last_name": "Apelido",
            "birthdate": "Data de Nascimento",
            "country": "Nacionalidade",
            "biography": "Biografia",
            "personal_website": "Website Pessoal",
            "picture": "Foto"
        }

        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
        }
