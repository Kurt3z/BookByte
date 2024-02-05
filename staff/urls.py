from django.urls import path

from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),


    path("books-dashboard/", views.booksDashboard, name="books-dashboard"),
    path("books-dashboard/add-book/", views.addBook, name="add-book"),
    path("books-dashboard/update-book/<str:pk>/",
         views.updateBook, name="update-book"),
    path("books-dashboard/delete-book/<str:pk>/",
         views.deleteBook, name="delete-book"),

    path("authors-dashboard/", views.authorsDashboard, name="authors-dashboard"),
    path("authors-dashboard/add-author/", views.addAuthor, name="add-author"),
    path("authors-dashboard/update-author/<str:pk>/",
         views.updateAuthor, name="update-author"),
    path("authors-dashboard/delete-author/<str:pk>/",
         views.deleteAuthor, name="delete-author"),

    path("publishers-dashboard/", views.publishersDashboard,
         name="publishers-dashboard"),
    path("publishers-dashboard/add-publisher", views.addPublisher,
         name="add-publisher"),
    path("publishers-dashboard/update-publisher/<str:pk>/",
         views.updatePublisher, name="update-publisher"),
    path("publishers-dashboard/delete-publisher/<str:pk>/",
         views.deletePublisher, name="delete-publisher"),

    path("genres-dashboard/", views.genresDashboard, name="genres-dashboard"),
    path("genres-dashboard/add-genre", views.addGenre,
         name="add-genre"),
    path("genres-dashboard/update-genre/<str:pk>/",
         views.updateGenre, name="update-genre"),
    path("genres-dashboard/delete-genre/<str:pk>/",
         views.deleteGenre, name="delete-genre"),
]
