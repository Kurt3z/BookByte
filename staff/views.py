from django.shortcuts import render, redirect

from books.models import Book, Author
from books.forms import BookForm, AuthorForm
from models.models import Publisher, Genre
from models.forms import PublisherForm, GenreForm


def dashboard(request):
    # total_books = Book.objects.count()
    total_books = 0
    total_movies = 0

    context = {
        "total_books": total_books,
        "total_movies": total_movies
    }

    return render(request, "staff/dashboard.html", context)


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

    return render(request, "staff/publishers-dashboard.html", context)


def genresDashboard(request):
    genres = Genre.objects.all()
    context = {
        "genres": genres
    }

    return render(request, "staff/genres-dashboard.html", context)


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


def addGenre(request):
    form = GenreForm()

    if request.method == "POST":
        form = GenreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("genres-dashboard")

    context = {
        "form": form,
        "page": "Género",
        "type": "Criar"
    }

    return render(request, "staff/form.html", context)


def updateGenre(request, pk):
    genre = Genre.objects.get(id=pk)
    form = GenreForm(instance=genre)

    if request.method == "POST":
        form = GenreForm(request.POST, request.FILES, instance=genre)
        if form.is_valid():
            form.save()
            return redirect("genres-dashboard")

    context = {
        "form": form,
        "type": "Editar"
    }

    return render(request, "staff/form.html", context)


def deleteGenre(request, pk):
    genre = Genre.objects.get(id=pk)

    if request.method == "POST":
        genre.delete()
        return redirect("genres-dashboard")

    context = {
        "object": genre
    }

    return render(request, "staff/delete.html", context)
