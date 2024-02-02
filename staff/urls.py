from django.urls import path

from . import views

urlpatterns = [
    path("book-dashboard/", views.booksDashboard, name="books-dashboard"),
    path("book-dashboard/add-book/", views.addBook, name="add-book"),
    path("book-dashboard/update-book/<str:pk>/",
         views.updateBook, name="update-book"),
    path("book-dashboard/delete-book/<str:pk>/",
         views.deleteBook, name="delete-book"),

    path("author-dashboard/", views.authorsDashboard, name="authors-dashboard"),
    path("author-dashboard/add-author/", views.addAuthor, name="add-author"),
    path("author-dashboard/update-author/<str:pk>/",
         views.updateAuthor, name="update-author"),
    path("book-dashboard/delete-author/<str:pk>/",
         views.deleteAuthor, name="delete-author"),
]
