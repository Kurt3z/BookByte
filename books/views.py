from django.shortcuts import render, redirect

from .models import Book
from .forms import BookForm


def books(request):
    books = Book.objects.all()
    context = {
        "books": books
    }

    return render(request, "books/books.html", context)


def updateBook(request, slug):
    book = Book.objects.get(slug=slug)
    form = BookForm(instance=book)

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("books")

    context = {
        "form": form
    }
    return render(request, "books/book-form.html", context)
