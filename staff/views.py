from django.shortcuts import render, redirect

from books.models import Book, Author
from books.forms import BookForm, AuthorForm


def booksDashboard(request):
    books = Book.objects.all()
    context = {
        "books": books
    }

    return render(request, "staff/books-dashboard.html", context)


def authorsDashboard(request):
    authors = Author.objects.all()
    context = {
        "authors": authors
    }

    return render(request, "staff/authors-dashboard.html", context)


# BOOKS CRUD

def addBook(request):
    form = BookForm()

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("books-dashboard")

    context = {
        "form": form,
        "page": "Autor"
    }
    return render(request, "staff/form.html", context)


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

    return render(request, "staff/form.html", context)


def deleteBook(request, pk):
    book = Book.objects.get(id=pk)

    if request.method == "POST":
        book.delete()
        return redirect("books-dashboard")

    context = {
        "object": book
    }

    return render(request, "staff/delete.html", context)


# AUTHORS CRUD

def addAuthor(request):
    form = AuthorForm()

    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("authors-dashboard")

    context = {
        "form": form,
        "page": "Autor"
    }

    return render(request, "staff/form.html", context)


def updateAuthor(request, pk):
    author = Author.objects.get(id=pk)
    form = AuthorForm(instance=author)

    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            return redirect("authors-dashboard")

    context = {
        "form": form
    }

    return render(request, "staff/form.html", context)


def deleteAuthor(request, pk):
    author = Author.objects.get(id=pk)

    if request.method == "POST":
        author.delete()
        return redirect("authors-dashboard")

    context = {
        "object": author
    }

    return render(request, "staff/delete.html", context)
