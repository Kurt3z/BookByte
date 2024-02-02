from django.shortcuts import render, redirect

from books.models import Book, Author
from books.forms import BookForm, AuthorForm
from models.models import Publisher
from models.forms import PublisherForm


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


def publishersDashboard(request):
    publishers = Publisher.objects.all()
    context = {
        "publishers": publishers
    }

    return render(request, "staff/publisher-dashboard.html", context)

# Do the same dashboard for every model


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
        "page": "Livro",
        "type": "Criar"
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
        "form": form,
        "type": "Editar"
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
        "page": "Autor",
        "type": "Criar"
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
        "form": form,
        "type": "Editar"
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

# PUBLISHER CRUD


def addPublisher(request):
    form = PublisherForm()

    if request.method == "POST":
        form = PublisherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("publishers-dashboard")

    context = {
        "form": form,
        "page": "Editora",
        "type": "Criar"
    }
    return render(request, "staff/form.html", context)


def updatePublisher(request, pk):
    publisher = Publisher.objects.get(id=pk)
    form = PublisherForm(instance=publisher)

    if request.method == "POST":
        form = PublisherForm(request.POST, request.FILES, instance=publisher)
        if form.is_valid():
            form.save()
            return redirect("publishers-dashboard")

    context = {
        "form": form,
        "type": "Editar"
    }

    return render(request, "staff/form.html", context)


def deletePublisher(request, pk):
    publisher = Publisher.objects.get(id=pk)

    if request.method == "POST":
        publisher.delete()
        return redirect("publishers-dashboard")

    context = {
        "object": publisher
    }

    return render(request, "staff/delete.html", context)

# GENRES CRUD
