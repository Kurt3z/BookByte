from django.shortcuts import render

from books.models import Book, Author


def index(request):
    books = Book.objects.order_by("-created")[:6]
    authors = Author.objects.order_by("-created")[:2]

    context = {
        "books": books,
        "authors": authors
    }

    return render(request, "models/index.html", context)
