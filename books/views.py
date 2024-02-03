from django.shortcuts import render, redirect

from .models import Book, Author


def books(request):
    books = Book.objects.all()
    context = {
        "books": books
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
