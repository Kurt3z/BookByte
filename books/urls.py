from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.books, name="books"),
    path("update-book/<slug:slug>/", views.updateBook, name="update-book")
]
