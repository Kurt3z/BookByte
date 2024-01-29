from django.contrib import admin

from .models.author import Author
from .models.book import Book

admin.site.register(Book)
admin.site.register(Author)
