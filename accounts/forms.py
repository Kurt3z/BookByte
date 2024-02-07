from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Contact


class ContactForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={'placeholder': 'Nome de utilizador'})
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Palavra-passe'})
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirmar palavra-passe'}),
        strip=False
    )

    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={'placeholder': 'Email'})
    )

    first_name = forms.CharField(
        label="First name",
        widget=forms.TextInput(
            attrs={'placeholder': 'Nome'})
    )

    last_name = forms.CharField(
        label="Last name",
        widget=forms.TextInput(
            attrs={'placeholder': 'Apelido'})
    )

    birthdate = forms.DateField(
        label="Birthdate",
        widget=forms.DateInput(format='%d / %m / %Y', attrs={'type': 'date'})
    )

    class Meta:
        model = Contact
        fields = ["username", "password1", "password2",
                  "email", "first_name", "last_name", "birthdate"]