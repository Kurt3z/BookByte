import uuid
from autoslug import AutoSlugField
from django.db import models

from models.models import Country


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, null=True, blank=True)
    biography = models.TextField()
    personal_website = models.URLField(blank=True, null=True)
    picture = models.ImageField(upload_to="authors/")
    slug = AutoSlugField(populate_from="title", unique=True,
                         db_index=True, editable=False, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
