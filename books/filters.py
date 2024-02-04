import django_filters
from django.db.models import Q
from django import forms

from .models import Book


class BookFilter(django_filters.FilterSet):
    title_isbn = django_filters.CharFilter(
        method="fitler_title_isbn",
        label="Search",
        widget=forms.TextInput(
            attrs={'placeholder': 'Pesquisar por título ou ISBN...'}),
    )

    class Meta:
        model = Book
        fields = ["title_isbn", "author", "publisher", "genre", "language"]
        exclude = ["id", "created", "cover",
                   "publication_date", "quantity", "summary", "pages", "title", "isbn", "slug"]

    def fitler_title_isbn(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) |
            Q(isbn__icontains=value)
        )
