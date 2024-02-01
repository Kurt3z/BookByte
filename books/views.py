from django.shortcuts import render, redirect

from .models import Book


def books(request):
    books = Book.objects.all()
    context = {
        "books": books
    }

    return render(request, "books/books.html", context)
