from django.shortcuts import render, redirect

from books.models import Book
from books.forms import BookForm


def booksDashboard(request):
    books = Book.objects.all()
    context = {
        "books": books
    }

    return render(request, "staff/books-dashboard.html", context)


def addBook(request):
    form = BookForm()

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect("books-dashboard")

    context = {
        "form": form
    }
    return render(request, "staff/book-form.html", context)


def updateBook(request, pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("books-dashboard")

    context = {
        "form": form
    }

    return render(request, "staff/book-form.html", context)


def deleteBook(request, pk):
    book = Book.objects.get(id=pk)

    if request.method == "POST":
        book.delete()
        return redirect("books-dashboard")

    context = {
        "book": book
    }

    return render(request, "staff/delete-book.html", context)
