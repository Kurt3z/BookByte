import uuid
from django.core.validators import RegexValidator

from django.db import models
from django.contrib.auth.models import AbstractUser

from models.models.district import District


class Contact(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=500, unique=True)
    birthdate = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    street = models.CharField(max_length=500, null=True)
    building = models.PositiveIntegerField(null=True)
    postal_code = models.CharField(max_length=8, validators=[
        RegexValidator(regex="^\d{4}-\d{3}$", message="Insira um Código-Postal válido.")], null=True)
    district = models.ForeignKey(
        District, on_delete=models.SET_NULL, null=True)
    profile_image = models.ImageField(
        upload_to="profiles/", default="user-default.jpg", null=True)


class Reader(models.Model):
    user = models.OneToOneField(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Librarian(models.Model):
    user = models.OneToOneField(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
