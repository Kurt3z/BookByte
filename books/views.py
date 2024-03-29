from django.shortcuts import render, redirect

from .models import Book, Author
from .filters import BookFilter
from .utils import paginateBooks


def books(request):
    books = Book.objects.all()
    myFilter = BookFilter(request.GET, queryset=books)
    books = myFilter.qs
    custom_range, books = paginateBooks(request, books, 16)

    myFilter.form.fields['genre'].label = "Género"
    myFilter.form.fields['publisher'].label = "Editora"
    myFilter.form.fields['language'].label = "Idioma"

    context = {
        "books": books,
        "myFilter": myFilter,
        "custom_range": custom_range,
        "reset_form_redirect": "books"
    }

    return render(request, "books/books.html", context)


def book(request, slug):
    book = Book.objects.get(slug=slug)
    context = {
        "book": book
    }

    return render(request, "books/book-detail.html", context)


def author(request, slug):
    author = Author.objects.get(slug=slug)
    context = {
        "author": author
    }

    return render(request, "books/author-detail.html", context)
