import django_filters
from django.db.models import Q
from django import forms

from .models import Book


class BookFilter(django_filters.FilterSet):
    title_isbn_author = django_filters.CharFilter(
        method="fitler_title_isbn_author",
        label="Search",
        widget=forms.TextInput(
            attrs={'placeholder': 'Pesquisar por título, autor ou ISBN...'}),
    )

    class Meta:
        model = Book
        fields = ["title_isbn_author",
                  "genre", "publisher", "language"]
        exclude = ["id", "created", "cover",
                   "publication_date", "quantity", "summary", "pages", "title", "isbn", "slug", "author"]

    def fitler_title_isbn_author(self, queryset, name, value):
        keywords = value.split()

        q_objects = Q()

        for keyword in keywords:
            q_objects |= (
                Q(title__icontains=keyword) |
                Q(isbn__icontains=keyword) |
                Q(author__first_name__icontains=keyword) |
                Q(author__last_name__icontains=keyword)
            )

        return queryset.filter(q_objects).distinct()
