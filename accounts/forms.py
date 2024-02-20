from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Contact


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            "first_name", "last_name",
            "gender", "street", "building", "postal_code", "district", "profile_image"
        ]

        labels = {
            "first_name": "Nome", "last_name": "Apelido",
            "gender": "Género", "street": "Rua", "building": "Porta",
            "postal_code": "Código Postal", "district": "Distrito"
        }


class ContactForm(UserCreationForm):
    class Meta:
        model = Contact
        fields = ["username", "password1", "password2",
                  "email", "first_name", "last_name", "birthdate"]

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.base_fields.items():
            field.error_messages['required'] = "Este campo não pode ser submetido vazio."
