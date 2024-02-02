from django.forms import ModelForm
from django import forms

from .models import Publisher, Genre


class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        exclude = ["id", "created"]

        labels = {
            "name": "Nome",
            "email": "Endereço de Email",
            "website": "Website"
        }


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        exclude = ["id", "created"]

        labels = {
            "caption": "Género"
        }
