from django.urls import path

from . import views


urlpatterns = [
    path("requisitions/", views.requisitions, name="requisitions"),
]
