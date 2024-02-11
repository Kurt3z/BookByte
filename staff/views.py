from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from books.models import Book, Author
from books.forms import BookForm, AuthorForm
from models.models import Publisher, Genre
from models.forms import PublisherForm, GenreForm
from requisitions.models import Requisition

from books.filters import BookFilter
from books.utils import paginateBooks


def is_librarian(user):
    return hasattr(user, "librarian") or user.is_superuser


@login_required(login_url="login")
@user_passes_test(is_librarian)
def dashboard(request):
    # total_books = Book.objects.count()
    total_books = 0
    total_movies = 0
    open_requisitions = Requisition.objects.filter(
        is_delivered=False, is_complete=True)

    context = {
        "total_books": total_books,
        "total_movies": total_movies,
        "requisitions": open_requisitions
    }

    return render(request, "staff/dashboard.html", context)


@login_required(login_url="login")
@user_passes_test(is_librarian)
def booksDashboard(request):
    books = Book.objects.all()
    myFilter = BookFilter(request.GET, queryset=books)
    books = myFilter.qs
    custom_range, books = paginateBooks(request, books, 8)

    context = {
        "books": books,
        "myFilter": myFilter,
        "custom_range": custom_range
    }

    return render(request, "staff/books-dashboard.html", context)


@login_required(login_url="login")
@user_passes_test(is_librarian)
def authorsDashboard(request):
    authors = Author.objects.all()
    custom_range, authors = paginateBooks(request, authors, 8)

    context = {
        "authors": authors,
        "custom_range": custom_range
    }

    return render(request, "staff/authors-dashboard.html", context)


@login_required(login_url="login")
@user_passes_test(is_librarian)
def publishersDashboard(request):
    publishers = Publisher.objects.all()
    custom_range, publishers = paginateBooks(request, publishers, 8)

    context = {
        "publishers": publishers,
        "custom_range": custom_range
    }

    return render(request, "staff/publishers-dashboard.html", context)


@login_required(login_url="login")
@user_passes_test(is_librarian)
def genresDashboard(request):
    genres = Genre.objects.all()
    custom_range, genres = paginateBooks(request, genres, 16)
    context = {
        "genres": genres,
        "custom_range": custom_range
    }

    return render(request, "staff/genres-dashboard.html", context)


# BOOKS CRUD
@login_required(login_url="login")
@user_passes_test(is_librarian)
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


@login_required(login_url="login")
@user_passes_test(is_librarian)
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


@login_required(login_url="login")
@user_passes_test(is_librarian)
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
@login_required(login_url="login")
@user_passes_test(is_librarian)
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


@login_required(login_url="login")
@user_passes_test(is_librarian)
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


@login_required(login_url="login")
@user_passes_test(is_librarian)
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


@login_required(login_url="login")
@user_passes_test(is_librarian)
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


@login_required(login_url="login")
@user_passes_test(is_librarian)
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


@login_required(login_url="login")
@user_passes_test(is_librarian)
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


@login_required(login_url="login")
@user_passes_test(is_librarian)
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


@login_required(login_url="login")
@user_passes_test(is_librarian)
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


@login_required(login_url="login")
@user_passes_test(is_librarian)
def deleteGenre(request, pk):
    genre = Genre.objects.get(id=pk)

    if request.method == "POST":
        genre.delete()
        return redirect("genres-dashboard")

    context = {
        "object": genre
    }

    return render(request, "staff/delete.html", context)


def deliverRequisition(request, pk):
    requisition = Requisition.objects.get(id=pk)

    if request.method == "POST":
        requisition.is_delivered = True

        for content in requisition.contents.all():
            content.quantity += 1
            content.save()

        requisition.save()

        return redirect("dashboard")
