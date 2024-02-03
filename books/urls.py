from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.books, name="books"),
    path("<slug:slug>/", views.book, name="book")
]
