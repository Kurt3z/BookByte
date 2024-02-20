import random
from django.shortcuts import render


from books.models import Book, Author


def index(request):
    books = Book.objects.order_by("-created")[:6]
    authors = Author.objects.all()

    number1 = random.randint(0, len(authors) - 1)
    number2 = random.randint(0, len(authors) - 1)

    random_authors = []
    random_authors.append(authors[number1])
    random_authors.append(authors[number2])

    context = {
        "books": books,
        "authors": random_authors
    }

    return render(request, "models/index.html", context)
