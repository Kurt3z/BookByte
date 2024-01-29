from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.books, name="books"),
    path("update-book/<str:pk>/", views.updateBook, name="update-book"),
    path("delete-book/<str:pk>/", views.deleteBook, name="delete-book"),
]
