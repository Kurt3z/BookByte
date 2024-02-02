from django.forms import ModelForm
from django import forms

from .models import Publisher


class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        exclude = ["id", "created"]

        labels = {
            "name": "Nome",
            "email": "Endereço de Email",
            "website": "Website"
        }
