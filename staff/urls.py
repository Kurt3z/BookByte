from django.urls import path

from . import views

urlpatterns = [
    path("book-dashboard/", views.booksDashboard, name="books-dashboard"),
    path("book-dashboard/add-book/", views.addBook, name="add-book"),
    path("book-dashboard/update-book/<str:pk>/",
         views.updateBook, name="update-book"),
    path("book-dashboard/delete-book/<str:pk>/",
         views.deleteBook, name="delete-book")
]
